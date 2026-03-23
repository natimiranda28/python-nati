"""
Solicitar al usuario la cantidad de stock que comprará.
Mostrar en la terminal el nombre del artículo, el precio unitario, y el precio final.
"""

nombre_articulo = "chocolate"
precio_unitario = 2000
stock = 100;
print(f"Va a comprar {nombre_articulo} a un precio unitario de {precio_unitario} pesos, y el stock disponible es de {stock} unidades")

cantidad_a_comprar = int(input("Ingrese la cantidad de stock que desea comprar: "))
pago = cantidad_a_comprar * precio_unitario
print (f"El monto a pagar por {cantidad_a_comprar} es {pago}" )
stock = stock - cantidad_a_comprar
print (f"El stock disponible de {nombre_articulo} es de {stock} unidades")


