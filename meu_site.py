from urllib import request
from flask import Flask, render_template
from flask.globals import request
from conexao import insereUsuario, loginUsuario

app = Flask(__name__)


#funçao mostra tela login
@app.route("/", methods=["POST","GET"])
def login():
    return render_template("login.html")

#Função que mostra tela de registro
@app.route("/registrar", methods=["POST","GET"])
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

#dashboard

@app.route("/dashboard", methods=["POST","GET"])
def dashboard():
    emailLogin = request.form["usuario"]
    senhaLogin = request.form["senha"]
    validaLogin = loginUsuario(emailLogin,senhaLogin)


    if not validaLogin:
        return render_template('login.html')
        
    else:
        saldoUsuario = validaLogin[4]
        nomeUsuario = validaLogin[2]
        return render_template("dashboard.html", saldo=saldoUsuario, nomeUsuario=nomeUsuario)
        

@app.route("/controlefinanceiro", methods=["POST","GET"])
def controlefinanceiro():
    return render_template("controleFinanceiro.html")


#Site no ar
if __name__ == "__main__":
    app.run(debug=True)

