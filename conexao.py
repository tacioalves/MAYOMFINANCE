import email
from select import select
from sqlite3 import connect
from xmlrpc.client import boolean
import psycopg2 as pg
import pandas as pd
from sqlalchemy import create_engine

#Configurações de conexão
dadosdeconexao = pg.connect(user = 'tutnuatuykrvsb', password = 'b7983eae81c99a68fce691cb5c70d5f42796db66a5c411c493ecc0972b9cf856', host='ec2-44-205-63-142.compute-1.amazonaws.com', port='5432', database='d9va8hg84qud84') 
#host = 'ec2-44-205-63-142.compute-1.amazonaws.com'
#dbname = 'd9va8hg84qud84'
#user = 'tutnuatuykrvsb'
#port = '5432'
#password = 'b7983eae81c99a68fce691cb5c70d5f42796db66a5c411c493ecc0972b9cf856'
#sslmode = 'require'
#pip freeze > requirements.txt (cria txt)

#String de conexão e String de leitura
engine = create_engine('postgresql://tutnuatuykrvsb:b7983eae81c99a68fce691cb5c70d5f42796db66a5c411c493ecc0972b9cf856@ec2-44-205-63-142.compute-1.amazonaws.com:5432/d9va8hg84qud84')
sql = "select * from usuarios"
df = pd.read_sql_query(sql,con=engine)
#print(df)



#String de inserção
def insereUsuario(usuario,email,senha):
    connection = dadosdeconexao
    curs = connection.cursor()
    sql_insert = ("INSERT INTO usuarios (nome,email,senha,saldo) VALUES ('{0}','{1}','{2}', 0)").format(usuario,email,senha)
    curs.execute(sql_insert)
    connection.commit()

#Faz login

def loginUsuario(emailLogin,senhaLogin):
    connection = dadosdeconexao
    curs = connection.cursor()
    sqlValida = ("SELECT * FROM usuarios where email = '{0}' AND senha = '{1}'").format(emailLogin,senhaLogin)
    curs.execute(sqlValida)
    validaLogin = curs.fetchone()

    return validaLogin




    





