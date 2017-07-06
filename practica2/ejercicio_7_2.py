#!/usr/bin/python

personas  = {}
p1=raw_input ("ingrese su nombre: ")
p2=raw_input ("ingrese su apellido: ")
p3=input ("ingrese su dni: ")
p4=input("anio de nacimiento: ")
p5=raw_input ("ingrese su lugar de nacimiento: ")

contrasenia_personal=(p3*p4)

personas = {"nombre": p1, "apellido": p2, "dni": p3, "anio de nacimiento": p4, "contrasenia": (contrasenia_personal)} 

print(personas)


