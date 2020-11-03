#https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists
    
import pymysql
import pandas as pd

def data_extraction(challenge_id):
    query = "SELECT date_executed, FK_challenge_id_number, FK_student_nick,id_number,query,snippet \
        FROM Students_query\
        INNER JOIN Students_queries_results ON FK_student_query_id_number = id_number\
        WHERE FK_challenge_id_number = id_desafio AND FK_student_nick != 'test_student'\
        AND date_executed BETWEEN '2019-04-29 00:00:00' AND '2019-04-29 23:59:59'\
        ORDER BY date_executed, FK_student_nick" 
    query = query.replace('id_desafio', str(challenge_id)) # ahora se incluye un orden para facilitar la busqueda
    conn = pymysql.connect(host='localhost', user='root',
                       passwd='rotted',db='gonsa2')
    data = pd.read_sql(query, conn)   
    conn.close()
    return data

def challenge_info(challenge_id):
    query = "SELECT summary, description, aim FROM all_challenges \
    WHERE id_number = id_desafio"
    query = query.replace('id_desafio', str(challenge_id)) 
    conn = pymysql.connect(host='localhost', user='root',
                       passwd='rotted',db='gonsa2')
    ch_info = pd.read_sql(query, conn)
    ch_info = ch_info.iloc[0] # ahora se entrega como una serie, igual que la data filtrada
    conn.close()
    return ch_info

def challenge_students(challenge_id):
    query = "SELECT DISTINCT FK_student_nick FROM Students_query \
    WHERE FK_challenge_id_number = id_desafio \
    AND date_executed BETWEEN '2019-04-29 00:00:00' AND '2019-04-29 23:59:59'\
    AND FK_student_nick != 'test_student'"
    query = query.replace('id_desafio', str(challenge_id)) 
    conn = pymysql.connect(host='localhost', user='root',
                       passwd='rotted',db='gonsa2')
    ch_students = pd.read_sql(query, conn)
    ch_students = ch_students.values.tolist()
    flat_ch_students = [item for sublist in ch_students for item in sublist]
    conn.close()
    return flat_ch_students
    
    
