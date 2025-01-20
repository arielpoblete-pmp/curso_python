class BaseClass:
    def __init__(self):
        self._protected_variable = 'Protected'
        self.__private_variable = 'Private'

    def _protected_method(self):
        print('Este es un metodo protegido')

    def __private_method(self):
        print('Esto es un metodo privado')

    def public_method(self):
        self.__private_method()

base = BaseClass()
#print(base._protected_variable)
#base._protected_method()

#base.public_method()
print(base.__private_variable)



def _actualizar_saldo_(self,amount : float):
    if self.is_active:
        self.balance += amount
        self.__registrar_transaction(amount)
        print (f"se ha demositado {amount}. Saldo actual {self.balance}")
        
    else:
        print(f"No se puede depostar, Cuenta inactiva")

def __registrar_transaction(self,amount: float):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    self.history.append (f"Time: {current_time}, Name: {self.name}, Transaction: +{amount}, Balance: {self.balance}")

def show_history(self):
    print("Historial de transacciones:")
    for event in self.history:
        print(event)