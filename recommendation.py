from data_extraction import data_extraction, challenge_info, challenge_students
from data_extraction import challenge_info
from filtering import filtering
from formatted import formatted

def corpus_builder(challenge_id, context=False, nickname=None, maxq=1, duplicates=False, sentences=False):
    data = data_extraction(challenge_id) # por desafio    
    if nickname is not None:
        ch_students = challenge_students(challenge_id)
        if nickname not in ch_students:
            return 'El estudiante no es válido'
    #return data
    filtered_data = filtering(data, nickname, maxq, duplicates) # por usuario unico o todos
    if context:
        ch_info = challenge_info(challenge_id)
        filtered_data = filtered_data.append(ch_info).reset_index(drop=True) # un solo reset en el paso previo a la entrega
    #return filtered_data
    words = formatted(filtered_data, sentences) # ahora cada snippet por separado
    return words
 
    
    
    


     