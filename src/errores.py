import numpy as np
import cargar_datos as cd
import matplotlib.pyplot as plt

######################## Funciones de error y operaciones #################################################3

def numero_cientifico(x, c_s = None, truncar = False, truncar_cifras = 2):
    '''
        Convierte un número a su representación en notación científica.
        Tambien puede truncar el número a un número de cifras significativas especificado.
    '''
    x_str = str(x)
    exp: int
    base: int
    num_flt: float
    num_flt1: np.float64
    if (c_s == None):
        exp = 0
        for i in range(len(x_str)):
            if x_str[i].isdigit():
                exp += 1
            else:
                break
        
        base = 10
        num_flt = float(x) / base ** exp
    else:
        exp = c_s
        base = 10
        num_flt = float(x) / base ** exp

    if truncar:
        num_flt1 = np.trunc(num_flt * 10 ** truncar_cifras) / 10 ** truncar_cifras
        return [np.array([np.float64(num_flt1)]), np.int64(base), np.int64(exp), np.float64(x)]
    else:  
        return [np.array([np.float64(num_flt)]), np.int64(base), np.int64(exp), np.float64(x)]

def error_absoluto(valor_real, valor_aproximado):
    '''Calcula el error absoluto entre un valor real y un valor aproximado.'''
    return np.abs(valor_real - valor_aproximado)

def error_relativo(valor_real, valor_aproximado):
    '''Calcula el error relativo entre un valor real y un valor aproximado. Te entrega un resultado en porcentaje.'''
    if valor_real == 0:
        raise ValueError("El valor real no puede ser cero para calcular el error relativo.")
    return (np.abs(valor_real - valor_aproximado) / valor_real) * 100

def comprar_dolares(monto_pesos, precio_compra):
    '''Calcula la cantidad de dólares que se pueden comprar con un monto en pesos y un precio de compra.'''
    return monto_pesos / precio_compra

def vender_dolares(cantidad_dolares, precio_venta):
    '''Calcula la cantidad de pesos que se obtienen al vender una cantidad de dólares a un precio de venta.'''
    return cantidad_dolares * precio_venta

def ganancia(monto_inicial, monto_final):
    '''Calcula la ganancia obtenida al comparar un monto inicial con un monto final.'''
    return monto_final - monto_inicial

def rentabilidad(monto_inicial, monto_final):
    '''Calcula la rentabilidad obtenida al comparar un monto inicial con un monto final. Entrega un porcentaje.'''
    if monto_inicial == 0:
        raise ValueError("El monto inicial no puede ser cero para calcular la rentabilidad.")
    return (monto_final / monto_inicial) * 100

def variacion_entre_meses(precio_mes_anterior, precio_mes_actual):
    '''Calcula la variación entre el precio de un mes anterior y el precio de un mes actual.'''
    return precio_mes_actual - precio_mes_anterior

def propagacion_resta(valor_aprox1, valor_aprox2, error_absoluto1, error_absoluto2):
    '''Calcula la propagación del error absoluto al restar dos valores aproximados.'''
    resultado = valor_aprox2 - valor_aprox1
    error_propagado = error_absoluto1 + error_absoluto2
    error_relativo_total = np.abs(error_propagado / resultado) if resultado != 0 else np.inf
    return [resultado, error_propagado, error_relativo_total]

def sacar_numero_redondeado_error_absoluto_relativo(datos_csv, cifras_significativas = 2):
    '''Calcula el numero redondeado, el error absoluto y el error relativo de cada mes a partir de los datos del csv, luego devuelve una lista con tres listas para cada valor.'''
    # Usaremos tres listas para guardar los errores absolutos, relativos y truncados de cada mes
    precios_reales = []
    errores_relativos = []
    errores_absolutos = []
    numeros_redondeados = []
    # Usaremos un ciclo for para recorrer cada mes y calcular los errores de representacion
    for i in range(datos_csv.shape[0]):
        precio_observado = datos_csv[i][3]
        precios_reales.append(precio_observado)
        #Calculamos el numero cientificos con la cantidad de cifras significativas que queremos,
        # y luego lo añadimos a la lista de numeros redondeados.
        numero_redondeado = numero_cientifico(precio_observado, None, truncar=True, truncar_cifras= cifras_significativas)
        numero_redondeado_2cifras = numero_redondeado[0] * numero_redondeado[1] ** numero_redondeado[2]
        numeros_redondeados.append(numero_redondeado_2cifras)

        # Calculamos el error absoluto y relativo entre el precio observado y el numero redondeado, y los añadimos a sus respectivas listas.
        er_absoluto = error_absoluto(precio_observado, numero_redondeado_2cifras)
        errores_absolutos.append(er_absoluto)
        er_relativo = error_relativo(precio_observado, numero_redondeado_2cifras)
        errores_relativos.append(er_relativo)
    return [errores_absolutos, errores_relativos, numeros_redondeados, precios_reales]

#######################################################################################################33

