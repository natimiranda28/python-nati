"""# Refactorizar el código usando elif, con el fin quitar anidaciones innecesarias.
edad = int(input("Ingresa la edad:"))

if edad < 0:
    mensaje = "edad no válida"
else:
    if edad >= 18:
        mensaje = "eres mayor de edad"
    else:
        mensaje = "eres menor de edad"

print(mensaje)
"""

edad = int(input("Ingresa la edad:"))

if edad < 0:
    mensaje = "edad no válida"
elif edad >= 18:
        mensaje = "eres mayor de edad"
else:
        mensaje = "eres menor de edad"

print(mensaje)