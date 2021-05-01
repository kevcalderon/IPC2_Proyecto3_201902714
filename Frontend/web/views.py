from django.shortcuts import render
from xml.dom import minidom
from django.core.files.storage import FileSystemStorage
import sys
from . import controlador
import json
import requests

# from web.controladorxml import readxml


rutaAbs = ""

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


       
