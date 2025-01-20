from collections import defaultdict

def count_products(orders: list[str]) -> defaultdict:
    #Crea un diccionario con valor por defecto 0 
    product_count = defaultdict(int)
    for product in orders:
        product_count[product] +=1
    return product_count

orders = ['laptop', 'smartphone', 'laptop', 'tablet']
count = count_products(orders)
print(count)

from collections import Counter

def count_sales(products: list[str]) -> Counter:
    # Usa Counter para contar cuántos productos de cada tipo se han vendido
    return Counter(products)

sales = ["laptop", "smartphone", "smartphone", "laptop", "tablet"]
result = count_sales(sales)
print(result)  # Output: Counter({'laptop': 2, 'smartphone': 2, 'tablet': 1})

from collections import deque

def manage_delivery_queue() -> deque:
    # Crea una cola para gestionar entregas de productos
    delivery_queue = deque(["order_1", "order_2", "order_3"])
    delivery_queue.append("order_4")  # Agrega al final de la cola
    delivery_queue.appendleft("order_0")  # Agrega al principio de la cola
    delivery_queue.pop()  # Elimina del final
    delivery_queue.popleft()  # Elimina del principio
    return delivery_queue

queue = manage_delivery_queue()
print(queue) 

from enum import Enum

class OrderStatus(Enum):
    PENDING = 1 #Pendiente
    SHIPPED = 2 #Enviado
    DELIVERED = 3 #Entregado

def check_order_status(status: OrderStatus):
    # Comprueba el estado del pedido y devuelve un mensaje
    if status == OrderStatus.PENDING:
        return "Order is still pending."
    elif status == OrderStatus.SHIPPED:
        return "Order has been shipped."
    elif status == OrderStatus.DELIVERED:
        return "Order has been delivered."
    
print(check_order_status(OrderStatus.DELIVERED)) 






#lo hice de manera muy sencilla en cuanto a
#los pedidos, y al final probando el código
#para uno de los pedidos
from collections import defaultdict, Counter
from enum import Enum

#lista de pedidos para realizar pruebas:
pedido1 = ["arroz", "panela", "galletas", "pollo", "pollo", "salchichón", "arroz"]
pedido2 = ["arroz", "galletas", "pollo", "pollo", "salchichón", "arroz"]
pedido3 = ["galletas", "galletas", "pollo", "pollo", "salchichón", "arroz"]

#empleando defaultdicts:
def registro_productos(pedido: list[str]) -> defaultdict:
    registro = defaultdict(int)
    for producto in pedido:
        registro[producto] += 1
    return registro


#creando clase para enumerar el estado del pedido mediante la enumeración
class OrderStatus(Enum):
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3

def check_order_status(status: OrderStatus):
    if status == OrderStatus.PENDING:
        return "La orden aún se encuentra pendiente."
    if status == OrderStatus.SHIPPED:
        return "La orden ya ha sido enviada."
    if status == OrderStatus.DELIVERED:
        return "La orden ya ha sido entregada."

#Empleando un Contador para realizar el conteo de cada uno de los productos:
def contador(productos: list[str]) -> Counter:
    return Counter(productos)

#se realiza el checkeo del estado de la orden
print(check_order_status(OrderStatus.PENDING))
#se realiza el registro del pedido y se imprime
registro_pedido = registro_productos(pedido1)
print(registro_pedido)
#se realiza el conteo de cada producto y se imprime
print(contador(pedido1))
```from collections import defaultdict, Counterfrom enum import Enum
\#lista de pedidos para realizar pruebas:pedido1 = \["arroz", "panela", "galletas", "pollo", "pollo", "salchichón", "arroz"]pedido2 = \["arroz", "galletas", "pollo", "pollo", "salchichón", "arroz"]pedido3 = \["galletas", "galletas", "pollo", "pollo", "salchichón", "arroz"]
\#empleando defaultdicts:def registro\_productos(pedido: list\[str]) -> defaultdict:    registro = defaultdict(int)    for producto in pedido:        registro\[producto] += 1    return registro

\#creando clase para enumerar el estado del pedido mediante la enumeraciónclass OrderStatus(Enum):    PENDING = 1    SHIPPED = 2    DELIVERED = 3
def check\_order\_status(status: OrderStatus):    if status == OrderStatus.PENDING:        return "La orden aún se encuentra pendiente."    if status == OrderStatus.SHIPPED:        return "La orden ya ha sido enviada."    if status == OrderStatus.DELIVERED:        return "La orden ya ha sido entregada."
\#Empleando un Contador para realizar el conteo de cada uno de los productos:def contador(productos: list\[str]) -> Counter:    return Counter(productos)
\#se realiza el checkeo del estado de la ordenprint(check\_order\_status(OrderStatus.PENDING))#se realiza el registro del pedido y se imprimeregistro\_pedido = registro\_productos(pedido1)print(registro\_pedido)#se realiza el conteo de cada producto y se imprimeprint(contador(pedido1))