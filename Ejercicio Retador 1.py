poblacion_h = 1494815
poblacion_m = 1532128
superficie = "57365 km2"
temperatura = 25.45
clima = "cálido, subhúmedo, seco y semiseco."
culiacan = 0.3315
mazatlan = 0.1657

poblacion_total = (poblacion_h + poblacion_m)
poblacion_cadena = str(poblacion_total)
print ("La población total es de: " + poblacion_cadena + " habitantes.")
poblacion_culiacan = round((poblacion_total * culiacan))

poblacion_culiacan_cadena = str (poblacion_culiacan)
print ("La población total de Culiacan es de: " + poblacion_culiacan_cadena + " habitantes.")

poblacion_mazatlan = round((poblacion_total * mazatlan))
poblacion_mazatlan_cadena = str(poblacion_mazatlan)
print ("La población total de Mazatlan es de: " + poblacion_mazatlan_cadena + " habitantes.")
temperatura_cadena = str (temperatura)
print ("La temperatura anual de Sinaloa es de: " + temperatura_cadena + " grados y sus tipos de clima son los siguientes: " + clima)