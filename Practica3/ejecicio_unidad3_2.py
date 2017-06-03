#!/usr/bin/python
cuenta ={}

p1=raw_input ("ingrese su nombre: ")

p2=raw_input ("ingrese su apellido: ")

p3=input ("ingrese su dni: ")

p4=(p1+p2)

len(p4)

clave = (len(p4)*p3)

cuenta={"nombre": (p1), "apellido":(p2), "dni": (p3), "clave":(clave) }

print (cuenta)
