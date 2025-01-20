class MultiplierFactory:
    
    def __new__(cls, factor: int):
        print(f"Creando instancia con factor {factor}")
        return super(MultiplierFactory, cls).__new__(cls)
    
    def __init__(self, factor: int):
        print(f"Inicializando con factor {factor}")
        self.factor = factor
    
    def __call__(self, number: int) -> int:
        return number * self.factor
    
multiplier = MultiplierFactory(5)

result = multiplier(10)
print(result)



def mi\_decorador(func):

&#x20;   def envoltura():

&#x20;       print("Algo se está haciendo antes de llamar a la función.")

&#x20;       func()

&#x20;       print("Algo se está haciendo después de llamar a la función.")

&#x20;   return envoltura



@mi\_decorador

def saludar():

&#x20;   print("¡Hola!")



saludar()