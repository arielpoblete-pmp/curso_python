import os

#Obtener el directorio actual
"""cwd = os.getcwd()
print("Directorio de trabajo actual", cwd)"""

#Listar los archivos .txt
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Archivos txt: ", txt_files)

#Renombrar archivo
os.rename('caperucita.txt', 'cuento.txt')
print('Archivo renombrado')

#Listar los archivos .txt
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Archivos txt: ", txt_files)

import math

#Hallar el area y perimetro de un circulo
radius = 5
area = math.pi * radius**2
perimeter = 2 * math.pi * radius
print(area)
print(perimeter)

import random

#Generar un numero entero aleatorio
random_number = random.randint(1,10)
print(random_number)

#Elegir colores aleatorios
colors = ['Rojo', 'Azul', 'Verde']
random_color = random.choice(colors)
print(random_color)

#Barajar una lista de cartas
cards = ['As', 'Rey', 'Reina', 'Jota', '10']
random.shuffle(cards)
print(cards)