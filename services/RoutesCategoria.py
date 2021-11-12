from flask import jsonify
from flask_restful import Resource, reqparse
from services.Categoria import Categoria
from ast import literal_eval


class CategoriaInsertRoute(Resource):

    # Método POST - Inserção de Dados das Categorias
    def post(self):
        try:
            parametros = reqparse.RequestParser()
            parametros.add_argument('desccategoria', type=str, required=True,
                                    help="Informe uma descrição para a categoria")

            argumentos = parametros.parse_args()
            dados = (argumentos["desccategoria"])

            categoria = Categoria()
            resultado_insert = categoria.inserirCategoria(dados)

            if resultado_insert == 0:
                return {
                           "sucesso": False,
                           "mensagem": "Erro ao inserir dados"
                       }, 400  # Status HTTP para "Bad Request" - a requisição gerou um erro

            return {
                       "sucesso": True,
                       "mensagem": "Dados inseridos com sucesso!"
                   }, 201  # Status HTTP para "Created" - o valor foi salvo no banco de dados com sucesso!

        except Exception as e:
            return {
                       "sucesso": False,
                       "mensagem": "Erro de servidor interno. Contate o admin para mais detalhes",
                       "detalhes_erro": e
                   }, 500  # Status HTTP para "Internal Server Error" - quando tem erros no código


class CategoriaListRoute(Resource):

    def get(self):
        try:
            categoria = Categoria()
            resultset = categoria.listarCategorias()

            if resultset == 0:
                return {
                           "sucesso": True,
                           "mensagem": "Nenhum dado a ser exibido"
                       }, 200  # Status HTTP para "HTTP OK" - quando a requisição retorna sucesso

            return jsonify(literal_eval(resultset))  # Content-Type: application/json
        except Exception as e:
            return {
                       "sucesso": False,
                       "mensagem": "Erro de servidor interno. Contate o admin para mais detalhes",
                       "detalhes_erro": e
                   }, 500  # Status HTTP para "Internal Server Error" - quando tem erros no código


class CategoriaListByIdRoute(Resource):

    def get(self, id):
        try:
            categoria = Categoria()
            resultset = categoria.listarCategoriaPorId(id)

            if resultset == 0:
                return {
                           "sucesso": False,
                           "mensagem": "Categoria não encontrada"
                       }, 404  # Status HTTP para "Not Found" - quando um recurso não é encontrado

            return jsonify(literal_eval(resultset))
        except Exception as e:
            return {
                       "sucesso": False,
                       "mensagem": "Erro de servidor interno. Contate o admin para mais detalhes",
                       "detalhes_erro": e
                   }, 500  # Status HTTP para "Internal Server Error" - quando tem erros no código


class CategoriaUpdateRoute(Resource):

    def put(self, id):
        try:
            parametros = reqparse.RequestParser()
            parametros.add_argument('desccategoria', type=str, required=True,
                                    help="Informe uma descrição para a categoria")
            argumentos = parametros.parse_args()
            valores = f"descricao_categoria = '{argumentos['desccategoria']}'"

            categoria = Categoria()
            resultado_update = categoria.atualizarCategoria(valores, id)

            if resultado_update == 0:
                return {
                           "sucesso": False,
                           "mensagem": "Erro ao atualizar os dados. Contate o administrador para mais detalhes"
                       }, 400

            return {
                       "sucesso": True,
                       "mensagem": "Atualizado com sucesso!"
                   }, 200
        except Exception as e:
            return {
                       "sucesso": False,
                       "mensagem": "Erro de servidor interno. Contate o admin para mais detalhes",
                       "detalhes_erro": e
                   }, 500  # Status HTTP para "Internal Server Error" - quando tem erros no código


class CategoriaDeleteRoute(Resource):

    def delete(self, id: int):
        try:
            categoria = Categoria()
            resultado_delete = categoria.deletarCategoria(id)

            if resultado_delete == 0:
                return {
                           "sucesso": False,
                           "mensagem": "Erro ao excluir os dados. Contate o administrador para mais detalhes"
                       }, 400

            return {}, 204
        except Exception as e:
            return {
                       "sucesso": False,
                       "mensagem": "Erro de servidor interno. Contate o admin para mais detalhes",
                       "detalhes_erro": e
                   }, 500  # Status HTTP para "Internal Server Error" - quando tem erros no código
