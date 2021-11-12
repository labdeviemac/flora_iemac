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
            # Insira o par "chave: valor" para cada chave,
            # valor nos itens do dicion_args se o valor nao for nulo
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
