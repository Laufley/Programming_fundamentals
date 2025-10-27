import math

###############################################
# FUNCIONES = CIUDADANOS DE PRIMERA CLASE 
###############################################

def saludar(nombre):
    return f"Hola, {nombre}!"

# Asignar la función a una variable
saludo = saludar

# Ahora la variable 'saludo' puede ser usada para llamar a la función
print(saludo("pepe"))

# tmbién podemos pasar funciones como argumentos a otras funciones
def responder(saludo, nombre):
    return f"{saludo(nombre)} ¿Cómo estás?"

print(saludo("juan"))
print(responder(saludo, "Juan"))



###############################################
# FUNCIONES = CIUDADANOS DE PRIMERA CLASE 
###############################################

# Ejemplo funcion impura
mi_lista = [1, 2, 3]

def add_num_impuro(num):  # Este f(x) tiene un efecto secundario k es add 1 num en la lista
    mi_lista.append(num) # Este efecto es impredecible si no sabes k existe esta lista fuera de la f(x)

add_num_impuro(4) 
print(mi_lista) 


# Ejemplo funcion pura: Creo una copia de la lista original, y modifico esa copia. La salia es una nueva lista
# Todo cambio se ha producido dentro de la funcion sin afectar a nada k estubiera fuera
mi_lista_2 = [1, 2, 3]
def add_pure_num(original_list, num):
    new_list = original_list.copy()
    new_list.append(num)
    return new_list

###############################################
# Lambda Functions
###############################################

def duplicar(n):
    return n*2

lambda_duplicar = lambda n: n*2

print(lambda_duplicar(2))

###############################################
# MAP & LIST
###############################################

lista_numeros = [1, 2, 3, 4]

numeros_duplicados_map = map(lambda x: x*2, lista_numeros)
print(list(numeros_duplicados_map))

# otra manera

python_way = [x*2 for x in lista_numeros]
print(f"python way{python_way}")

###############################################
# FILTER & LIST
###############################################

numeros_originales = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_pares = filter(lambda x : x % 2 == 0, numeros_originales)
print(list(numeros_pares))

# si no usaramos filter, la forma con loop seria
numeros_pares_loop = [x for x in numeros_originales if x%2 ==0]
print(list(numeros_pares_loop))

func = list()



######### EJERCICIOS ##########
temps_f = ["32", "68", "104", "50", "77"]

def convert_to_int(given_list):
    int_list = []
    for num in given_list :
        result = int(num)
        int_list.append(result)
    return int_list

temps_int = convert_to_int
print(temps_int(temps_f))


def celsius_converter(given_list):
    maths = lambda x: (x - 32) * 5/9
    result = map(maths, given_list)
    return result
celsius = celsius_converter
print(list(celsius(temps_int(temps_f))))

def round_up(param_list):
   result= map(lambda x: math.ceil(x), param_list)
   return result

print(list(round_up(celsius(temps_int(temps_f)))))

###############################################

numbers = [1, 2, 3, 4, 5]

doubled_numbers = map(lambda x : x*2, numbers)
print(list(doubled_numbers))

double_numbers_stored_list_directly = list(map(lambda x: x*2, numbers))
print(double_numbers_stored_list_directly)

doubled_numbers_python_way = [x * 2 for x in numbers]
print(list(doubled_numbers_python_way))

################################################

ages_list = [15, 21, 17, 30, 19, 40]
only_adults = list(filter(lambda x : x > 18, ages_list))
print(only_adults)

only_adults_python_way_bools = [x > 18 for x in ages_list] # returns bools!
print(only_adults_python_way_bools)

def filter_python_way (number, array):
    adults = []
    for n in array:
        if n >= number :
            adults.append(n)
    return adults

print(filter_python_way(18, ages_list))

## SIMPLIFY
filter_python_way_shorter = [x for x in ages_list if x>18]
print(filter_python_way_shorter)

weights_list = [47, 49, 56, 42, 68, 71]

divide_by_2 = [x / 2 for x in weights_list]
to_int = [int(x) for x in (divide_by_2)]
print(to_int)


speed_values = [80, 85, 90, 100, 120, 140, 150, 200]
is_over_speed_limit = [ x > 120 for x in speed_values]
print(is_over_speed_limit)
print(is_over_speed_limit)

speed_values = [80, 85, 90, 100, 120, 140, 150, 200]
values_over_speed_limit = [x for x in speed_values if x>120]
print(values_over_speed_limit)

################################################

temp_celsius = [12, 25, 37, 40, 5, 20, 30]

filter_temp_over_20_comprension_lista = [x for x in temp_celsius if x > 20]
print(filter_temp_over_20_comprension_lista)

filter_temp_over_20_with_filter = filter(lambda x: x>20, temp_celsius)

convert_to_farenheit_with_map = map(lambda x : (x * (9 / 5) + 32), filter_temp_over_20_with_filter)
print(list(convert_to_farenheit_with_map))

convert_to_farenheit_with_comprension_lista = [x * (9 / 5) + 32 for x in filter_temp_over_20_comprension_lista]
print(convert_to_farenheit_with_comprension_lista)