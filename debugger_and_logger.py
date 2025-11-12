import logging

#Basic config to save logs on a file (although not optimal)
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def mi_funcion_importante(data) :
    logging.info(f"funcion iniciada con los datos: ${data}")
    try :
        resultado = data / 2
        logging.info(f"calculo exitoso. Resultado: ${resultado}")
        return resultado
    except TypeError:
        logging.error("Error! los datos de entrada no eran un numero.", exc_info=True)
        return None
mi_funcion_importante("texto")



# To debug
def calcular_precio_con_descuento(precio_base, descuento_porc):
    factor_descuento = descuento_porc / 100

    precio_final = precio_base * (1 + factor_descuento)
    return precio_final

precio_producto = 100
descuento = 20
print(f"El precio final es: {calcular_precio_con_descuento(precio_producto, descuento)}")