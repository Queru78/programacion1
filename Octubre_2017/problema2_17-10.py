#problema 2 

#input: 
#1 una lista de N posiciones iniciadas en 0:
#2 una lista cuyo elemento es una tupla con los siguientes forma:
#(elem 1, elem 2)
#3 elem 1: un rango de numeros con maximo = longitud de la lista definitiva en el punto 1
#4 elem 2: un numero randam de 1 a 999
#output: 
#la lista definitiva en el punto 1 debe llenarse sumando los valores elem 2 de las tuplas e sus posiciones definitivas en los rangos elem 1.

#ejemplos:  input1: [0,0,0,0,0] [((0,3),327),((3,5),292),((1,4),173)]
#output1: [327,500,500,465,292]
import random
def generar_lista():
	long = random.randint(1,11)
	for i in range(1,long):
		print i
generar_lista() 		










lista1 = [0,0,0,0,0]

lista2 = [(range(0,3), 327), (range(3,5),292), (range(1,4),173)]

for i in lista2:
	for i2 in i[0]:
		v = i[1]
		lista1[i2] = lista1[i2] + v
print lista1
	

