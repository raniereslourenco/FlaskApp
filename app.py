from flask import Flask

#__name__ = "__main__"
app = Flask(__name__)

# criar uma rota - "Hello World!"
@app.route("/")

#o que vai ser executado na rota
def hello():
    return "Hello World!"

@app.route("/about")
def about():
    return "Pagina Sobre"

#rodar o programa
if __name__ == "__main__": #desenvolvimento local
    app.run(debug=True)