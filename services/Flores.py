from flask import jsonify
from connection.Conexao import Conexao


class Flores(Conexao):

    def inserirFlores(self, dados):
        cursor = self.conexao.cursor()
        try:
            query_sql = "INSERT INTO flores VALUES (null, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query_sql, dados)

            if cursor.rowcount < 1:
                return 0

            return cursor.rowcount
        except Exception as e:
            return e

    def listarFlores(self):
        cursor = self.conexao.cursor()
        try:
            query_sql = "SELECT * FROM flores as f " \
                        "JOIN especie AS e ON e.id = f.especie" \
                        "JOIN categoria AS c ON c.id = f.categoria"
            cursor.execute(query_sql)
            result = cursor.fetchall()

            if len(result) == 0:
                return 0

            data_json = {}
            for data in result:
                data_json.update({
                    data[0]: {
                        "descricao": data[1],
                        "quantidade": int(data[2]),
                        "valorUnitario": float(data[3]),
                        "valorBuque": float(data[4]),
                        "especieFlor": data[8],
                        "tipoAdubo": data[9],
                        "tempoVida": data[10],
                        "intervaloAgua": data[11],
                        "observacoesEspecie": data[12],
                        "descricaoCategoria": data[15],
                    }
                })
            return jsonify(data_json)
        except Exception as e:
            return e

    def listarFloresPorId(self, id):
        cursor = self.conexao.cursor()
        try:
            query_sql = f"SELECT * FROM flores as f " \
                        f"JOIN especie AS e ON e.id = f.especie" \
                        f"JOIN categoria AS c ON c.id = f.categoria" \
                        f"WHERE f.id = {id}"
            cursor.execute(query_sql)
            result = cursor.fetchall()

            if len(result) == 0:
                return 0

            data_json = {}
            for data in result:
                data_json.update({
                    data[0]: {
                        "descricao": data[1],
                        "quantidade": int(data[2]),
                        "valorUnitario": float(data[3]),
                        "valorBuque": float(data[4]),
                        "especieFlor": data[8],
                        "tipoAdubo": data[9],
                        "tempoVida": data[10],
                        "intervaloAgua": data[11],
                        "observacoesEspecie": data[12],
                        "descricaoCategoria": data[15],
                    }
                })
            return jsonify(data_json)
        except Exception as e:
            return e

    def atualizarFlores(self, dados, id):
        cursor = self.conexao.cursor()
        try:
            query_sql = f"UPDATE flores SET {dados} WHERE id = {id}"
            cursor.execute(query_sql)
            self.conexao.commit()

            if cursor.rowcount < 1:
                return 0

            return cursor.rowcount
        except Exception as e:
            return e
