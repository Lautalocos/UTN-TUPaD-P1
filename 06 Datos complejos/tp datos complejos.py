#actividad 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

precios_frutas['naranja'] = 1200
precios_frutas['manzana'] = 1500
precios_frutas['pera'] = 2300


print(precios_frutas)

#actividad 2

precios_frutas['Banana'] = 1330
precios_frutas['manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

#actividad 3

lista_precios_frutas = list(precios_frutas.keys())

print(lista_precios_frutas)

#actividad 4

contactos = {}

while len(contactos) < 5:
    contactos[str(input("ingrese el nombre del nuevo contacto: "))] = int(input("ingrese el numero del nuevo contacto: "))

buscador = str(input("ingrese el nombre del contacto a buscar: "))


if buscador in contactos:
    print(f"el numero del contacto {buscador} es {contactos[buscador]}")
else:
    print("el nombre no se encuentra en la lista de contactos")

#actividad 5

frase = input("ingrese una frase: ")
palabras = frase.split()
unico = set(palabras)

print(f"las palabras unicas son {unico}")

contador = {}

for i in palabras:
    contador[i] = contador.get(i, 0) + 1

print(f"veces que se repite cada palabra: {contador}")

#actividad 6

alumnos = {}

for alumno in range(3):
    alumno = str(input("ingrese el nombre del alumno: "))
    notas = []
    for nota in range(3):
        nota = int(input(f"ingrese la nota {nota + 1}° de {alumno}: "))
        notas.append(nota)
    alumnos[alumno] = tuple(notas)

print(alumnos)

for alumno, notas in alumnos.items():
    suma = sum(notas) / 3
    print(f"{alumno}: {suma}")

#actividad 7

aprobados_parcial_1 = {1, 2, 3, 4, 5, 8, 9, 15}  # Ejemplo
aprobados_parcial_2 = {3, 4, 5, 6, 7, 9, 10, 12, 14}

print("aprobaron ambos parciales :", aprobados_parcial_1.intersection(aprobados_parcial_2))

print("aprobaron solo uno de los dos :", aprobados_parcial_1.symmetric_difference(aprobados_parcial_2))

print("aprobaron al menos uno :", aprobados_parcial_1.union(aprobados_parcial_2))

# actividad 8

productos = {"manzana": 20, "naranja": 30, "banana": 15}

producto = input("ingrese nombre de producto: ")

if producto in productos:
    opcion = input("¿desea añadir unidades?")
    if opcion == "si":
        cantidad = int(input("¿cuantas unidades desea añadir? "))
        productos[producto] += cantidad
        print(f"ahora {producto} tiene {productos[producto]} unidades.")
    else:
        print(f"stock de {producto}: {productos[producto]}")
else:
    cantidad = int(input("producto no existe. indique cantidad de unidades: "))
    print(f"se ha agregado {producto} con {cantidad} unidades.")

#actividad 9
agenda = {(5, "09:00"): "parcial", (10, "15:30"): "trabajo practico", (2, "10:00"): "grabacion de video"}

dia = int(input("ingrese el dia: "))
hora = input("ingrese la hora (hora:minuto): ")

if (dia, hora) in agenda:
    print(f"la actividad para {dia} a las {hora} es: {agenda[(dia, hora)]}")
else:
    print("Sin actividades.")

#actividad 10

paises = {"argentina": "buenos Aires", "chile": "santiago", "uruguay": "montevideo"}

capital_pais = {capital: pais for pais, capital in paises.items()}

print("resultado :", capital_pais)