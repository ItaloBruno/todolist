from flask import Flask

app = Flask(__name__)

@app.route("/v1/")
def home():
	return "Rota raiz da nossa API"
