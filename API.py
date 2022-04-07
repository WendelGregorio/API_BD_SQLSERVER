from flask import Flask
from ConBDAPI import Dados
import json

Projetos = Dados() #armazena os dados retornados da função do arquivo ConDB

projsJson = json.dumps(str(Projetos))
response = json.loads(projsJson) #DADOS CONVERTIDOS EM JSON

app = Flask(__name__) 

@app.route('/', methods=['GET']) #ROTA CRIADA COM DECORATOR DA LIB FLASK
def hello():    
    return response #RETORNO AO CLIENT SIDE COM OS DADOS DOS PROJETOS


if __name__ == '__main__':
    app.run()