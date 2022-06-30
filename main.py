import mysql.connector
import previsao
import operacoes


if __name__ == "__main__":
    previsao.cidade()
    previsao.conectar()
    operacoes.inserir('1','Ribeirão Pires', 'Graus')