#ejercicio 1
#num = 0

#while num <= 100:
#    print (num)
#    num = num + 1

#ejercicio 2
#num = int(input("ingrese un numero entero: "))
#digitos = 0


#while num > 0:
#    num = num // 10
#    digitos = digitos + 1

#print(f"el numero contiene {digitos} digitos")

#ejercicio 3
#numMin = int(input("ingrese el numero minimo: "))
#numMax = int(input("ingrese el numero maximo: "))
#sumador = 0


#for i in range(numMin+1, numMax):
#    sumador = sumador + i

#print (f"la suma de los numeros enteros entre los 2 ingresados es {sumador}")

#ejercicio 4
#num = 1
#suma = 0

#while num != 0:
#    num = int(input("ingrese un numero: "))
#    suma = suma + num

#print(f"el total de la suma de los numeros ingresados es {suma}")

#ejercicio 5
#import random
#azar = random.randint(0, 9)
#intento = int(input("adivine un numero entre 0 y 9: "))
#contador = 1

#while intento != azar:
#    contador = contador + 1
#    intento = int(input("equivocado! intente otra vez: "))

#print (f"felicidadez! usted adivino el numero {azar} en {contador} intentos")

#ejercicio 6

#for i in range(100, 0, -2):
#    print (i)

#ejercicio 7
#num = int(input("ingrese un numero enetero positivo: "))
#sumador = 0

#for i in range(0, num+1):
#    sumador = sumador + i

#print (sumador)

#ejercicio 8

#par = 0
#impar = 0
#posi = 0
#nega = 0
#num = 0

#cambie el 5 en range por un 100 para probar con 100 numeros
#for i in range(0, 5):
#    num = int(input("ingrese un numero entero: "))
#    if num >= 0:
#        if num % 2 == 0:
#            par = par + 1
#        else:
#            impar = impar + 1
#        posi = posi + 1 
#    else:
#        if num % 2 == 0:
#            par = par + 1
#        else:
#            impar = impar + 1
#        nega = nega + 1

#print (f"numeros pares: {par}")
#print (f"numeros impar: {impar}")
#print (f"numeros positivos: {posi}")
#print (f"numeros negativos: {nega}")

#ejercicio 9
#cambiar el valor de nums a 100 para probar con 100 numeros
#nums = 5
#sumador = 0

#for i in range(1, nums+1):
#    num = int(input(f"ingrese el n° {i}: "))
#    sumador = sumador + num

#print(f"la media de los valores ingresados es igual a {sumador/nums}")

#ejercicio 10

#num = int(input("ingrese un numero: "))
#inver = 0

#while num != 0:
#    digito = num % 10
#    inver = inver * 10 + digito
#    num = num // 10

#print(f"el numero invertido es {inver}")