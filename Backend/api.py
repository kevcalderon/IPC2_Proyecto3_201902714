from flask import Flask, jsonify, request, Response
from flask_cors import CORS
import json
import xml.etree.cElementTree as ET
from xml.dom import minidom
from controladorApi import createEstadisticaXML
from Afectado import Afectado
from Evento import Evento
import xmltodict


listaEventos = list()


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
        listaAfectados = list()
        for event in params['evento']:
            fecha = event['fecha']
            usuario = event['usuario']
            for i in event['afectados']:
                
                listaAfectados.append(Afectado(i))
            codigo = event['codigo']
            descripcion = event['descripcion']
            evento = Evento(fecha, usuario, listaAfectados, codigo, descripcion)
            listaEventos.append(evento)
            listaAfectados = []

        # y = 0
        # for i in listaEventos:
        #     print("fecha ", i.fecha)
        #     print("nombre ", i.usuario)
        #     for x  in listaEventos[y].afectado:
        #         print("afectado", x.correo)
        #     print("codigo ", i.codigo)
        #     print("descripcion ", i.descripcionCodigo)
        #     print("")
        #     y += 1
        createEstadisticaXML(listaEventos)
   

        return jsonify({"status": 200, "mensaje": "Se guardo con exito los eventos."})

        
        
@app.route('/mostrar', methods=['GET'])
def filtroFecha():
    if request.method == 'GET':       
        ruta = "C:\\Users\\compu\\Desktop\\IPC2 - 2.0\\PROYECTO3\\Frontend\\media\\estadistica.xml"
        with open(ruta, 'r') as myfile:
            obj = xmltodict.parse(myfile.read())
            # print(json.dumps(obj))

        
        return jsonify(json.dumps(obj))
            

if __name__ == '__main__':
    app.run(debug=True, port=5000)