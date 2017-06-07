#!/usr/bin/python

anio = input ("Ingrese un anio calendario: ")

if anio ==1800:
	print ("no es un anio bisiesto")
elif anio %4==0:
	print ("es un anio bisiesto")
elif anio %100==0:
	print ("no es un anio bisiesto")
elif anio %400==0:
	print ("es un anio bisiesto")
else:
	print ("no es un anio bisiesto")

 

 
