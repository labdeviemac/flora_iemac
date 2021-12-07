import mysql.connector
import os


class Conexao:

    def __init__(self):
        self.conexao = mysql.connector.connect(
            host=os.environ["HOST"],
            port=os.environ["PORT"],
            user=os.environ["USER"],
            password=os.environ["PASSWORD"],
            database=os.environ["DATABASE"]
        )
