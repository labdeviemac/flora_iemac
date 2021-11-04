from flask import Flask
from flask_restful import Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
cors = CORS(app)


if __name__ == "__main__":
    app.run(port=3000, debug=True)
