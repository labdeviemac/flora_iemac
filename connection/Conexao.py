import mysql.connector


class Conexao:

    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            port=3307,
            user="flora_user",
            password="fl0r4i3m@c",
            database="flora_iemac"
        )
