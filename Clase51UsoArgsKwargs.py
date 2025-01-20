def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1,2,3,4,5))
print(sum_numbers(1,2))
print(sum_numbers(1,2,3,4,5,7,8,9,10))


#Desempaquetado args
def add(a, b, c):
    return a + b + c

values = (1, 2, 3)
print(add(*values)) 

def show_info(name, age):
    print(f"Name: {name}, Age: {age}")

data = {"name": "Ana", "age": 28}
show_info(**data)


class Employee:
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.skills = args
        self.details = kwargs
    
    def show_employee(self):
        print(f'Employee: {self.name}')
        print('Skills', self.skills)
        print('Details', self.details)

employee = Employee('Carlos', 'Python', 'Java', 'C++', age=30, city = 'Bogotá')
employee.show_employee()

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

print_info(name='Carlos', age=30, city='Bogotá')
print_info(name='Carlos', age=30, city='Bogotá', country = 'Colombia')