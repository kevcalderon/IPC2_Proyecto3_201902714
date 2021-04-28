from flask import Flask, jsonify, request, Response
from flask_cors import CORS
import json
import xml.etree.cElementTree as ET

from Afectado import Afectado
from Evento import Evento



listaEventos = list()
listaUsuarios = list()

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def index():
    return '<h1>hola mundo</h1>'


@app.route('/enviar', methods=['POST'])
def agregarEvento():
    if request.method == 'POST':
        params=request.get_json()
        
        # guarda los eventos en la lista, por medio del json enviado desde el api.
        # data2.json, es el que se esta usando para utilizar la api
        
        for event in params['evento']:
            print('fecha:', event['fecha'])
            print('usuario:', event['usuario'])

        return jsonify({"status": 200, "mensaje": "Se guardo con exito los eventos."})
   

if __name__ == '__main__':
    app.run(debug=True, port=5000)