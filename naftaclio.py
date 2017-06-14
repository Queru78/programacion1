#!/usr/bin/python
#calcular de nafta para clio (localidad las flores)

km = input ("ingrese la cantidad de kilometros a destino: ")
nafta = (km*6.0/100)

print (("cantidad de litros a destino: %s litros ") %(nafta))
gasto = (nafta*22)

print (("haciendo %s kilometros el clio gasta mas o menos: %s pesos ") % (km, gasto))

