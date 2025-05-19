# ejercicio 1
def factorial(num):
    if num == 0:
        return 1
    else:
        return factorial(num-1) * num

num = int(input("ingrese un numero: "))

print(factorial(num))

# ejercicio 2
def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos-1) + fibonacci(pos-2)

pos = int(input("Introduzca un numero: "))

print("la serie de fibonacci completa es: ")
for i in range(pos + 1):
    print(fibonacci(i), end=" ")

# ejercicio 3
def pot(base, expo):
    if expo == 0:
        return 1 
    else:
        return base * pot(base, expo - 1)

# Algoritmo general de prueba
base = int(input("Introduce la base: "))
expo = int(input("Introduce el exponente: "))

resultado = pot(base, expo)
print(f"{base} elevado a la {expo} es igual a {resultado}")

# ejercicio 4
def entero_a_binario(num):
    if num == 0:
        return ""
    else:
        return entero_a_binario(num // 2) + str(num % 2)

num = int(input("ingrese un numero entero: "))

print(entero_a_binario(num))

# ejercicio 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

palabra = str(input("ingrese una palabra: "))

if es_palindromo(palabra):
    print(f"la palabra {palabra} es palindromo")
else:
    print("la palabra ingresada no es palindromo")

# ejercicio 6
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

n = int(input("ingrese un numero: "))

print(f"la suma de los digitos del numero {n} es {suma_digitos(n)}")

# ejercicio 7
def contar_bloques(n):
    if n == 0:
        return 0
    else:
        return n + contar_bloques(n-1)

n = int(input("ingrese el numero de bloques de la base de la piramide: "))

print(f"el numero de bloques de una piramide con una base de {n} bloques es {contar_bloques(n)}")

# ejercicio 8
def contar_digito(numero, digito):
    if numero < 10:
        return 1 if numero == digito else 0
    contador = 1 if numero % 10 == digito else 0
    return contador + contar_digito(numero // 10, digito)

numero = int(input("ingrese un numero entero: "))
digito = int(input("ingrese el digito que quiere buscar dentro del numero anterior: "))

print(f"el digito {digito} aparece {contar_digito(numero, digito)} veces en el numero {numero}")


