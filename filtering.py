#https://stackoverflow.com/questions/52281025/pandas-select-first-3-rows-with-distinct-values-in-specific-column
    
import pandas as pd
from bs4 import BeautifulSoup

def filtering(data, nickname, maxq, duplicates): 
    uid_number = data.drop_duplicates(['id_number', 'FK_student_nick']).groupby('FK_student_nick').head(maxq)['id_number'].tolist()
    filtered_data = data[data['id_number'].isin(uid_number)] # Filtro para obtener los snippet de la primera query de todos
    
    if nickname is not None: # cuando es un solo usuario solo toma sus queries
        filtered_data = filtered_data[filtered_data['FK_student_nick'] == nickname]

    # operaciones comunes
    filtered_data['snippet'] = filtered_data['snippet'].map(lambda text: BeautifulSoup(text, 'html.parser').get_text())
    if not duplicates:
        filtered_data = filtered_data['snippet'].drop_duplicates() # elimino los duplicados
    else:
        filtered_data = filtered_data['snippet']
    return filtered_data