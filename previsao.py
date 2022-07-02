import mysql.connector
from mysql.connector import errorcode #Trata as exceções que vão surgir

def conectar():
    try:
        db_connection = mysql.connector.connect(host='localhost',
                                                user='root',
                                                password='',
                                                database='projeto')
        print('Conectado com sucesso!')
        return db_connection

    except mysql.connector.Error as erro: #Guardando as possíveis exceções na variável erro
        if erro.errno == errorcode.ER_BAD_DB_ERROR: #Caso o banco de dados não exista
            print('Banco de dados não existe!, {}'.format(erro))
        elif erro.errno == errorcode.ER_ACCESS_DENIED_ERROR: #Caso o usuário ou senha estejam errados
            print('Usuário ou senha não são válidos!, {}'.format(erro))
        else:
            print(erro)
    else:
        db_connection.close



