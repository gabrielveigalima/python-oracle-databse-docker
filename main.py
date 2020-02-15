import cx_Oracle
import os

#Configurações de conexão
DIALECT = 'oracle'
SQL_DRIVER = 'cx_oracle'

#Pegando as credenciais via variável de ambiente

USERNAME = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASSWORD')
HOST = os.getenv('DB_HOST')
PORT = os.getenv('DB_PORT')
SERVICE = os.getenv('DB_SERVICE')

#Criando a string de conexão

connstr = f"{USERNAME}/{PASSWORD}@{HOST}:{PORT}/{SERVICE}"

#Conectando ao SGBD
conn = cx_Oracle.connect(connstr,encoding = "UTF-8", nencoding = "UTF-8")

#Criando um cursor
cursor = conn.cursor()

#Rodando uma Query para teste
cursor.execute("select * from global_name")
result = cursor.fetchall()
for row in result:
    print(result)
