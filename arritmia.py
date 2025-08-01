M=int(input("¡cuantos valores de frecuencia cardiaca va a ingresar?"))
fuera_de_rango = 0
contador = 0
while contador < M:
     frecuencia = int(input("Ingrese frecuencia cardíaca (ppm): "))
     if frecuencia < 60 or frecuencia > 100:
        fuera_de_rango = fuera_de_rango + 1

        contador = contador + 1

if fuera_de_rango > 3:
    print("potencial arritmia")
else:
    print("ritmico")