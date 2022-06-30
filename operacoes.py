import mysql.connector
import previsao

db_connection = previsao.conectar()
con = db_connection.close

def inserir(codigo,cidade,graus):
    try:
        sql = "insert into localizacao(codigo,cidade,graus) values('','{}','{}')".format(codigo,cidade,graus)
        con.execute(sql)
        db_connection.commit()
        print("{} inserido".format(codigo,cidade,graus))
    except Exception as erro:
        return erro