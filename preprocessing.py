#https://pypi.org/project/Unidecode/
#https://gist.github.com/j4mie/557354
    
import re

def preprocessing(text):
    formatted_text = text.lower()
    formatted_text = re.sub('[^a-zá-úñü]', ' ', formatted_text) # solo letras
    formatted_text = re.sub(r'\s+', ' ', formatted_text) #sin espacios adicionales (al menos un espacio)
    return formatted_text