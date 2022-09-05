from flask import Flask, render_template

app = Flask(__name__)


#funçao

@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/registrar")
def sobre():
    return render_template("registrar.html")

#Site no ar
if __name__ == "__main__":
    app.run(debug=True)

