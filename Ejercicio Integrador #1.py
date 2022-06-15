productos = [[1, "Maíz grano",285.55],[2,"Pepino",334.72],[3,"Tomate Verde", 129.00]]

venta_productos = [
[2, 122],
[1, 89],
[1, 22],
[3, 48],
[1, 75],
[3, 322],
[2, 95],
[1, 148],
[1, 83],
[3, 100]
]

numero_cajas = int(input("Número de cajas a vender: "))
id_producto = int(input("ID del producto: "))

for producto in productos:
  if producto[0] == id_producto:
    venta_productos.append([id_producto, numero_cajas])
    print(f'El producto es: {producto[1]}')
    print(f'El precio por caja es: {producto[2]}')
    total = producto[2] * numero_cajas
    if numero_cajas <= 100:
      total += 1500
    total_cajas_vendidas = 0
    for venta in venta_productos:
      if venta[0] == id_producto:
        total_cajas_vendidas += venta[1]
        
    if total_cajas_vendidas > 1500:
      total *= 0.8

    print(f'Cajas vendidas durante el día del producto seleccionado: {total_cajas_vendidas}')
    print(f'Aplica descuento del 20%: {total_cajas_vendidas > 1500}')
    print(f'El total a pagar es: {round(total, 2)}')