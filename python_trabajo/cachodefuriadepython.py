#! /usr/bin/python

dni = input ("ingrese un dni: ")

def dni_check (num):
	count = 0
	if num < 100:
		return False
	else: 
		smun = str(num)
		for i in smun:
			if (int(i) % 2) !=0:
				count+=1
		return (count >= 3)

v = dni_check(dni)
if v:
	print "el %s es valido " % (dni)