#A1 Error de representación mes a mes V
def representation_error():
    # Cargamos los datos del CSV usando la funcion para obtener estos datos como np.arrays de tamaño 4
    datos_csv = cd.obtener_datos()

    num_red_err_abs_rel = sacar_numero_redondeado_error_absoluto_relativo(datos_csv, cifras_significativas=2)

    # Buscamos el error relativo máximo y su índice para poder imprimir el mes y año correspondiente.
    max_er_relativo = max(num_red_err_abs_rel[1])
    ind_max_er_relativo = num_red_err_abs_rel[1].index(max_er_relativo)
    print("El error relativo máximo se encuentra en el mes", datos_csv[ind_max_er_relativo][1],"del año", datos_csv[ind_max_er_relativo][0], "con un valor de: ", numero_cientifico(max_er_relativo[0], 0, True, 2)[0][0], "%")
    # Zona de Grafico de Barras
    num_meses = range(len(num_red_err_abs_rel[1]))  # Genera un array de índices para los meses

    # Correcto: figsize va en subplots(), que crea tanto el lienzo como el gráfico
    fig, ax = plt.subplots(figsize=(12, 6))

    ax.bar(num_meses, num_red_err_abs_rel[1], color='skyblue', edgecolor= 'black')

    ax.set_xlabel('Meses')
    ax.set_ylabel('Error relativo (%)')
    ax.set_title('Error relativo mes a mes')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
#A2 Evaluación entre dos puntos (una compra-venta) V
def evaluacion_compra_venta(monto_inicial, errores_relativos, numeros_redondeados, indice_compra, indice_venta):
    precio_aprox_compra = numeros_redondeados[indice_compra]
    precio_aprox_venta = numeros_redondeados[indice_venta]
    
    error_relativo_compra = errores_relativos[indice_compra]
    error_relativo_venta = errores_relativos[indice_venta]
    
    #Propagación
    error_relativo_total = error_relativo_compra + error_relativo_venta
    
    #Operaciones financieras
    cantidad_dolares = comprar_dolares(monto_inicial, precio_aprox_compra)
    monto_final = vender_dolares(cantidad_dolares, precio_aprox_venta)
    ganancia_obtenida = ganancia(monto_inicial, monto_final)
    rentabilidad_obtenida = rentabilidad(monto_inicial, monto_final)
    
    #Pasar a error absoluto para arrastrar a la ganancia
    error_absoluto_final = (error_relativo_total * monto_final) / 100

    #Calculo del error porcentual de la ganancia se ocupa valor absoluto de la ganancia para que no de negativo, y se multiplica por 100 para pasarlo a porcentaje
    if ganancia_obtenida != 0:
        error_porcentual_ganancia = (error_absoluto_final / np.abs(ganancia_obtenida)) * 100
    else:
        error_porcentual_ganancia = float('inf') # Si la ganancia es 0, el error es infinito
    
    print(f"Ganancia obtenida: {numero_cientifico(ganancia_obtenida[0], 0, True, 2)[0][0]} ± {numero_cientifico(error_absoluto_final[0], 0, True, 2)[0][0]} pesos")
    print(f"Error porcentual de la ganancia: {numero_cientifico(error_porcentual_ganancia[0], 0, True, 2)[0][0]}%")
    print(f"Rentabilidad obtenida: {numero_cientifico(rentabilidad_obtenida[0], 0, True, 2)[0][0]}%")
    
    return [monto_final, ganancia_obtenida, rentabilidad_obtenida, error_absoluto_final, error_porcentual_ganancia]

#A5 Mejor compra y mejor venta V
def mejor_compra_venta(monto_inicial = 1000000):
    # Cargamos los datos del CSV usando la funcion para obtener estos datos como np.arrays de tamaño 4
    datos_csv = cd.obtener_datos()

    # Sacamos los numeros redondeados y errores absolutos de cada mes, con dos cifras significativas 
    num_red_real_err_abs_rel = sacar_numero_redondeado_error_absoluto_relativo(datos_csv, cifras_significativas=2)
    nums_redondeados = num_red_real_err_abs_rel[2]

    # Sacamos el mejor precio de compra y el mejor precio de venta, junto con sus indices para poder imprimir el mes y año correspondiente.
    mejor_compra = min(nums_redondeados)
    mejor_venta = max(nums_redondeados)
    ind_mejor_compra = np.where (np.array(nums_redondeados) == mejor_compra)[0][0]
    ind_mejor_venta = np.where (np.array(nums_redondeados) == mejor_venta)[0][0]
    print("El mejor precio de compra se encuentra en el mes", datos_csv[ind_mejor_compra][1],"del año", datos_csv[ind_mejor_compra][0], "con un valor de: ", mejor_compra[0])
    print("El mejor precio de venta se encuentra en el mes", datos_csv[ind_mejor_venta][1],"del año", datos_csv[ind_mejor_venta][0], "con un valor de: ", mejor_venta[0])

    # Calculamos el resultado de comprar 1,000,000 de pesos chilenos en el mejor mes de compra y venderlos en el mejor mes de venta, junto con su error relativo total.
    resultado = evaluacion_compra_venta(monto_inicial, num_red_real_err_abs_rel[1], nums_redondeados, ind_mejor_compra, ind_mejor_venta)

    return resultado

if __name__ == "__main__":
    # Ejemplo de uso de las funciones
    representation_error()
    #eval_c_v= evaluacion_compra_venta()
    #cancelacion()
    #solo = variacion_anual()
    #mejor_compra_venta()
    #pass