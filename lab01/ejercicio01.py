import math

# 1)

def primer_punto(saldo):
# Estado inicial
    #saldo = 500_000      Saldo de la cuenta
    deposito = 150_000   # Monto a depositar
    retiro = 80_000      # Monto a retirar

    # Actualización del estado
    saldo = saldo + deposito   # Se deposita dinero
    saldo = saldo - retiro     # Se retira dinero

    # Salida del estado final
    print("Saldo final de la cuenta:", saldo)

    #a. 
    interes = 0.02
    saldo_final = saldo + (saldo * interes)

    #b.
    print(f"Saldo final con intereses: ${saldo_final:.2f}")

def segundo_punto():
    # Lista inicial de temperaturas en °C
    temperaturas = [22.5, 23.0, 21.8, 24.3, 25.1]

    # Operaciones básicas
    print("Temperaturas:", temperaturas)

    #a. 
    temperaturas.append(26)
    #[22.5, 23.0, 21.8, 24.3, 25.1]

    #b.
    temperaturas.pop(0)
    #[22.5, 23.0, 21.8, 24.3, 25.1, 26]
    
    #c.
    temperaturas.insert(1, 22.9)
    #[23.0, 21.8, 24.3, 25.1, 26]
    
    #d.
    temperaturas.sort()
    #[21.8, 22.9, 23.0, 24.3, 25.1, 26]
    
    #e.
    diferencia_temperaturas = max(temperaturas) - min(temperaturas)
    #4.199999999999999

    promedio_temperturas = sum(temperaturas) / len(temperaturas)
    #23.849999999999998

    #f.
    temperaturas.append(23.7)
    posicion_elemento = temperaturas.index(23.7)
    #6

    #g. 
    print(temperaturas[1:4])
    #[22.9, 23.0, 24.3]

    #h.
    print(temperaturas[:3])
    #[21.8, 22.9, 23.0]

def tercer_punto():
    # Lista de productos en una tienda
    inventario = [
        {"nombre": "Pan", "precio": 1500, "stock": 30},
        {"nombre": "Leche", "precio": 3500, "stock": 15},
        {"nombre": "Café", "precio": 8000, "stock": 20},
    ]
    #a.
    print(inventario[0]["nombre"])
    #pan

    #b.
    inventario.append({"nombre": "huevos", "precio": 5000, "stock": 8})
    #[{'nombre': 'Pan', 'precio': 1500, 'stock': 30}, 
    # {'nombre': 'Leche', 'precio': 3500, 'stock': 15}, 
    # {'nombre': 'Café', 'precio': 8000, 'stock': 10}, 
    # {'nombre': 'huevos', 'precio': 5000, 'stock': 8}]

    #c.
    inventario[1]["stock"] = 13
    #[{'nombre': 'Pan', 'precio': 1500, 'stock': 30}, 
    # {'nombre': 'Leche', 'precio': 3500, 'stock': 13}, 
    # {'nombre': 'Café', 'precio': 8000, 'stock': 10}, 
    # {'nombre': 'huevos', 'precio': 5000, 'stock': 8}]

    #d.
    valor_inventario = sum(i["precio"] * i["stock"] for i in inventario)
    #210500
    
    #e.
    for i in inventario:
        if i["stock"] < 10:
            print(i)
    #{'nombre': 'huevos', 'precio': 5000, 'stock': 8}

    #f.
    for i in inventario:
        i["precio"] = i["precio"] + (i["precio"] * 0.1)
    #[{'nombre': 'Pan', 'precio': 1650.0, 'stock': 30}, 
    # {'nombre': 'Leche', 'precio': 3850.0, 'stock': 13}, 
    # {'nombre': 'Café', 'precio': 8800.0, 'stock': 10}, 
    # {'nombre': 'huevos', 'precio': 5500.0, 'stock': 8}]

    #g.

    #h.
    productoExiste = None
    busquedaProducto = input("que producto desea? ")
    for i in inventario:
        if i["nombre"] == busquedaProducto:
            productoExiste = i
            break
    if productoExiste:
        print(i)
    else:
        print("producto no encontrado")
    
    #i.
    for i in inventario:
        if i["stock"] == 0:
            inventario.pop(inventario[i])
    print(inventario)

    #j.
    ordenPrecio = sorted(inventario, key=lambda x: x["stock"])
    #[{'nombre': 'huevos', 'precio': 5500.0, 'stock': 8}, 
    # {'nombre': 'Leche', 'precio': 3850.0, 'stock': 13}, 
    # {'nombre': 'Café', 'precio': 8800.0, 'stock': 20}, 
    # {'nombre': 'Pan', 'precio': 1650.0, 'stock': 30}]

def cuarto_punto():
    # Tupla: coordenadas (x, y)
    punto = (3, 7)
    print("Punto:", punto)

    #a
    rectangulo = (3,4)

    #b.
    area = rectangulo[0] * rectangulo[1]
    perimetro = 2 * (rectangulo[0] + rectangulo[1])

    posiciones = [(0, 0), (1, 2), (3, 4)]

    distancia_PuntoUnoPuntoDos = math.sqrt((posiciones[0][0] - posiciones[1][0])**2 + (posiciones[0][1] - posiciones[1][1])**2)
    disttancia_PuntoDosPuntoTres = math.sqrt((posiciones[1][0] - posiciones[2][0])**2 + (posiciones[1][1] - posiciones[2][1])**2)
    distancia_total = distancia_PuntoUnoPuntoDos + disttancia_PuntoDosPuntoTres
    print(f"distancia entre puntos uno y dos: {distancia_PuntoUnoPuntoDos:.2f}")
    print(f"distancia entre puntos dos y tres: {disttancia_PuntoDosPuntoTres:.2f}")
    print(f"distancia total: {distancia_total:.2f}")

def quinto_punto():
    biblioteca = {
        "libros": [
            {"titulo": "1984", "autor": "George Orwell", "prestado": False},
            {"titulo": "El Principito", "autor": "Antoine de Saint-Exupéry", "prestado": True},
        ],
        "usuarios": ["Ana", "Luis", "María"]
    }
        

def main():
    print("1. Primer punto")
    print("2. Segundo punto")
    print("3. Tercer punto")
    print("4. Cuarto punto")
    print("5. Quinto punto")
    print("6. Salir")
    punto = int(input("punto a revisar: "))
    while punto != 6:
        match punto:
            case 1:
                saldo = float(input("ingrese su saldo: "))
                primer_punto(saldo)
                punto = int(input("punto a revisar: "))
            case 2: 
                segundo_punto()
                punto = int(input("punto a revisar: "))
            case 3:
                tercer_punto()
                punto = int(input("punto a revisar: "))
            case 4:
                cuarto_punto()
                punto = int(input("punto a revisar: "))
            case 5:
                quinto_punto()
                punto = int(input("punto a revisar: "))
                
            case _:
                print("numero invalido, elija otro")
                punto = int(input("punto a revisar: "))

main()