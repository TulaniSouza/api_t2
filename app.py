from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/pague")
def exiba_mensagem():
    return "<h2>pagar as people!</h2>"

# #se o app.py for o arquivo principal da API:
# #EXECUTE O APP.RUN COM O MODO DE DEBUG ATIVADO


def init_db():
    with sqlite3.connect("database.db") as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS LIVROS(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                categoria TEXT NOT NULL,
                autor TEXT NO NULL,
                imagem_url TEXT NOT NULL      
            )
""")


init_db()
@app.route("/doar", methods=["POST"])

def doar():
    dados = request.get_json()
    

if __name__=="__main__":
    app.run(debug=True)
    