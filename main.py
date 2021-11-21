from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from routes.RoutesFlores import *
from routes.RoutesEspecies import *
from routes.RoutesFornecedor import *
from routes.RoutesCategoria import *

app = Flask(__name__)
api = Api(app)
cors = CORS(app)

api.add_resource(CategoriaListRoute, "/categorias")  # GET
api.add_resource(CategoriaInsertRoute, "/categorias")  # POST
api.add_resource(CategoriaListByIdRoute, "/categorias/<int:id>")  # GET
api.add_resource(CategoriaUpdateRoute, "/categorias/<int:id>")  # PUT
api.add_resource(CategoriaDeleteRoute, "/categorias/<int:id>")  # DELETE

api.add_resource(EspecieListRoute, "/especies")  # GET
api.add_resource(EspeciesInsertRoute, "/especies")  # POST
api.add_resource(EspecieListByIdRoute, "/especies/<int:id>")  # GET
api.add_resource(EspecieUpdateRoute, "/especies/<int:id>")  # PUT
api.add_resource(EspeciesUpdatePatchRoute, "/especies/<int:id>")  # PATCH
api.add_resource(EspecieDeleteRoute, "/especies/<int:id>")  # DELETE

api.add_resource(FloresListRoute, "/flores")  # GET
api.add_resource(FloresInsertRoute, "/flores")  # POST
api.add_resource(FloresListByIdRoute, "/flores/<int:id>")  # GET
api.add_resource(FloresUpdateRoute, "/flores/<int:id>")  # PUT
api.add_resource(FloresUpdatePatchRoute, "/flores/<int:id>")  # PATCH

api.add_resource(FornecedorListRoute, "/fornecedores")  # GET
api.add_resource(FornecedorInsertRoute, "/fornecedores")  # POST
api.add_resource(FornecedorListByIdRoute, "/fornecedores/<int:id>")  # GET
api.add_resource(FornecedorUpdateRoute, "/fornecedores/<int:id>")  # PUT
api.add_resource(FornecedorUpdatePatchRoute, "/fornecedores/<int:id>")  # PATCH

if __name__ == "__main__":
    app.run(port=3000, debug=True)
