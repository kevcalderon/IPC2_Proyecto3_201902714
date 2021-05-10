from django.shortcuts import render
from xml.dom import minidom
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse
import sys
from . import controlador
import json
import requests

# from web.controladorxml import readxml


rutaAbs = ""
def filtroFecha(request):
    fecha = {}
    
    if request.method == 'GET':
        listfechas = []
        direccion = "http://127.0.0.1:5000/mostrar"
        response = requests.get(direccion)
        data = response.json()
        obj = json.loads(data)
        
        for estadistica in obj:
            try:
                for x in range(0,100):
                    key = obj[estadistica]['ESTADISTICA'][x]['FECHA']
                    print(key)
                    listfechas.append(key)
            except IndexError:
                pass
        fecha['fecha'] = listfechas
    
    return render(request, 'fecha.html', context={"fecha": fecha})


def filtroCodigo(request):
    codigo = {}
    if request.method == 'GET':
        listcodigo = []
        direccion = "http://127.0.0.1:5000/mostrarCodigo"
        response = requests.get(direccion)
        data = response.json()
        
        # print(data)
        for x in data['codigo']:
            listcodigo.append(x)

        codigo['codigo'] = listcodigo

    return render(request, 'codigo.html', codigo)



# Create your views here.
def index(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        ruta = uploaded_file.name
        fs =  FileSystemStorage()
        name = fs.save(ruta, uploaded_file)
        
        # obtengo la ruta 
        rutaAbs = "C:\\Users\\compu\\Desktop\\IPC2 - 2.0\\PROYECTO3\\Frontend\\media\\"
        rutaAbs = rutaAbs + ruta
        
        textArea = ""
        with open(rutaAbs, 'r', encoding='utf-8') as f:
            lineas = f.readlines()
            posicion = 1
            # print(lineas)
            for file in lineas:
                file.rstrip('\n')
                textArea = textArea + file
                # print(file)
        context['url'] = textArea       
        print(rutaAbs)

        controlador.xmlToJson(rutaAbs)


    return render(request, 'index.html', context)


def enviar(request):
    if request.method == "POST":
        url = 'http://127.0.0.1:5000/enviar'
        ruta = "C:\\Users\\compu\\Desktop\\IPC2 - 2.0\\PROYECTO3\\Frontend\\media\\data.json"
        # data = json.loads(ruta)
        with open(ruta, 'r') as j:
            contents = json.loads(j.read())
            # print(contents)
        response = requests.post(url, json=contents)
        print("Informacion enviada al api :D")
        return render(request, 'index.html')


def documentacion(request):
    url = "C:\\Users\\compu\\Desktop\\IPC2 - 2.0\\PROYECTO3\\Documentacion\\documentacionProyecto3.pdf"
    response = FileResponse(open(url, 'rb'), content_type='application/pdf')
    return response


def consulta(request):
    context1 = {}
    if request.method == "GET":
        url = ruta = "C:\\Users\\compu\\Desktop\\IPC2 - 2.0\\PROYECTO3\\Frontend\\media\\estadistica.xml"
        textAreaEstadistica = ""
        with open(url, 'r', encoding='utf-8') as f:
            lineas = f.readlines()

            for file in lineas:
                textAreaEstadistica = textAreaEstadistica + file    
            print(textAreaEstadistica)
        context1['url2'] = textAreaEstadistica

    return render(request, 'index.html', context1)  