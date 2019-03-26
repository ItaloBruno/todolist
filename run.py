#==================================================================================
from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

#==================================================================================
# Configurações da nossa API
app = Flask(__name__)
api = Api(app)

#==================================================================================
# Lista com exemplos de objetos da Classe ToDo
todo_list = {
	'task1': {
		'nome':		'Estruturação da API',
		'descricao':'Montar toda a estrutura básica da nossa API',
		'status':	 True
	},
	'task2': {
		'nome':		'Métodos da classe Task',
		'descricao':'Implementar os seus métodos',
		'status':	 True
	},
	'task3': {
		'nome':		'Métodos da classe TaskList',
		'descricao':'Implementar os seus métodos',
		'status':	 False
	}
}

#==================================================================================
"""
	Esta função verifica se o a Task com o task_id passado como parâmetro existe.
	Se não existir, retorna uma mensagem de erro com o seu respectivo código.
"""
def abort_if_task_doesnt_exist(task_id):
	if task_id not in todo_list:
		abort(404, message="The {} doesn't exits on application".format(task_id))

#==================================================================================
# Realização do parse das informações vindas no corpo da requisição HTTP.
parse = reqparse.RequestParser()
parse.add_argument('nome', 		type=str)
parse.add_argument('descricao', type=str)
parse.add_argument('status', 	type=bool)

#==================================================================================
"""
	Classe responsável por responder as requisições HTTP direcionadas ao objeto Task. 
	Nela foram implementados as seguintes requisições:
		- Get 
		- Put 
		- Delete
"""
class Task(Resource):
	def get(self, task_id):
		abort_if_task_doesnt_exist(task_id) # Verificando se a tarefa existe ou não
		return todo_list[task_id]

	def put(self, task_id):
		abort_if_task_doesnt_exist(task_id) # Verificando se a tarefa existe ou não
		args = parse.parse_args()
		task = {
			'nome':		 args['nome'],
			'descricao': args['descricao'],
			'status':	 args['status']
		}
		todo_list[task_id] = task
		return task, 201

	def delete(self, task_id):
		abort_if_task_doesnt_exist(task_id) # Verificando se a tarefa existe ou não
		del todo_list[task_id]
		return 'Task deleted', 201

#==================================================================================
"""
	Classe responsável por responder as requisições HTTP direcionadas ao objeto TaskList. 
	Nela foram implementados as seguintes requisições:
		- Get 
		- Post
"""
class TaskList(Resource):
	def get(self):
		return todo_list

	def post(self):
		args = parse.parse_args()
		task_id = int(max(todo_list.keys()).lstrip('task')) + 1
		task_id = 'task{}'.format(task_id)
		task = {
			'nome':		 args['nome'],
			'descricao': args['descricao'],
			'status':	 args['status']
		}
		todo_list[task_id] = task
		return todo_list[task_id], 201

#==================================================================================
# Fazendo a associação entre as classes e seus respectivos Endpoints
api.add_resource(Task, 		'/v1/todos/<string:task_id>')
api.add_resource(TaskList, 	'/v1/todos/')

