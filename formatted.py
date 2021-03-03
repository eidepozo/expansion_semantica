from preprocessing import preprocessing
from nltk.corpus import stopwords
from nltk import sent_tokenize, word_tokenize

def formatted(filtered_data, sentences): # ahora snippet completo o por sentencia
    filtered_data = filtered_data.tolist()
    if sentences:
        filtered_data = [sent_tokenize(paragraph, language='spanish') for paragraph in filtered_data]
        filtered_data = [item for sublist in filtered_data for item in sublist] #flat
    
    preprocessed_data = [preprocessing(snippet) for snippet in filtered_data]
    all_words = [word_tokenize(snippet) for snippet in preprocessed_data]
    
    es_sw = stopwords.words('spanish')
    es_sw.extend(['si', 'asi', 'ser', 'tener', 'mas']) 
    en_sw = stopwords.words('english')
    en_sw.extend(['www', 'com'])
    for i in range(len(all_words)):
        all_words[i] = [w for w in all_words[i] if w not in es_sw and w not in en_sw and len(w)>1] #filtro adicional
    all_words = [w for w in all_words if w] # filtro para listas vacias
    return all_words