from flask import jsonify
from flask_restful import Resource, reqparse
from services.Fornecedores import Fornecedores
from ast import literal_eval


class FornecedorUpdatePatchRoute(Resource):

    def patch(self, id: int):
        try:
            parametros = reqparse.RequestParser()
            parametros.add_argument('razao_social', type=str, required=False)
            parametros.add_argument('nome_fantasia', type=str, required=False)
            parametros.add_argument('cnpj', type=str, required=False)
            parametros.add_argument('telefone', type=str, required=False)

            args = parametros.parse_args()
            dicion_args = dict(args)
            values = {chave: valor for chave, valor in dicion_args.items() if valor is not None}

            string_dados = ''
            for chave, valor in values.items():
                string_dados += f"{chave} = '{valor}', "

            fornecedores = Fornecedores()
            resultado_update = fornecedores.atualizarFornecedor(string_dados, id)

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
                   }, 500


class FornecedorInsertRoute(Resource):

    def post(self):
        try:
            parametros = reqparse.RequestParser()
            parametros.add_argument('razao_social', type=str, required=False)
            parametros.add_argument('nome_fantasia', type=str, required=False)
            parametros.add_argument('cnpj', type=str, required=False)
            parametros.add_argument('telefone', type=str, required=False)

            args = parametros.parse_args()
            dados = (args["razao_social"], args["nome_fantasia"], args["cnpj"], args["telefone"])

            fornecedor = Fornecedores()
            resultado_insert = fornecedor.inserirFornecedor(dados)

            if resultado_insert == 0:
                return {
                           "sucesso": False,
                           "mensagem": "Erro ao inserir dados"
                       }, 400

            return {
                       "sucesso": True,
                       "mensagem": "Dados inseridos com sucesso!"
                   }, 201

        except Exception as e:
            return {
                       "sucesso": False,
                       "mensagem": "Erro de servidor interno. Contate o admin para mais detalhes",
                       "detalhes_erro": e
                   }, 500


class FornecedorListRoute(Resource):

    def get(self):
        try:
            fornecedor = Fornecedores()
            resultset = fornecedor.listarFornecedores()

            if resultset == 0:
                return {
                           "sucesso": True,
                           "mensagem": "Nenhum dado a ser exibido"
                       }, 200

            return jsonify(literal_eval(resultset))
        except Exception as e:
            return {
                       "sucesso": False,
                       "mensagem": "Erro de servidor interno. Contate o admin para mais detalhes",
                       "detalhes_erro": e
                   }, 500


class FornecedorListByIdRoute(Resource):

    def get(self, id):
        try:
            fornecedor = Fornecedores()
            resultset = fornecedor.selecionarPorId(id)

            if resultset == 0:
                return {
                           "sucesso": False,
                           "mensagem": "Fornecedor n??o encontrado"
                       }, 404

            return jsonify(literal_eval(resultset))
        except Exception as e:
            return {
                       "sucesso": False,
                       "mensagem": "Erro de servidor interno. Contate o admin para mais detalhes",
                       "detalhes_erro": e
                   }, 500


class FornecedorUpdateRoute(Resource):

    def put(self, id):
        try:
            parametros = reqparse.RequestParser()
            parametros.add_argument('razao_social', type=str, required=False)
            parametros.add_argument('nome_fantasia', type=str, required=False)
            parametros.add_argument('cnpj', type=str, required=False)
            parametros.add_argument('telefone', type=str, required=False)

            argumentos = parametros.parse_args()
            valores = f"razao_social = '{argumentos['razao_social']}', nome_fantasia = '{argumentos['nome_fantasia']}'," \
                      f"cnpj = '{argumentos['cnpj']}', telefone = {argumentos['telefone']}"

            fornecedor = Fornecedores()
            resultado_update = fornecedor.atualizarFornecedor(valores, id)

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
                   }, 500
