from flask import Flask, render_template

app = Flask(__name__)


#funçao

@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/sobre")
def sobre():
    return "Primeiro site"

#Site no ar
if __name__ == "__main__":
    app.run(debug=True)