# Lista de dos dimensiones
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz:")
for fila in matriz:
    for elemento in fila:
        print(elemento, end=' ')
    print()

# Lista de tres dimensiones
tensor = [
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
]

print("\nTensor:")
for bloque in tensor:
    for fila in bloque:
        for elemento in fila:
            print(elemento, end=' ')
        print()
    print()

# Tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

print("Tupla1:", tupla1)
print("Tupla2:", tupla2)

tupla_concatenada = tupla1 + tupla2
print("Tupla concatenada:", tupla_concatenada)

tupla_repetida = tupla1 * 2
print("Tupla repetida:", tupla_repetida)

print("¿Está 3 en la tupla1?", 3 in tupla1)
print("Longitud de tupla1:", len(tupla1))

print("Elementos de tupla1:")
for elemento in tupla1:
    print(elemento)

a, b, c = tupla1
print("Desempaquetado de tupla1:", a, b, c)