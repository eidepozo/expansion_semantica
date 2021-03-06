from sklearn.metrics.pairwise import linear_kernel
import numpy as np
from collections import OrderedDict, Counter
from bing_search import bing_search_alt
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import pandas as pd

def group_matrix(df, tf):
    S = [sim_matrix(tf, row[0], row[1], row[2], row[3]) for row in df[['query', 'snippet1', 'snippet2', 'snippet3']].values]
    S = np.asarray(S) # casteo como np
    return S

#https://stackoverflow.com/questions/12118720/python-tf-idf-cosine-to-find-document-similarity
    
def sim_matrix(tf, q, s1, s2, s3):
    # vectorizacion
    tfidf_matrix = tf.fit_transform([q,s1,s2,s3]) # corpus, tdif_matrix[0] corresponde a la matriz de la query
    #print (tf.get_feature_names())
    S = []
    for i in range(4): # largo del corpus
        S.append(linear_kernel(tfidf_matrix[i], tfidf_matrix).flatten()) # similaridad del coseno 
    return S

#https://pymotw.com/2/collections/ordereddict.html
#https://www.quora.com/Where-can-I-find-a-maximum-marginal-relevance-algorithm-in-Python-for-redundancy-removal-in-two-documents
#http://www.cs.bilkent.edu.tr/~canf/CS533/hwSpring14/eightMinPresentations/handoutMMR.pdf

def MMR_score(S, docs=[1,2,3], lambda_=0.5):
    selected = OrderedDict()
    init_idx= np.argmax(S[0][1::]) + 1 # el indice del d con mayor similaridad a q
    selected[init_idx] = S[init_idx,0]
    while Counter(selected.keys()) != Counter(docs): # comparar la lista de docs con los seleccionados
        remaining = [x for x in docs if x not in selected]
        mmr_score = lambda x: lambda_*S[x, 0] - (1-lambda_)*max([S[x, y] for y in selected]) # definicion del puntaje
        result = {k: mmr_score(k) for k in remaining}
        next_selected = max(result, key=result.get) 
        selected[next_selected] = result[next_selected]
    return selected


def sum_cos_df(model,df,user_id, size): # dataframe de palabra incluida, similaridad y sum_cos
    #vocab = list(model.wv.vocab)
    #size = len(list(model.wv.vocab)) #673
    q = df.iloc[user_id][1] # query original
    try:
        all_sims=(model.wv.most_similar([q.split()[-1]], topn=size))
    except KeyError:
        print("Esta palabra no aparece en el modelo")
    nsdf, sum_cos = sum_cos_array(size,all_sims, q)
    sdf = pd.DataFrame(sum_cos, columns=['sum_cos'])
    wadf = pd.DataFrame([i[0] for i in all_sims], columns=['word_added'])
    prdf = pd.DataFrame([i[1] for i in all_sims], columns=['similarity_w'])
    df2 = pd.concat([wadf,nsdf, prdf, sdf], axis=1)
    return df2

def sum_cos_array(size, all_sims, q): # arreglo de sum_cos, realiza nueva busqueda
    sum_cos = np.zeros(size)
    es_sw = stopwords.words('spanish')
    nsdf = pd.DataFrame(columns = ['s1','s2','s3'])
    for i in range(size):
        #print (i) # contador scrap
        nq = q + ' '+all_sims[i][0]
        res = bing_search_alt(nq)
        a_series = pd.Series(res, index = nsdf.columns)
        nsdf = nsdf.append(a_series, ignore_index=True) # df con nuevos snippets
        tf = TfidfVectorizer(stop_words=es_sw) # no se si es necesario
        try: 
            S = np.asarray(sim_matrix(tf, nq, res[0], res[1], res[2]))
        except IndexError: # ante insuficientes snippets
            print ("Palabra N %d : %s" %(i, all_sims[i][0]))
            return nsdf, sum_cos # ultimo estado matriz
        sum_cos[i] = S[1,2] + S[1,3] + S[2,3]
    return nsdf, sum_cos


    