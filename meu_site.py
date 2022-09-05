from flask import Flask, render_template

app = Flask(__name__)


#funçao

@app.route("/")
def login():
    return render_template("login.html")


@app.route("/registrar")
def registrar():
    return render_template("registrar.html")

#Site no ar
if __name__ == "__main__":
    app.run(debug=True)

