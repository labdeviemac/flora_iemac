from flask import jsonify
from ast import literal_eval
from flask_restful import Resource, reqparse
from services.Flores import Flores


class FloresUpdatePatchRoute(Resource):

    def patch(self, id: int):
        try:
            parametros = reqparse.RequestParser()
            parametros.add_argument('descricao', type=str, required=False)
            parametros.add_argument('quantidade', type=int, required=False)
            parametros.add_argument('valor_unit', type=float, required=False)
            parametros.add_argument('valor_buque', type=float, required=False)
            parametros.add_argument('especie', type=int, required=False)
            parametros.add_argument('categoria', type=int, required=False)

            args = parametros.parse_args()
            dicion_args = dict(args)
            values = {chave: valor for chave, valor in dicion_args.items() if valor is not None}

            string_dados = ''
            for chave, valor in values.items():
                string_dados += f"{chave} = '{valor}', "

            flores = Flores()
            resultado_update = flores.atualizarFlores(string_dados, id)

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


class FloresInsertRoute(Resource):

    def post(self):
        try:
            parametros = reqparse.RequestParser()
            parametros.add_argument('descricao', type=str, required=False)
            parametros.add_argument('quantidade', type=int, required=False)
            parametros.add_argument('valor_unit', type=float, required=False)
            parametros.add_argument('valor_buque', type=float, required=False)
            parametros.add_argument('especie', type=int, required=False)
            parametros.add_argument('categoria', type=int, required=False)

            args = parametros.parse_args()
            dados = (args["descricao"], args["quantidade"], args["valor_unit"], args["valor_buque"],
                     args["especie"], args["categoria"])

            flores = Flores()
            resultado_insert = flores.inserirFlores(dados)

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


class FloresListRoute(Resource):

    def get(self):
        try:
            flores = Flores()
            resultset = flores.listarFlores()

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


class FloresListByIdRoute(Resource):

    def get(self, id):
        try:
            flores = Flores()
            resultset = flores.listarFloresPorId(id)

            if resultset == 0:
                return {
                           "sucesso": False,
                           "mensagem": "Flor não encontrada"
                       }, 404

            return jsonify(literal_eval(resultset))
        except Exception as e:
            return {
                       "sucesso": False,
                       "mensagem": "Erro de servidor interno. Contate o admin para mais detalhes",
                       "detalhes_erro": e
                   }, 500


class FloresUpdateRoute(Resource):

    def put(self, id):
        try:
            parametros = reqparse.RequestParser()
            parametros.add_argument('descricao', type=str, required=False)
            parametros.add_argument('quantidade', type=int, required=False)
            parametros.add_argument('valor_unit', type=float, required=False)
            parametros.add_argument('valor_buque', type=float, required=False)
            parametros.add_argument('especie', type=int, required=False)
            parametros.add_argument('categoria', type=int, required=False)

            argumentos = parametros.parse_args()
            valores = f"descricao = '{argumentos['descricao']}', quantidade = {argumentos['quantidade']}, " \
                      f"valor_unit = {argumentos['valor_unit']}, valor_buque = {argumentos['valor_buque']}," \
                      f"especie = {argumentos['especie']}, categoria = {argumentos['categoria']}"

            flores = Flores()
            resultado_update = flores.atualizarFlores(valores, id)

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
