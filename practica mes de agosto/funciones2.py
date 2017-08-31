
#!/usr/bin/python

num1 = input ("ingrese el primer numero: ")
num2 = input ("ingrese el segundo numero: ")
num3 = input ("ingrese el trecer numero: ")

def mayor(num1,num2,num3):
        if  num1 < num2 and num3 < num2:
                return num2
        elif num2 < num1 and num3 < num1:
                return num1
	elif num2 < num3 and num1 < num3:
		return num3
        else:
                print ("los numeros son iguales")
		return 0
print mayor(num1,num2,num3)

