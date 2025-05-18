# ejercicio 1:
def imprimir_hola_mundo():
    print ("hola mundo!")

imprimir_hola_mundo()

# ejercicio 2:
def saludar_usuario(nombre):
    print(f"hola {nombre}!")

saludar_usuario(input("ingrese su nombre: "))

# ejercicio 3:
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")
edad = input("ingrese su edad: ")
residencia = input("ingrese su residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

# ejercicio 4
import math
def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("ingrese el radio del circulo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"area del circulo: {area}")
print(f"perimetro del circulo: {perimetro}")

# ejercicio 5
def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("ingrese la cantidad de segundos: "))
horas = segundos_a_horas(segundos)

print (f"{segundos} segundos convertidos a horas equivale a {horas} horas")

# ejercicio 6
def tabla_multiplicar(numero):
    for i in range(1,11):
        print (numero * i)

numero = int(input("ingrese un numero entero: "))

tabla_multiplicar(numero)

# ejercicio 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return (suma, resta, multiplicacion, division)

a = float(input("Ingresa el primer numero: "))
b = float(input("Ingresa el segundo numero: "))

resultado = operaciones_basicas(a, b)

print(f"la suma de los 2 numeros es: {resultado[0]}")
print(f"la resta del primer numero por el segundo es: {resultado[1]}")
print(f"la multiplicacion de los 2 numeros es: {resultado[2]}")
print(f"la division del primer numero por el segundo es: {resultado[3]}")

# ejercicio 8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("ingrese su peso en kg: "))
altura = float(input("ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)

print(f"su imc es: {imc:.2f}")

# ejercicio 9
def celsius_a_fahrenheit(celsius):
    return celsius * (9/5) + 32

celsius = float(input("ingrese la temperatura en celsius: "))

fahrenheit = celsius_a_fahrenheit(celsius)
print (f"la temperatura convertida a fahrenheit es: {fahrenheit}")

# ejercicio 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("ingrese el primer numero: "))
b = float(input("ingrese el segundo numero: "))
c = float(input("ingrese el tercer numero: "))

promedio = calcular_promedio(a, b, c)
print(f"el promedio de {a}, {b} y {c} es {promedio}")