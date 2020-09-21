#https://pypi.org/project/Unidecode/
#https://gist.github.com/j4mie/557354
    
    
from unidecode import unidecode
import re

def preprocessing(aux, corpus):
    pp_corpus = corpus.lower()
    pp_corpus = pp_corpus.replace('ñ',aux) # caso particular
    pp_corpus = unidecode(pp_corpus) # unaccented
    pp_corpus = re.sub('[^a-zA-Z]', ' ', pp_corpus) # solo letras
    pp_corpus = re.sub(r'\s+', ' ', pp_corpus) #sin espacios adicionales
    pp_corpus = pp_corpus.replace(aux,'ñ')
    return pp_corpus