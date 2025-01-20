import threading
import time

#función que simula el procesamiento de una solicitud
def process_request(request_id):
    print(f'Procesando solicitud {request_id}')
    time.sleep(3)
    print(f'Solicitud {request_id} completada')

threads = []

for i in range(3):
    #Crear nuevo hilo que ejecutará la función
    thread = threading.Thread(target=process_request, args=(i,))
    threads.append(thread)
    thread.start()

#Esperar a que todos los hilos terminen
for thread in threads:
    #Asegura de el programa espere a que cada hilo termine
    thread.join()

print('Todas las solicitudes completadas')



import multiprocessing

#Función que calcule el cuadrado de un número
def calculate_square(n):
    return n*n

if __name__ == '__main__':
    numbers = [1,2,3,4,5]

    #crear un pool
    with multiprocessing.Pool() as pool:
        results = pool.map(calculate_square, numbers)

    print(f'Resultados: {results}')