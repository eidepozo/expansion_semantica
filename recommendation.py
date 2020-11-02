from data_extraction import data_extraction, challenge_info, challenge_students
from data_extraction import challenge_info
from filtering import filtering
from formatted import formatted

from gensim.models import Word2Vec

def model_build(challenge_id, context=0, nickname=None, maxq=1, display=0, minimum=40, window=5):
    data = data_extraction(challenge_id) # por desafio
    if context == 1:
        ch_info = challenge_info(challenge_id)
    
    if nickname is not None:
        ch_students = challenge_students(challenge_id)
        if nickname not in ch_students:
            return 'El estudiante no es válido'
      
    filtered_data = filtering(data, nickname, maxq) # por usuario unico o todos
    return filtered_data
    #display(filtered_data)
    #words = formatted(dataf, entrega) # como corpus o articulos (preprocesados), retorna las palabras
    #display(words)
    
    #model = Word2Vec(words, min_count=minimo, sg=1, window=ventana)
    #return model
    
    
    


     