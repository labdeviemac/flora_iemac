from flask import jsonify
from connection.Conexao import Conexao


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
                    data[0]: {
                        "especie": data[1],
                        "tipoadubo": data[2],
                        "tempovida": data[3],
                        "intervaloagua": data[4],
                        "observacoes": data[5],
                        "fornecedor_id": data[6],
                        "razaosocial": data[8],
                        "nomefantasia": data[9],
                        "cnpj": data[10],
                        "telefonefornecedor": data[11]
                    }
                })
            return jsonify(data_json)
        except Exception as e:
            return e

    def listarEspeciePorId(self, id):
        cursor = self.conexao.cursor()
        try:
            query_sql = f"SELECT * FROM especie as e JOIN fornecedor as f on f.id = e.fornecedor WHERE e.id = {id}"
            cursor.execute(query_sql)
            result = cursor.fetchall()

            if len(result) == 0:
                return 0

            data_json = {}
            for data in result:
                data_json.update({
                        "especieid": data[0],
                        "especie": data[1],
                        "tipoadubo": data[2],
                        "tempovida": data[3],
                        "intervaloagua": data[4],
                        "observacoes": data[5],
                        "fornecedor_id": data[6],
                        "razaosocial": data[8],
                        "nomefantasia": data[9],
                        "cnpj": data[10],
                        "telefonefornecedor": data[11]
                })
            return jsonify(data_json)
        except Exception as e:
            return e

    def atualizarEspecie(self, dados, id):
        cursor = self.conexao.cursor()
        try:
            query_sql = f"UPDATE especie SET {dados} WHERE id = {id}"
            cursor.execute(query_sql)
            self.conexao.commit()

            if cursor.rowcount < 1:
                return 0

            return cursor.rowcount
        except Exception as e:
            return e

    def deletarEspecie(self, id):
        cursor = self.conexao.cursor()
        try:
            query_sql = f"DELETE FROM especie WHERE id = {id}"
            cursor.execute(query_sql)
            self.conexao.commit()

            if cursor.rowcount < 1:
                return 0

            return cursor.rowcount
        except Exception as e:
            return e
