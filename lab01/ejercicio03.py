import requests

def primer_punto():
    # Llamado a una API pública
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    usuarios = response.json()
    # Procesamiento imperativo
    nombres = []
    for u in usuarios:
        nombres.append(u["name"])

    print("Usuarios encontrados:")
    for n in nombres:
        print("-", n)
    
    #a.
    palabra = "biz"
    correos_filtrados = []

    for u in usuarios:
        if palabra in u["email"]:
            correos_filtrados.append(u["email"])

    print("Correos filtrados:")
    for c in correos_filtrados:
        print("-", c)

def segundo_punto():
    # Entrada de datos
    nombre_pokemon = input("Ingrese el nombre de un Pokémon: ").lower()

    # Llamado a la API
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}"
    respuesta = requests.get(url)

    # Verificación del estado de la respuesta
    if respuesta.status_code == 200:
        datos = respuesta.json()

        # Modelado del estado del Pokémon
        pokemon = {
            "nombre": datos["name"],
            "altura": datos["height"],
            "peso": datos["weight"],
            "tipos": [t["type"]["name"] for t in datos["types"]],
            "habilidades": [h["ability"]["name"] for h in datos["abilities"]]
        }

        # Salida del estado actual
        print("\n📘 Información del Pokémon")
        print(f"Nombre: {pokemon['nombre'].capitalize()}")
        print(f"Altura: {pokemon['altura']}")
        print(f"Peso: {pokemon['peso']}")
        print(f"Tipos: {', '.join(pokemon['tipos'])}")
        print(f"Habilidades: {', '.join(pokemon['habilidades'])}")

        #1.
        #a.
        if len(pokemon["tipos"]) > 1:
            print("Pokémon de tipo mixto")
        
        #b.
        if pokemon["peso"] > 100:
            print("Pokémon de gran tamaño")
        else:
            print("Pokémon ligero")

        #2.
        for i in pokemon["habilidades"]:
            print(i)

        #3. decir si un pokemon cuenta con tipos de pokemon iniciales (fuego, agua o planta)
        tipos = ["fire", "water", "grass"]
        for i in pokemon["tipos"]:
            if i in tipos:
                print("Pokémon de tipo inicial")
    else:
        print("Pokémon no encontrado. Verifique el nombre ingresado.")


def main():
    print("1. Primer punto")
    print("2. Segundo punto")
    print("3. Salir")
    punto = int(input("punto a revisar: "))
    while punto != 3:
        match punto:
            case 1:
                primer_punto()
                punto = int(input("punto a revisar: "))
            case 2: 
                segundo_punto()
                punto = int(input("punto a revisar: "))
            case _:
                print("numero invalido, elija otro")
                punto = int(input("punto a revisar: "))
main()
