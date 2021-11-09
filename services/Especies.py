from services.Conexao import Conexao
import json

class Especie(Conexao):

    def inserirEspecie(self, data):
        cursor = self.conexao.cursor()
        try:
            query_sql = "INSERT INTO especie VALUES (null, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query_sql, data)
            self.conexao.commit()

            if cursor.rowcount < 1:
                return 0

            return cursor.rowcount
        except Exception as e:
            return e

    def listarEspecies(self):
        cursor = self.conexao.cursor()
        try:
            query_sql = "SELECT * FROM especie as e JOIN fornecedor as f on f.id = e.fornecedor"
            cursor.execute(query_sql)
            result = cursor.fetchall()

            if len(result) == 0:
                return 0

            data_json = {}
            for data in result:
                data_json.update({
                    # DESAFIO
                })
            return json.dumps(data_json)
        except Exception as e:
            return e