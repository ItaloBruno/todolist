# Importando Bibliotecas
from flask import Flask
from flask_restful import Resource, Api
import os

# Configurações da nossa API
app = Flask(__name__)
api = Api(app)

# Classe que usaremos para responder as requisições
class Hello(Resource):
	def get(self):
		return {
			"Eai" : "Abestado"
		}

# Fazendo associação entre a classe e a rota
api.add_resource(Hello, "/")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)