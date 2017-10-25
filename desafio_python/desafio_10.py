#!/usr/bin/python

import random
def numeros_enteros():
	lista=[] 
	long = random.randint(3,10)	
	for x in range (0,long):
		m = random.randint(1,9)
		lista.append(m)
	u = random.randint(10,15)
	lista.append(u)
	return lista


def combinatoria(l):
	ultpos = len(l)-1
	ultval = l[ultpos]
	res = []
	bl=[]
	for n in l[0:-2]:
		bl.append(n)
		for m in l[0:-2]:
		 	#print ultval
			if (n+m) == ultval:
				print ultval
				if(m not in bl):
					#print m
					t=(n,m)
					res.append(t)
					bl.append(m)
	return res


l=numeros_enteros()
print l
print combinatoria(l)
