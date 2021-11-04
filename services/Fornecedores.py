from services.Conexao import Conexao
import json


class Fornecedores(Conexao):

    def inserirFornecedor(self, valores):
        cursor = self.conexao.cursor()
        try:
            query_sql = "INSERT INTO fornecedor VALUES (null, %s, %s, %s, %s)"
            cursor.execute(query_sql, valores)
            self.conexao.commit()

            if cursor.rowcount == 0:
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
                return json.dumps({
                    "mensagem": "Nenhum dado para exibir"
                })

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


        # DESAFIO - Façam os métodos atualizarFornecedor e selecionarFornecedorPorId