#!/usr/bin/python

cantidad_persona = input ("cantidad de personas que viajan: ")

if (cantidad_persona) == 1: 
	print ("viaja en Bicicleta")
elif (cantidad_persona) ==  2:
	print ("viajan en Moto")
elif (cantidad_persona) <=  4:
	print ("viajan en Auto")
elif (cantidad_persona) <=  12:
	print ("viajan en Camioneta")
elif (cantidad_persona) <=  40:
	print ("viajan en Colectivo")
elif (cantidad_persona) <=  200:
	print ("viajan en Avion")
else:
	print ("viajan tal vez en avion")




