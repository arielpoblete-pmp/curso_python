# Función que suma dos números
def add(a, b):
    return a + b

# Función que resta dos números
def subtract(a, b):
    return a - b

# Función que multiplica dos números
def multiply(a, b):
    return a * b

# Función que divide dos números
def divide(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre 0")
    return a / b

if __name__ == "__main__":
    print('Operaciones')
    res_1 = add(3,4)
    print(f'Suma: {res_1}')
    print(divide(10,7))


#Lista de diccionarios
employees = []

def add_employee(name: str) -> dict:
    '''
    Crea un diccionario con un único ítem(name) y lo agrega a la lista de empleados
    '''
    tupla = [('name', name)]
    dict_employee = {key: value for (key,value) in tupla}
    employees.append(dict_employee)
    return dict_employee

def delete_employee(name: str):
    '''
    Busca el nombre(name) entre los diccionarios de la lista de empleados y elimina al empleado de la lista
    '''
    for dicti in employees:
        if dicti.get('name') == name:
            employees.remove(dicti)


if __name__ == '__main__':
    print(employees)
    add_employee('David')
    print(employees)
    add_employee('Carlos')
    print(employees)
    delete_employee('David')
    print(employees)

```#Lista de diccionariosemployees = \[]
def add\_employee(name: str) -> dict:    '''    Crea un diccionario con un único ítem(name) y lo agrega a la lista de empleados    '''    tupla = \[('name', name)]    dict\_employee = {key: value for (key,value) in tupla}    employees.append(dict\_employee)    return dict\_employee
def delete\_employee(name: str):    '''    Busca el nombre(name) entre los diccionarios de la lista de empleados y elimina al empleado de la lista    '''    for dicti in employees:        if dicti.get('name') == name:            employees.remove(dicti)

if \_\_name\_\_ == '\_\_main\_\_':    print(employees)    add\_employee('David')    print(employees)    add\_employee('Carlos')    print(employees)    delete\_employee('David')    print(employees)