import os

class OperasBas:

    def init(self):
        pass

    def suma(self, num1, num2):
        res = num1 + num2
        return res

    def resta(self, num1, num2):
        res = num1 - num2
        return res

    def multiplicacion(self, num1, num2):
        res = num1 * num2
        return res

    def division(self, num1, num2):
        res = num1 / num2
        return res


def main():
        os.system('cls')
        ob = OperasBas()
        opt = -1
        res = 0
        while (opt != 0):
            print('Menú de opciones \n1.- Suma \n2.- Resta \n3.- Multiplicación \n4.- División \n5.- Salir\n')
            opt = int(
                input('Elige una opción del menú:'))
            if (opt == 5):
                break
            os.system('cls')

            num1 = int(input('Ingresa el primer número:'))
            num2 = int(input('Ingresa el segundo número:'))
            if (opt == 1):
                res = ob.suma(num1, num2)

            elif (opt == 2):
                res = ob.resta(num1, num2)

            elif (opt == 3):
                res = ob.multi(num1, num2)

            elif (opt == 4):
                res = ob.div(num1, num2)
            print('El resultado es: {}'.format(res))



#print("La suma es: {} ".format(obj.res))
   # print("La resta es: {} ".format(obj.res))
   # print("La multiplicacion es: {} ".format(obj.res))
   # print("La division es: {} ".format(obj.res))

if __name__ == '__main__':
        main()
    