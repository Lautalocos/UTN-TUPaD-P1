#ejercicio 1
edad = int(input("ingrese su edad: "))

if edad <= 0:
    print("ingrese una edad mayor a 0")
elif edad < 18:
    print("usted es menor de edad")
else:
    print("usted es mayor de edad")

#ejercicio 2
#nota = int(input("ingrese su nota: "))

#if nota >= 6:
#    print("aprobado")
#else:
#    print("desaprobado")

#ejercicio 3
#num = int(input("ingrese un numero: "))

#if num % 2 == 0:
#    print("Ha ingresado un número par")
#else:
#    print("Por favor, ingrese un número par")

#ejercicio 4
#edad = int(input("ingrese su edad: "))

#if edad <= 0:
#    print("ingrese una edad mayor a 0")
#elif edad < 12:
#    print("usted es un niño/a")
#elif edad >= 12 and edad < 18:
#    print("usted es un adolescente")
#elif edad >= 18 and edad < 30:
#    print("usted es un adulto joven")
#else:
#    print("usted es un adulto")

#ejercicio 5
#contraseña = str(input("ingrese una contraseña que tenga entre 8 y 14 caracteres: "))

#caracteres = len(contraseña)

#if caracteres >= 8 and caracteres <= 14:
#    print("Ha ingresado una contraseña correcta")
#else:
#    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#ejercicio 6
#from statistics import mode, median, mean
#import random
#numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

#media = mean(numeros_aleatorios)
#mediana = median(numeros_aleatorios)
#moda = mode(numeros_aleatorios)

#print(f"la media es {media}")
#print(f"la mediana es {mediana}")
#print(f"la moda es {moda}")

#if media > mediana and mediana > moda:
#    print("hay sesgo positivo")
#elif media < mediana and mediana < moda:
#    print("hay sesgo negativo")
#elif media == mediana and mediana == moda:
#    print("no hay sesgo")

#ejercicio 7
#palabra = str(input("ingrese una palabra o frase: "))

#if palabra[-1].lower() in 'aeiouáéíóú':
#    palabra += "!"

#print(palabra)

#ejercicio 8
#nombre = str(input("ingrese su nombre: "))
#num = int (input("ingrese 1 si quiere su nombre en mayusculuas, 2 si quiere en minusculas y 3 si quiere solo la primer letra en mayusculas: "))

#if num == 1:
#    print(nombre.upper())
#elif num == 2:
#    print(nombre.lower())
#elif num == 3:
#    print(nombre.title())

#ejercicio 9
#magnitud = int(input("indique la magnitud del terremoto: "))

#print("en la escala de richter el terremoto tiene una magnitud: ")

#if magnitud > 0 and magnitud < 3:
#    print("muy leve")
#elif magnitud >= 3 and magnitud < 4:
#    print("leve")
#elif magnitud >= 4 and magnitud < 5:
#    print("moderado")
#elif magnitud >= 5 and magnitud < 6:
#    print("fuerte")
#elif magnitud >= 6 and magnitud < 7:
#    print("muy fuerte")
#elif magnitud >= 7:
#    print("extremo")

#ejercicio 10
#hemis = str(input("ingrese en que hemisferio esta, norte o sur (n/s): "))
#mes = int(input("ingrese el mes (numero): "))
#dia = int(input("ingrese el dia del mes: "))
#estacion = str

#if hemis == "n" or hemis == "norte":
#    if (mes == 12 and dia >= 21) or (mes >= 1 and mes <= 3) or (mes == 3 and dia <= 20):
#        estacion = "invierno"
#    elif (mes >= 3 and mes <= 5) or (mes == 3 and dia >= 21) or (mes == 6 and dia <= 20):
#        estacion = "primavera"
#    elif (mes >= 6 and mes <= 8) or (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20):
#        estacion = "verano"
#    elif (mes >= 9 and mes <= 11) or (mes == 9 and dia >= 21) or (mes == 12 and dia <= 20):
#        estacion = "otoño"
#elif hemis == "s" or hemis == "sur":
#    if (mes == 12 and dia >= 21) or (mes >= 1 and mes <= 3) or (mes == 3 and dia <= 20):
#        estacion = "verano"
#    elif (mes >= 3 and mes <= 5) or (mes == 3 and dia >= 21) or (mes == 6 and dia <= 20):
#        estacion = "otoño"
#    elif (mes >= 6 and mes <= 8) or (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20):
#        estacion = "invierno"
#    elif (mes >= 9 and mes <= 11) or (mes == 9 and dia >= 21) or (mes == 12 and dia <= 20):
#        estacion = "primavera"
#else:
#    print("revise los datos ingreasados")

#print(f"en el dia {dia} del mes {mes}, la estacion es {estacion}")
