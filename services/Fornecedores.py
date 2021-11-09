from services.Conexao import Conexao
import json


class Fornecedores(Conexao):

    def inserirFornecedor(self, valores):
        cursor = self.conexao.cursor()
        try:
            query_sql = "INSERT INTO fornecedor VALUES (null, %s, %s, %s, %s)"
            cursor.execute(query_sql, valores)
            self.conexao.commit()

            if cursor.rowcount < 1:
                return 0

            return cursor.rowcount
        except Exception as e:
            return e

    def listarFornecedores(self):
        cursor = self.conexao.cursor()
        try:
            query_sql = "SELECT * FROM fornecedor"
            cursor.execute(query_sql)
            resultado = cursor.fetchall()

            if len(resultado) == 0:
                return 0

            dados_json = {}
            for data in resultado:
                dados_json.update({
                    data[0]: {
                        "razao_social": data[1],
                        "nome_fantasia": data[2],
                        "cnpj": data[3],
                        "telefone_contato": data[4]
                    }
                })
            return json.dumps(dados_json)
        except Exception as e:
            return e

    def selecionarPorId(self, id):
        cursor = self.conexao.cursor()
        try:
            query_sql = f"SELECT * FROM fornecedor WHERE id = {id}"
            cursor.execute(query_sql)
            result = cursor.fetchall()
            data_json = {}
            for dado in result:
                data_json.update({
                    "id": dado[0],
                    "razaosocial": dado[1],
                    "nomefantasia": dado[2],
                    "cnpj": dado[3],
                    "telefone": int(dado[4])
                })
            return json.dumps(data_json)
        except Exception as e:
            return e

    def atualizarFornecedor(self, data, id):
        cursor = self.conexao.cursor()
        try:
            query_sql = f"UPDATE fornecedor SET {data} WHERE id = {id}"
            cursor.execute(query_sql)
            self.conexao.commit()

            if cursor.rowcount < 1:
                return 0

            return cursor.rowcount
        except Exception as e:
            return e