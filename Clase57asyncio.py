import asyncio

async def process_data(data):
    print(f'Procesando {data}...')
    #Simular una operación
    await asyncio.sleep(10)
    print(f'{data} procesado.')
    return data * 2

async def main():
    print('Inicio de procesamiento')
    result = await process_data('archivo.txt')
    print(f'Resultado: {result}')

asyncio.run(main())


import asyncio
import random

async def donwload_process(file):
    print(f'Descargando archivo {file}')
    time=random.randint(1,10)
    await asyncio.sleep(time)
    print(f'{file} downloaded')
    return file

async def main():
    print('Inicio de la descarga')
    result=await donwload_process('file1.txt')
    result1=await donwload_process('file2.txt')
    result2=await donwload_process('file3.txt')
    print(f'{result,result1,result2}')


asyncio.run(main())