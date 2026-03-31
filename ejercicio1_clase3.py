"""Ejercicio:

Crear un programa que muestre 3 postres como menú.
El usuario debe escribir uno.
Si el nombre coincide con el menú, imprimir "Pedido recibido: <tal cosa>",
de lo contrario, imprimir "<tal cosa> no está en el menú"

PARTE DOS:


1. Poner precio a cada producto y que se muestre en el menú.  
2. Crear una billetera con saldo inicial (se puede usar `input`).  
3. Al finalizar, mostrar el saldo final de la billetera.  
4. Si el usuario elige un producto, restar el precio del producto al saldo inicial.  
5. Si no tengo dinero suficiente, imprimir un mensaje.  
6. Si se pudo realizar la compra, también, otro mensaje.  

"""

menu = ["pastel", "helado", "flan"]
print("Menu:")
print("1. Pastel")
print("2. Helado")
print("3. Flan")

eleccion = input("Ingrese un postre del menu")
if eleccion == 1:
    print("Pedido recibido: Pastel")
elif eleccion == 2:
    print("Pedido recibido: Helado")    
elif eleccion == 3:    print("Pedido recibido: Flan")
else:    print(f"{eleccion} no está en el menú")

 
#PARTE DOS
precios = {"pastel": 10, "helado": 5, "flan": 7}
saldo = float(input("Ingrese el saldo inicial de su billetera: "))
eleccion = input("Ingrese un postre del menu")
if eleccion in precios:
    precio = precios[eleccion]
    if saldo >= precio:
        saldo -= precio
        print(f"Pedido recibido: {eleccion}. Saldo restante: {saldo}")
    else:
        print("No tienes suficiente dinero para comprar este postre.")      
else:    print(f"{eleccion} no está en el menú")



