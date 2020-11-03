from preprocessing import preprocessing
import nltk
from nltk.corpus import stopwords

def formatted(filtered_data): # ahora se considera cada snippet por separado
    preprocessed_data = filtered_data.apply(preprocessing)
    formatted_data = preprocessed_data.tolist()
    all_words = [nltk.word_tokenize(snippet) for snippet in formatted_data]
    
    es_sw = stopwords.words('spanish')
    es_sw.extend(['si', 'asi', 'ser', 'tener', 'mas']) 
    en_sw = stopwords.words('english') 
    for i in range(len(all_words)):
        all_words[i] = [w for w in all_words[i] if w not in es_sw and w not in en_sw]
    return all_words