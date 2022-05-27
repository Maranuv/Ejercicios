print ("Buenas tardes, a continuación ingrese los valores (cantidad) de su pedido de costales, Gracias.")
peso_cemento = 40
peso_yeso = 30
capacidad_camion = 3254
cemento =int(input("¿Cuántos costales de Cemento va a querer? "))
yeso = int(input("¿Cuántos costales de Yeso va a querer? "))

pedido_cemento = cemento*peso_cemento
pedido_yeso = yeso*peso_yeso
pedido_total = pedido_cemento + pedido_yeso
print("El peso del pedido en kg es: " + str(pedido_total))

print(f"¿Se puede realizar el envío?: {pedido_total > capacidad_camion*0.5 and pedido_total < capacidad_camion}")