
#!/usr/bin/python
#calcular nafta para clio (localidad las flores)

km = input ("ingrese la cantidad de kilometros a destino: ")
nafta = (km*6.0/100)

print (("cantidad de litros a destino: %s litros ") %(nafta))
gasto = (nafta*22)

print (("haciendo %s kilometros el clio gasta mas o menos: %s pesos ") % (km, gasto))

tiempo = (60*km/100)

if (tiempo) <= 59:

	print (("tiempo estimativo de llegada a destino: %s minutos") % (tiempo))

hora = (tiempo/60.0)

if (hora) >= 1:

	print (("tiempo estimativo de llegada a destino: %s horas") % (hora))

