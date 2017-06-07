#!/usr/bin/python

a = input ("ingrese longuitud del lado a: ")
b = input ("ingrese longuitud del lado b: ")
c = input ("ingrese longuitud del lado c: ")

if ((a+b>c) and (a+c>b) and (b+c>a)):
	print ("es un triangulo")

else:
	print ("no es un triangulo")

