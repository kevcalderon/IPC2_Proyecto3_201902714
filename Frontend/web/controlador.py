def xmlToJson(ruta):
    with open(ruta, 'r', encoding='utf-8') as f:
        lineas = f.readlines()
        posicion = 1
        # print(lineas)
        for file in lineas:
            file.rstrip('\n')
            print(file)