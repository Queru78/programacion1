#!/usr/bin/python

pal=raw_input("ingrese palabra: ")


def inversa (palabra):

	nue = ""

	if len(palabra)==1:
		return palabra
	else:
		for i in palabra:

			nue = i + nue
		return nue

p = inversa (pal)

print p
