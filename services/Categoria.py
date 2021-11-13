from connection.Conexao import Conexao


class Categoria(Conexao):

    def inserirCategoria(self, values: tuple) -> int | Exception:
        cursor = self.conexao.cursor()
        try:
            query_sql = "INSERT INTO categoria VALUES (null, %s)"
            cursor.execute(query_sql, values)
            self.conexao.commit()

            if cursor.rowcount < 1:
                return 0

            return cursor.rowcount
        except Exception as e:
            return e

    def listarCategorias(self) -> dict | Exception | int:
        cursor = self.conexao.cursor()
        try:
            query_sql = "SELECT * FROM categoria"
            cursor.execute(query_sql)
            result = cursor.fetchall()

            if len(result) == 0:
                return 0

            dados_json = {}
            for dado in result:
                dados_json.update({
                    dado[0]: {
                        "id": dado[0],
                        "descricaocategoria": dado[1]
                    }
                })
            return dados_json
        except Exception as e:
            return e

    def listarCategoriaPorId(self, id: int) -> int | dict | Exception:
        cursor = self.conexao.cursor()
        try:
            query_sql = f"SELECT * FROM categoria WHERE id = {id}"
            cursor.execute(query_sql)
            result = cursor.fetchall()

            if len(result) == 0:
                return 0

            dados_json = {}
            for dado in result:
                dados_json.update({
                    "id": dado[0],
                    "descricaocategoria": dado[1]
                })
            return dados_json
        except Exception as e:
            return e

    def atualizarCategoria(self, dados: str, id: int) -> int | Exception:
        cursor = self.conexao.cursor()
        try:
            query_sql = f"UPDATE categoria SET {dados} WHERE id = {id}"
            cursor.execute(query_sql)
            self.conexao.commit()

            if cursor.rowcount < 1:
                return 0
            
            return cursor.rowcount
        except Exception as e:
            return e

    def deletarCategoria(self, id: int) -> int | Exception:
        cursor = self.conexao.cursor()
        try:
            query_sql = f"DELETE categoria WHERE id = {id}"
            cursor.execute(query_sql)
            self.conexao.commit()

            if cursor.rowcount < 1:
                return 0

            return cursor.rowcount
        except Exception as e:
            return e


