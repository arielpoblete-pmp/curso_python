class Order:

    @staticmethod
    def calculate_tax(amount, tax_rate):
        return amount * (tax_rate / 100)
    
print(Order.calculate_tax(1000, 18))


class Order:
    global_discount = 10

    def __init__(self,amount):
        self.amount = amount

    @classmethod
    def update_gloabal_discount(cls, new_discount):
        cls.global_discount = new_discount

Order.update_gloabal_discount(15)
print(Order.global_discount)
        
class Order:
    global_discount =10
    def __init__(self,amount):
        self.amount = amount
    @classmethod
    def update_global_discount(cls, new_discount):
        cls.global_discount = new_discount
        
    @staticmethod
    def calculate_mount(amount):
        if amount < 50 :
            return f"El monto es menor que el minimo permitido '{amount}'"
        else :
            return f"El monto es mayor que el minimo permitido '{amount}'"
    @classmethod
    def discount(cls,amount):
        new_amount = amount - (amount*(cls.global_discount/100))
        return f"El monto {amount} tiene un descuento global de {cls.global_discount} porciento el monto ajustado es {new_amount}"

print(Order.calculate_mount(50))
print(Order.global_discount)
Order.update_global_discount(10)
print(Order.global_discount)
print(Order.discount(300))
```Saludos.