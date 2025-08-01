N= int(input("¿cuantas lecturas va a ingresar?"))
contador = 0
suma = 0
while contador < N:
    lectura = float(input("ingrese su valor de glucosa (mg/dL): "))
    suma = suma + lectura
    contador = contador + 1

promedio = suma / N
if promedio > 180:
    print("hiperglucemia")
elif promedio >= 70 and promedio <= 180:
    print("normal")
elif promedio < 70:
    print ("hipoglucemia")

    print("El promedio fue:", promedio)