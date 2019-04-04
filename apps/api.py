from flask_restful import Api, Resource

api = Api()

class Index(Resource):
    def get(self):
       return {
           'Eai': 'Abestado'
       }

def configure_api(app):
    api.add_resource(Index, '/')

    api.init_app(app)


