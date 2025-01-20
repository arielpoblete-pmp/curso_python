#Decorador que comprueba si un empleado tiene un rol específico
def check_access(required_role):
    def decorator(func):
        def wrapper(employee):
            #Si el rol de lempleado coincide con el rol requerido
            if employee.get('role') == required_role:
                return func(employee)
            else:
                print(f'ACCESO DENEGAGO. Solo {required_role} pueden realizar esta acción')
        return wrapper
    return decorator

def log_action(func):
    def wrapper(employee):
        print(f'Registrando acción para el empleado {employee['name']}')
        return func(employee)
    return wrapper

@check_access('admin')
@log_action
def delete_employee(employee):
    print(f'El empleado {employee['name']}, ha sido eliminado')

admin = {'name': 'Carlos', 'role': 'admin'}
employee = {'name': 'Ana', 'role': 'employee'}

#delete_employee(admin)
delete_employee(employee)




class User:
    def __init__(self, name:str, role:str) -> None:
        self.name = name
        self.role = role

def get_current_user():
    return User('gb.so', 'admin')

# función decoradora
def check_access(required_role: str): #aquí recibimos el parámetro enviado al decorador
    def decorator(func): #este es el decorador que recibe la función
        def wrapper(user: User):  # función envolvente, es necesario poner los parámetros
            current_user = get_current_user()
            if current_user.role == required_role:
                return func(user)
            else:
                raise Exception(f'el usuario {current_user.name} no tiene permitida la acción de eliminar usuarios porque no es {required_role}')
        return wrapper
    return decorator


@check_access('admin')  # decorador en uso
def delete_user(user: User):
    print('usuario eliminado')


user_to_delete = User('pepe.cierra', 'cliente')
delete_user(user_to_delete)
```class User:    def \_\_init\_\_(self, name:str, role:str) -> None:        self.name = name        self.role = role
def get\_current\_user():    return User('gb.so', 'admin')
\# función decoradoradef check\_access(required\_role: str): #aquí recibimos el parámetro enviado al decorador    def decorator(func): #este es el decorador que recibe la función        def wrapper(user: User):  # función envolvente, es necesario poner los parámetros            current\_user = get\_current\_user()            if current\_user.role == required\_role:                return func(user)            else:                raise Exception(f'el usuario {current\_user.name} no tiene permitida la acción de eliminar usuarios porque no es {required\_role}')        return wrapper    return decorator

@check\_access('admin')  # decorador en usodef delete\_user(user: User):    print('usuario eliminado')

user\_to\_delete = User('pepe.cierra', 'cliente')delete\_user(user\_to\_delete)