from sklearn.metrics.pairwise import linear_kernel
import numpy as np
from collections import OrderedDict, Counter

def group_matrix(df, tf):
    S = [sim_matrix(tf, row[0], row[1], row[2], row[3]) for row in df[['query', 'snippet1', 'snippet2', 'snippet3']].values]
    S = np.asarray(S) # casteo como np
    return S
    
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

def sum_cos(df, S):
    
    