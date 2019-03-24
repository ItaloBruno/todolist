# Importando Bibliotecas
from flask import Flask
from flask_restful import Resource, Api

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
