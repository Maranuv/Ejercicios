numero_cajas =int(input("Número de cajas a vender: "))
id_producto = int(input("Id del producto: "))

productos = [[1, "Maíz grano", 285.55],[2, "Pepino", 334.72],[3, "Tomate Verde", 129.00]]

for producto in productos:
 if producto [0] == id_producto:
   print(f'El producto es: {producto[1]}')
   print(f'El precio por caja es de: {producto[2]}')
   subtotal = producto[2] * numero_cajas
   if numero_cajas <= 100:
     subtotal += 1500

   print(f'El total a pagar: {round(subtotal, 2)}')