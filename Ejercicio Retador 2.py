municipio1 = input("Ingrese el primer municipio: ")
print("Ya quedó registrado")
municipio2 = input("Ingrese el segundo municipio: ")
print("Ya quedó registrado")
municipio3 = input("Ingrese el tercer municipio: ")
print("Ya quedó registrado")
municipios = [municipio1, municipio2, municipio3]
print (municipios)

habitantes1 = int(input("Ingrese el número de habitantes de " + municipio1 + ": "))
habitantes2 = int(input("Ingrese el número de habitantes de " + municipio2 + ": "))
habitantes3 = int(input("Ingrese el número de habitantes de " + municipio3 + ": "))
habitantes = [habitantes1, habitantes2, habitantes3]
print(habitantes)

total_habitantes = (habitantes1 + habitantes2 + habitantes3)
print ("El total de habitantes en los 3 municipios es de: " +str(total_habitantes)+ " habitantes.")
total_de_municipios = len(municipios)
promedio_habitantes = int((total_habitantes/total_de_municipios))
print ("El promedio de habitantes por municipio es de: " +str(promedio_habitantes)+ " habitantes.")