#!/usr/bin/python

tipo = input ("ingrese edad: ")

if tipo < 2:
	
	print "bebe"

elif tipo >2 and tipo<=12:

	print "menor"
elif tipo > 12 and tipo <=18:

	print "adolescente" 

elif tipo>18 and tipo<=45:

	print "adulto"

elif tipo>45 and tipo<=60:

	print "veterano"

else:
	print "abuelo"
