from flask import Flask, jsonify, request, Response
from flask_cors import CORS
import json
import xml.etree.cElementTree as ET
from xml.dom import minidom

from Afectado import Afectado
from Evento import Evento


listaEventos = list()


app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def index():
    return '<h1>hola mundo</h1>'


def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")






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

        ruta = 'C:\\Users\\compu\\Desktop\\IPC2 - 2.0\\PROYECTO3\\Frontend\\media\\'

        root = ET.Element('ESTADISTICAS')
        listaTemp = []
        
        for evento in listaEventos:
            if len(listaTemp) == 0:
                listaTemp.append(evento.fecha)    
                # print("se agrego fecha ", evento.fecha)

                estadistica = ET.SubElement(root, "ESTADISTICA")
                ET.SubElement(estadistica, "FECHA").text=str(evento.fecha)
                count = 0
                for x in listaEventos:
                    if x.fecha == evento.fecha:
                        count += 1
                ET.SubElement(estadistica, "CANTIDAD_MENSAJES").text=str(count)

                reportadoPor = ET.SubElement(estadistica, "REPORTADO_POR")
                listaTemp1 = []
                for x in listaEventos:
                    if x.fecha == evento.fecha:
                        cant = 0
                        for y in listaEventos:
                            if x.fecha == y.fecha:        
                                if x.usuario == y.usuario:
                                    # print(y.usuario)
                                    cant += 1  
                                    # print(cant)
                                    # print("")

                        if len(listaTemp1) == 0:
                            listaTemp1.append(x.usuario)
                            usuario = ET.SubElement(reportadoPor, "USUARIO")
                            correo = ET.SubElement(usuario, "EMAIL").text=str(x.usuario)
                            cantidad = ET.SubElement(usuario, "CANTIDAD_MENSAJES").text=str(cant)
                        else:
                            if x.usuario in listaTemp1:
                                continue
                            else:
                                listaTemp1.append(x.usuario)
                                usuario = ET.SubElement(reportadoPor, "USUARIO")
                                correo = ET.SubElement(usuario, "EMAIL").text=str(x.usuario)
                                cantidad = ET.SubElement(usuario, "CANTIDAD_MENSAJES").text=str(cant)

            else:
                # la lista quiere decir que hay mas de una fecha entonces se hace una busqueda
                # para ver si se encuentra o no
                if evento.fecha in listaTemp:
                    # print("La fecha ya existe! Ya se tomo la informacion de esa fecha")
                    pass
                else:
                    listaTemp.append(evento.fecha)
                    print("se agrego la nueva fecha ", evento.fecha)
                    i = ET.SubElement(root, "ESTADISTICA")
                    ET.SubElement(i, "FECHA").text=str(evento.fecha)
                    count = 0
                    for x in listaEventos:
                        if x.fecha == evento.fecha:
                            count += 1
                    ET.SubElement(i, "CANTIDAD_MENSAJES").text=str(count)

                    reportadoPor = ET.SubElement(i, "REPORTADO_POR")

                    listaTemp1 = []
                    for x in listaEventos:
                        if x.fecha == evento.fecha:
                            cant = 0
                            for y in listaEventos:
                                if x.fecha == y.fecha:        
                                    if x.usuario == y.usuario:
                                        # print(y.usuario)
                                        cant += 1  
                                        # print(cant)
                                        # print("")

                            if len(listaTemp1) == 0:
                                listaTemp1.append(x.usuario)
                                usuario = ET.SubElement(reportadoPor, "USUARIO")
                                correo = ET.SubElement(usuario, "EMAIL").text=str(x.usuario)
                                cantidad = ET.SubElement(usuario, "CANTIDAD_MENSAJES").text=str(cant)
                            else:
                                if x.usuario in listaTemp1:
                                    continue
                                else:
                                    listaTemp1.append(x.usuario)
                                    usuario = ET.SubElement(reportadoPor, "USUARIO")
                                    correo = ET.SubElement(usuario, "EMAIL").text=str(x.usuario)
                                    cantidad = ET.SubElement(usuario, "CANTIDAD_MENSAJES").text=str(cant)
                    
        myData = prettify(root)
        f = open(ruta+'estadistica.xml', 'w')
        f.write(myData)

        return jsonify({"status": 200, "mensaje": "Se guardo con exito los eventos."})

        
        
@app.route('/mostrar', methods=['GET'])
def mostrarEventos():
    if request.method == 'GET':       

        return jsonify({"status": 200, "mensaje": "Se mostro con exito los eventos.."})
            

if __name__ == '__main__':
    app.run(debug=True, port=5000)