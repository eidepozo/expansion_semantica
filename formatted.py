from preprocessing import preprocessing
import nltk
from nltk.corpus import stopwords

def formatted(dataf, entrega=0):
    if entrega == 0:
        datafd = dataf.str.cat() 
    #se deberia aplicar de la misma forma para ambas opciones
    datafd = preprocessing(datafd)
    
    all_sentences = nltk.sent_tokenize(datafd)
    all_words = [nltk.word_tokenize(sent) for sent in all_sentences] #lista dentro de una lista
 
    es_sw = stopwords.words('spanish') # lista stopword a usar
    es_sw.extend(['si', 'asi', 'ser', 'tener', 'mas']) # no estaban incluidas antes y se repiten bastante
    en_sw = stopwords.words('english') # se incluyen ahora las sw en ingles
    for i in range(len(all_words)):
        all_words[i] = [w for w in all_words[i] if w not in es_sw and w not in en_sw]
    return all_words