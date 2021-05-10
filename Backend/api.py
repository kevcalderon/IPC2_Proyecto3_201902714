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
            


@app.route('/mostrarCodigo', methods=['GET'])
def datosCodigo():
    if request.method == 'GET':
        dataCode = {}
        dataCode['codigo'] = []
        temp = list()
        ruta = "C:\\Users\\compu\\Desktop\\IPC2 - 2.0\\PROYECTO3\\Frontend\\media\\estadistica.xml"
        archivo = minidom.parse(ruta)

        estadistica = archivo.getElementsByTagName('ESTADISTICA')

        for x in estadistica:
            errores = archivo.getElementsByTagName("ERRORES")
            for y in errores:
                error = archivo.getElementsByTagName('ERROR')
                posicion = 0
                for w in error:
                    etiquetacodigo = archivo.getElementsByTagName('CODIGO')
                    codigo = etiquetacodigo[posicion].firstChild.nodeValue
                    if len(temp) == 0:
                        temp.append(codigo)
                    else:
                        if codigo in temp:
                            continue
                        else:
                            temp.append(codigo)
                    # print(columna)
                    posicion += 1
        

        dataCode['codigo'] = temp
        return jsonify(dataCode)



@app.route('/graficaCodigos', methods=['GET'])
def datosGraficaCodigo():
    if request.method == 'GET':
        dataEstadistica = {}
        dataCodigos = []
        dataEstadistica['estadistica'] = []
        # dataCodigos['codigos'] = []
        temp = list()
        ruta = "C:\\Users\\compu\\Desktop\\IPC2 - 2.0\\PROYECTO3\\Frontend\\media\\estadistica.xml"
        archivo = minidom.parse(ruta)
        estadistica = archivo.getElementsByTagName('ESTADISTICA')

        for x in estadistica:
            etiquetafecha = x.getElementsByTagName("FECHA")
            fecha = etiquetafecha[0].firstChild.nodeValue
            # print(fecha)

            errores = x.getElementsByTagName("ERROR")
            for y in errores:
                etiquetacodigo = y.getElementsByTagName("CODIGO")
                codigo = etiquetacodigo[0].firstChild.nodeValue
                etiquetaCantidad = y.getElementsByTagName("CANTIDAD_MENSAJES")
                cantidad = etiquetaCantidad[0].firstChild.nodeValue
                # print(codigo)
                # print(cantidad)

                dataCodigos.append({
                    'codigo' : codigo,
                    'cantidad' : cantidad
                })
            
            
            dataEstadistica['estadistica'].append({
                'fecha' : fecha,
                'codigos' : dataCodigos
            })


            dataCodigos = []


           
        return jsonify(dataEstadistica)

if __name__ == '__main__':
    app.run(debug=True, port=5000)