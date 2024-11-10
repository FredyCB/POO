import json

with open("data.json") as archivo:
    objeto = json.loads(archivo.read())

    # Buscar el id 12
    for dic in objeto:
        if dic["id"] == "12":
            print("ID 12:", dic)

    # Buscar el item mas caro
    maximo = 0
    posicion_mas_caro = 0
    for pos, dic in enumerate(objeto):
        # Conocer el precio
        data = dic["data"]

        if data is None:
            continue

        precio = float(data.get("price", data.get("Price", 0)))

        # valor = data.get("price")
        # if valor is None:
        #     valor = data.get("Price", 0)
        # precio = float(valor)

        if precio > maximo:
            maximo = precio
            posicion_mas_caro = pos
    print("El mas caro es:", objeto[posicion_mas_caro])

    # Buscar el item mas antiguo
    anio_minimo = None
    pos_antiguo = 0

    for pos, dic in enumerate(objeto):
        # Conocer el precio
        data = dic["data"]

        if data is None:
            continue

        try:
            year = int(data["year"])
        except (KeyError, TypeError):
            year = None

        if year is None:
            continue

        if anio_minimo is None or anio_minimo > year:
            anio_minimo = year
            pos_antiguo = pos
    print("El item mas antiguo es:", objeto[pos_antiguo])
