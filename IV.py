dosis = float(input("Ingrese la dosis prescrita (mg/h): "))
concentracion = float(input("Ingrese la concentración (mg/mL): "))

velocidad = dosis / concentracion

print("Velocidad de infusión:", velocidad, "mL/h")

if velocidad > 50:
    print("pide atención")
else:
    print("continuar")