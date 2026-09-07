import numpy as np
import matplotlib.pyplot as plt
import cargar_datos as cd
import errores as er

#A3 Cancelación (dos meses casi iguales)
def cancelacion():
    datos_csv = cd.obtener_datos()
    num_red_real_err_abs_rel = er.sacar_numero_redondeado_error_absoluto_relativo(datos_csv, cifras_significativas=3)
    errores_absolutos = num_red_real_err_abs_rel[0]
    errores_relativos = num_red_real_err_abs_rel[1]
    error_absolutos = []
    error_relativos = []
    for i in range(len(num_red_real_err_abs_rel[2])-1):
        precio_mes_actual = num_red_real_err_abs_rel[2][i]
        precio_mes_siguiente = num_red_real_err_abs_rel[2][i+1]
        resultado_resta, error_propagado, error_relativo_total = er.propagacion_resta(precio_mes_actual, precio_mes_siguiente, errores_absolutos[i], errores_absolutos[i+1])
        error_absolutos.append(error_propagado)
        error_relativos.append(error_relativo_total)
        print("año:", datos_csv[i][0], "precio_mes_actual: ", precio_mes_actual, "precio_mes_siguiente: ", precio_mes_siguiente, "resultado_resta: ", resultado_resta, "error_propagado: ", error_propagado, "error_relativo_total: ", error_relativo_total)
    max_er_relativo = max(errores_relativos)
    ind_max_er_relativo = errores_relativos.index(max_er_relativo)
    print("El error relativo máximo se encuentra entre el mes", datos_csv[ind_max_er_relativo][1],"del año", datos_csv[ind_max_er_relativo][0], "y el mes", datos_csv[ind_max_er_relativo+1][1],"del año", datos_csv[ind_max_er_relativo+1][0], "con un valor de: ", max_er_relativo*100, "%")
    return errores_absolutos, errores_relativos


#A4 Anualidad (variacion enero -> diciembre) V
def variacion_anual():
    datos_csv = cd.obtener_datos()
    num_red_real_err_abs_rel = er.sacar_numero_redondeado_error_absoluto_relativo(datos_csv, cifras_significativas=2)
    errores_absolutos = num_red_real_err_abs_rel[0]
    precios_redondeados = num_red_real_err_abs_rel[2]
    errores_propagado = []
    errores_relativos_totales = []
    for i in range(0, len(precios_redondeados), 12):
        precio_enero = precios_redondeados[i]
        precio_diciembre = precios_redondeados[i+11]
        resultado_resta, error_propagado, error_relativo_total = er.propagacion_resta(precio_enero, precio_diciembre, errores_absolutos[i], errores_absolutos[i+11])
        errores_propagado.append(error_propagado)
        errores_relativos_totales.append(error_relativo_total)
        #print("precio_enero: ", precio_enero, "precio_diciembre: ", precio_diciembre, "resultado_resta: ", resultado_resta, "error_propagado: ", error_propagado, "error_relativo_total: ", error_relativo_total)
    max_er_relativo = max(errores_relativos_totales)
    ind_max_er_relativo = errores_relativos_totales.index(max_er_relativo)
    print(errores_relativos_totales)
    errores_relativos_totales = sorted(errores_relativos_totales)
    print("El error relativo máximo se encuentra entre el mes enero del año", datos_csv[ind_max_er_relativo*12][0], "y el mes diciembre del año", datos_csv[ind_max_er_relativo*12+11][0], "con un valor de: ", max_er_relativo*100, "%")
    print(errores_relativos_totales) #Lo que tienen en comun entre los años pocos confiables son que estos tienen es que el valor con el que inician el año tienen una diferencia mayor con respecto a como terminan.
    return errores_absolutos, errores_relativos_totales