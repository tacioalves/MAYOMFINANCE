from urllib import request
from flask import Flask, render_template
from flask.globals import request
from conexao import insereUsuario

app = Flask(__name__)


#funçao mostra tela login
@app.route("/")
def login():
    return render_template("login.html")

#Função que mostra tela de registro
@app.route("/registrar")
def registrar():
    return render_template("registrar.html")

#Função que registra usuario
@app.route("/registraUsuario", methods=["POST","GET"])
def registraUsuario():
    usuario = request.form["usuario"]
    email = request.form["email"]
    senha = request.form["senha"]
    insereUsuario(usuario,email,senha)
    return render_template("login.html")

#Site no ar
if __name__ == "__main__":
    app.run(debug=True)

