print('Sumar dos números')
num1=int (input('Dame el primer número'))
num2=int (input('Dame el segundo número'))

res=num1+num2
print("La suma de {0} + {1} ".format(num1, num2, res))

if num1 > num2 : 
    print("{} es mayor que {}".format(num1, num2))
else:
    print("{} es mayor que {}".format(num2, num1))

print("**************Nuevo programa************")
 
edad = int(input("Ingresa tu edad"))
if edad > 18:
    print("Eres mayor de edad")
elif edad == 18:
    print("Tienes 10 años!!!!")
else:
    print("No eres mayor de edad")

#AND, OR, NOT
#>, <, <=, =>, !

valor1=200
valor2=2
valor3=1000

if(valor1  > 1000 and valor2 > 2) or valor3 < 2000:
    print("resultado")
    