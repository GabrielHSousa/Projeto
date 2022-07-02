import mysql.connector
import previsao
import requests
from bs4 import BeautifulSoup


db_connection = previsao.conectar()
con = db_connection.cursor()

def inserir(cidade,graus):
    try:
        sql = "insert into localizacao(codigo,cidade,graus) values('','{}','{}')".format(cidade,graus)
        con.execute(sql)
        db_connection.commit()
        print("{} inserido".format(con.rowcount))
    except Exception as erro:
        return erro

def cidade():
    loca = input('Digite a cidade que quer saber a previsão do tempo:')
    busca = f'A previsão do tempo em {loca} é de '
    url = f'https://www.google.com/search?q={busca}'
    r = requests.get(url)
    s = BeautifulSoup(r.text,'html.parser')
    update = s.find('div',class_='BNeawe').text
    a = (busca + update)
    print(a)
    inserir(loca,a)