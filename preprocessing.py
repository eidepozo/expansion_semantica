#https://pypi.org/project/Unidecode/
#https://gist.github.com/j4mie/557354
    
    
from unidecode import unidecode
import re

def preprocessing(texto):
    textof = texto.lower()
    textof = re.sub('[^a-zá-úñü]', ' ', textof) # solo letras
    textof = re.sub(r'\s+', ' ', textof) #sin espacios adicionales (al menos un espacio)
    return textof