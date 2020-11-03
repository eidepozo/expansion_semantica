from data_extraction import data_extraction, challenge_info, challenge_students
from data_extraction import challenge_info
from filtering import filtering
from formatted import formatted

from gensim.models import Word2Vec

def model_build(challenge_id, context=False, nickname=None, maxq=1, minimum=40, window=5):
    data = data_extraction(challenge_id) # por desafio    
    if nickname is not None:
        ch_students = challenge_students(challenge_id)
        if nickname not in ch_students:
            return 'El estudiante no es válido'
    #return data
    filtered_data = filtering(data, nickname, maxq) # por usuario unico o todos
    if context:
        ch_info = challenge_info(challenge_id)
        filtered_data = filtered_data.append(ch_info).reset_index(drop=True) # un solo reset en el paso previo a la entrega
    #return filtered_data
    words = formatted(filtered_data) # ahora cada snippet por separado
    #return words
    model = Word2Vec(words, min_count=minimum, sg=1, window=window)
    return model
    
    
    


     