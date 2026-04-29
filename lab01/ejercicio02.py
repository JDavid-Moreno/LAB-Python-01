def primer_punto():
    edad = int(input("Ingrese su edad: "))
    tiene_licencia = input("¿Tiene licencia? (s/n): ")
    #a.
    if edad < 18 or tiene_licencia == "no":
        print("no puede conducir")
    
    #b.
    tiene_sancion = input("cuenta con sancion? (y/n): ")
    if tiene_licencia == "si":
        print("no puede conducir")
    
def segundo_punto():
    cont = 0
    for i in range(1, 6):
        print(f"Iteración número {i}")
        #a.
        cont += i
        #b.
        if i % 2 == 0:
            print(i)
        #c.
        print(cont)

def tercer_punto():
    contador = 0
    direccion = 1
    while 0 <= contador < 5:
        print("Contador:", contador)
        #a.
        if contador == 4:
            direccion = -1
        contador += direccion

    #b.
    numero = int(input("ingrese un numero: "))
    while numero != 0:
        numero = int(input("ingrese un numero: "))

def cuarto_punto():
    suma_pares = 0
    suma_impares = 0
    for i in range(1, 11):
        if i % 2 == 0:
            suma_pares += i
        else:
            suma_impares += i

    print("Suma de los pares:", suma_pares)



def main():
    punto = int(input("punto a revisar: "))
    while punto != 6:
        match punto:
            case 1:
                primer_punto()
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