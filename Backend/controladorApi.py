import json
import xml.etree.cElementTree as ET
from xml.dom import minidom


def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")




def createEstadisticaXML(listaEventos):
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

                afectados = ET.SubElement(estadistica, "AFECTADOS")      
                posicion = 0
                listaTemp2 = []
                for x in listaEventos:
                    if x.fecha == evento.fecha:
                        for y in listaEventos[posicion].afectado:
                            if len(listaTemp2) == 0:
                                afectado = ET.SubElement(afectados, "AFECTADO").text=str(y.correo)
                                listaTemp2.append(y.correo)
                            else:
                                if y.correo in listaTemp2:
                                    continue
                                else:
                                    afectado = ET.SubElement(afectados, "AFECTADO").text=str(y.correo)
                                    listaTemp2.append(y.correo)

                    posicion += 1


                errores = ET.SubElement(estadistica, "ERRORES")
                listaTemp3 = []
                for x in listaEventos:
                    if x.fecha == evento.fecha:
                        cant2 = 0
                        for y in listaEventos:
                            if x.fecha == y.fecha:
                                if x.codigo == y.codigo:
                                    cant2 += 1

                        if len(listaTemp3) == 0:
                            listaTemp3.append(x.codigo)
                            error = ET.SubElement(errores, "ERROR")
                            codigo = ET.SubElement(error, "CODIGO").text=str(x.codigo)
                            cantidad = ET.SubElement(error, "CANTIDAD_MENSAJES").text=str(cant2)             
                        else:
                            if x.codigo in listaTemp3:
                                continue
                            else:
                                listaTemp3.append(x.codigo)
                                error = ET.SubElement(errores, "ERROR")
                                correo = ET.SubElement(errores, "CODIGO").text=str(x.codigo)
                                cantidad = ET.SubElement(errores, "CANTIDAD_MENSAJES").text=str(cant2)
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
                    
    
                    afectados = ET.SubElement(i, "AFECTADOS")      
                    posicion = 0
                    listaTemp3 = []
                    for x in listaEventos:
                        if x.fecha == evento.fecha:
                            for y in listaEventos[posicion].afectado:
                                if len(listaTemp3) == 0:
                                    afectado = ET.SubElement(afectados, "AFECTADO").text=str(y.correo)
                                    listaTemp3.append(y.correo)
                                else:
                                    if y.correo in listaTemp3:
                                        continue
                                    else:
                                        afectado = ET.SubElement(afectados, "AFECTADO").text=str(y.correo)
                                        listaTemp3.append(y.correo)

                        posicion += 1

                    errores = ET.SubElement(i, "ERRORES")
                    listaTemp4 = []
                    for x in listaEventos:
                        if x.fecha == evento.fecha:
                            cant2 = 0
                            for y in listaEventos:
                                if x.fecha == y.fecha:
                                    if x.codigo == y.codigo:
                                        cant2 += 1

                            if len(listaTemp4) == 0:
                                listaTemp4.append(x.codigo)
                                error = ET.SubElement(errores, "ERROR")
                                codigo = ET.SubElement(error, "CODIGO").text=str(x.codigo)
                                cantidad = ET.SubElement(error, "CANTIDAD_MENSAJES").text=str(cant2)             
                            else:
                                if x.codigo in listaTemp4:
                                    continue
                                else:
                                    listaTemp3.append(x.codigo)
                                    error = ET.SubElement(errores, "ERROR")
                                    correo = ET.SubElement(error, "CODIGO").text=str(x.codigo)
                                    cantidad = ET.SubElement(error, "CANTIDAD_MENSAJES").text=str(cant2)

            myData = prettify(root)
            f = open(ruta+'estadistica.xml', 'w')
            f.write(myData)

            