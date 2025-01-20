# Ejemplo de Docstrings 

def calculate_average(numbers):
    '''
    Calcula el promesio de una lista de números.

    Parámetros:
    numbers (lista): Lista de número enteros o flotantes.

    Retorna (float): El promedio de los números en la lista
    '''
    return sum(numbers) / len(numbers)

# Imprime el promedio de una lista de números
print(calculate_average([1, 2, 3, 4, 5, 6]))