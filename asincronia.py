import asyncio
import time


# time.sleep(3)-> bloquea que continúe ninguna ejecución hasta que el tiempo se complete.
 
# asyncio.sleep(3)-> NO bloquea ninguna ejecucion, cede el control.

# await-> Le digo al programa k puede continuar haciendo X mientras espera

# asyncio.gather()-> Gather permite lanzar tareas en paralelo

# asyncio.run() -> Para llamar a una funcion asincronica.








###########################
#### SIN ASINCRONIA #######
###########################
def pedir_cafe_sync():
    print("Pidiendo un cafe...")
    time.sleep(3) # Permite bloquear el programa por un tiempo concreto
    print("cafe listo!")
    return "Cafe"


inicio = time.time()
pedir_cafe_sync()
fin = time.time()


print(f"Tiempo total = {fin - inicio:.2f}") #para k me lo de solo en 2 digitos
#  Pidiendo un cafe...
# cafe listo!
# Tiempo total = 3.01










###########################
#### CON ASINCRONIA #######
###########################

async def pedir_cafe_async_basic():
    print("Pidiendo un cafe...")
    time.sleep(3)
    print("cafe listo!")
    return "Cafe"

inicio = time.time()
pedir_cafe_async_basic()
fin = time.time()

print(f"Tiempo total = {fin - inicio:.2f}")
# Tiempo total = 0.01










######################################################
#### CON ASINCRONIA Y AWAIT ##########################
######################################################

# async def pedir_cafe():
#     print("Pidiendo un cafe...")
#     await asyncio.sleep(3) # Con asyncio no se bloquea, cede el control. Y le añado AWAIT para k continue haciendo algo
#     print("cafe listo!")
#     return "Cafe"

# inicio = time.time()
# pedir_cafe()
# fin = time.time()

# print(f"Tiempo total = {fin - inicio:.2f}")
# #Tiempo total = 0.00
# # El tiempo total es zero pk aunk la funcion es asincrona, su contexto (inicio, fin) es sincrono.










###### PERFECTO, AHORA EJEMPLO PARA VER K TARDA 3S, PERO NO DEMUESTRA K PUEDA LANZAR ACCIONES PARALELAS:

# async def pedir_cafe():
#     print("Pidiendo un cafe...")
#     await asyncio.sleep(3)
#     return "Cafe"


# async def main():
#     inicio = time.time()
#     await(pedir_cafe())
#     fin = time.time()
#     print(f"Tiempo total {fin - inicio}:.2f")

# asyncio.run(main())
# #Pidiendo un cafe...
# #cafe listo!
# #Tiempo total = 3.00






###### PERFECTO, AHORA EJEMPLO K DEMUESTRE K PUEDA LANZAR ACCIONES PARALELAS:

async def pedir_cafe_async_paralel_tasks():
    print("Pidiendo un cafe...")
    await asyncio.sleep(3)
    print("cafe listo!")
    return "Cafe"


async def main():
    inicio = time.time()
    await asyncio.gather( # gather permite lanzar tareas k se ejecutan a la vez
        pedir_cafe_async_paralel_tasks(),
        pedir_cafe_async_paralel_tasks(),
        pedir_cafe_async_paralel_tasks()
    )
    fin = time.time()
    print(f"Tiempo total {fin - inicio}:.2f")

asyncio.run(main())
# Pidiendo un cafe...
# Pidiendo un cafe...
# Pidiendo un cafe...
# cafe listo!
# cafe listo!
# cafe listo!
# Tiempo total 3

# Los tres cafes se piden de manera paralela por lo k el tiempo total no es 9, es 3!

async def pedir_cafe():

	print("Pidiendo un cafe...")
	await asyncio.sleep(3)
	print("cafe listo!")
	return "Cafe"


async def pedir_4_cafes_en_paralelo():
    inicio = time.time()
    await asyncio.gather(
        pedir_cafe(),
        pedir_cafe(),
        pedir_cafe(),
        pedir_cafe()
	)
    fin = time.time()
    print(f"cafes listos en {inicio - fin:.2f} ")

asyncio.run(pedir_4_cafes_en_paralelo())

