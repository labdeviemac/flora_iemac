from flask import jsonify
from ast import literal_eval
from flask_restful import Resource, reqparse
from services.Especies import Especie


class EspeciesUpdatePatchRoute(Resource):

    def patch(self, id: int):
        try:
            parametros = reqparse.RequestParser()
            parametros.add_argument('especie', type=str, required=False)
            parametros.add_argument('tipo_adubo', type=str, required=False)
            parametros.add_argument('tempo_vida', type=int, required=False)
            parametros.add_argument('intervalo_agua', type=int, required=False)
            parametros.add_argument('observacoes_especie', type=str, required=False)
            parametros.add_argument('fornecedor', type=int, required=False)

            args = parametros.parse_args()
            dicion_args = dict(args)
            values = {chave: valor for chave, valor in dicion_args.items() if valor is not None}

            string_dados = ''
            for chave, valor in values.items():
                string_dados += f"{chave} = '{valor}', "

            especie = Especie()
            resultado_update = especie.atualizarEspecie(string_dados, id)

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


class EspeciesInsertRoute(Resource):

    def post(self):
        try:
            parametros = reqparse.RequestParser()
            parametros.add_argument('especie', type=str, required=True)
            parametros.add_argument('tipo_adubo', type=str, required=True)
            parametros.add_argument('tempo_vida', type=int, required=True)
            parametros.add_argument('intervalo_agua', type=int, required=True)
            parametros.add_argument('observacoes_especie', type=str, required=True)
            parametros.add_argument('fornecedor', type=int, required=True)

            args = parametros.parse_args()
            dados = (args["especie"], args["tipo_adubo"], args["tempo_vida"], args["intervalo_agua"],
                     args["observacoes_especie"], args["fornecedor"])

            especie = Especie()
            resultado_insert = especie.inserirEspecie(dados)

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


class EspecieListRoute(Resource):

    def get(self):
        try:
            especie = Especie()
            resultset = especie.listarEspecies()

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


class EspecieListByIdRoute(Resource):

    def get(self, id):
        try:
            especie = Especie()
            resultset = especie.listarEspeciePorId(id)

            if resultset == 0:
                return {
                           "sucesso": False,
                           "mensagem": "Espécie não encontrada"
                       }, 404

            return jsonify(literal_eval(resultset))
        except Exception as e:
            return {
                       "sucesso": False,
                       "mensagem": "Erro de servidor interno. Contate o admin para mais detalhes",
                       "detalhes_erro": e
                   }, 500


class EspecieUpdateRoute(Resource):

    def put(self, id):
        try:
            parametros = reqparse.RequestParser()
            parametros.add_argument('especie', type=str, required=False)
            parametros.add_argument('tipo_adubo', type=str, required=False)
            parametros.add_argument('tempo_vida', type=int, required=False)
            parametros.add_argument('intervalo_agua', type=int, required=False)
            parametros.add_argument('observacoes_especie', type=str, required=False)
            parametros.add_argument('fornecedor', type=int, required=False)

            argumentos = parametros.parse_args()
            valores = f"especie = '{argumentos['especie']}', tipo_adubo = '{argumentos['tipo_adubo']}', " \
                      f"tempo_vida = {argumentos['tempo_vida']}, intervalo_agua = {argumentos['intervalo_agua']}," \
                      f"observacoes_especie = '{argumentos['observacoes_especie']}', " \
                      f"fornecedor = {argumentos['fornecedor']}"

            especie = Especie()
            resultado_update = especie.atualizarEspecie(valores, id)

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


class EspecieDeleteRoute(Resource):

    def delete(self, id: int):
        try:
            especie = Especie()
            resultado_delete = especie.deletarEspecie(id)

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
                   }, 500
