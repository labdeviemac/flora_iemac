from flask import jsonify
from flask_restful import Resource, abort, reqparse
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
