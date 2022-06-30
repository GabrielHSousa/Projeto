import mysql.connector

import requests
from bs4 import BeautifulSoup
import mysql.connector #Faz acesso ao mysql
from mysql.connector import errorcode #Trata as exceções que vão surgir


def cidade():

    loca = input('Digite a cidade que quer saber a previsão do tempo:')
    busca = f'A previsão do tempo em {loca} é de '
    url = f'https://www.google.com/search?q={busca}'
    r = requests.get(url)
    s = BeautifulSoup(r.text,'html.parser')
    update = s.find('div',class_='BNeawe').text
    a = (busca + update)
    print(a)



def conectar():
    try:
        db_connection = mysql.connector.connect(host='localhost',
                                                user='root',
                                                password='',
                                                database='Projeto')
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
        db_connection.close()

