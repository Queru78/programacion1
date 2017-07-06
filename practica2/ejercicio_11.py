#!/usr/bin/python

sexo=raw_input ("ingrese sexo:  ")
altura=input ("ingrese altura:  ") 

if ((sexo=="femenino")  and (altura < 145)):
	
	print "petiza"

elif ((sexo == "femenino") and (altura > 145) and (altura <170)):

	print  "normal"

elif ((sexo=="femenino") and (altura >170)):

	print "alta"

elif ((sexo=="masculino") and (altura<160)):

	print "petizo"

elif ((sexo=="masculino") and ((altura>160) and (altura<190))):

	print "normal"

elif ((sexo=="masculino") and (altura>190)):

	print "Alto"
 
else :

	print "jodido" 
