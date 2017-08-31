#!/usr/bin/python

num1 = input ("ingrese el primer numero: ")
num2 = input ("ingrese el segundo numero: ")

def mayor(num1,num2):
	if  num1 < num2:
		return num2
	elif num1 > num2:
		return num1
	else:
		print ("los numeros son iguales")
		return 0
print mayor(num1,num2)

