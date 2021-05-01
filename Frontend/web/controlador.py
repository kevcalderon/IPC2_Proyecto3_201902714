from xml.dom import minidom
import xml.etree.ElementTree as ET
import xmltodict
import json
import re



def xmlToJson(ruta):
    data = {}
    data['evento'] = []
    afectedList = []
    with open(ruta, 'r', encoding='utf-8') as f:
        lineas = f.readlines()
        posicion = 4

        for file in lineas:
            file.rstrip('\n')
            if posicion == 6:
                file = file.rstrip('\n')
                aux = file.split(',')
                # fecha lista! :D
                fecha = aux[1].replace(" ", "")
            if posicion == 7:
                file = file.rstrip('\n')
                pattern = r"([\w.-]+)@([\w.-]+)(.[\w.]+)"
                aux = file.split(':')
                match = re.search(pattern, aux[1])
                # nombreUsuario lista! :D
                if match:
                    usuario = match.group()
            if posicion == 8:
                file = file.rstrip('\n')
                aux = file.split(':')
                aux2 = aux[1].split(',')
                pattern = r"([\w.-]+)@([\w.-]+)(.[\w.]+)"
                # print("AFECTADOS!!!!!")
                for i in aux2:
                    match = re.search(pattern, i)
                    if match:
                        afectados = match.group()
                        # print(afectados)
                        afectedList.append( afectados
                        )
                # print("")
            if posicion == 9:
                file = file.rstrip('\n')
                aux = file.split(':')
                aux2 =  aux[1].split('-')
                codigo = aux2[0].replace(" ", "")
                descripcion = aux2[1].lstrip()
            if file == '\t</EVENTO>\n' or file == '\t</EVENTO>\n':
                file = file.rstrip('\n')
                # print("fecha: " + fecha)
                # print("usuario: " + usuario)
                # print("afectados:" + afectados)
                # print("codigo: " + codigo)
                # print("descripcion: " + descripcion)
                # print("")
                data['evento'].append({
                    'fecha' : fecha,
                    'usuario' : usuario,
                    'afectados' : afectedList,
                    'codigo' : codigo,
                    'descripcion' : descripcion
                })
                 
                posicion = 4
                afectedList = []
            posicion += 1


    with open('C:\\Users\\compu\\Desktop\\IPC2 - 2.0\\PROYECTO3\\Frontend\\media\\data.json', 'w', encoding='utf-8') as file:
        dataJson = json.dump(data, file, indent=4)
    



    

