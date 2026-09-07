import numpy as np
import matplotlib.pyplot as plt
import cargar_datos as cd
import errores as er
#A3 Cancelación (dos meses casi iguales)
def cancelacion():
    #Obtendremos los datos que hay en el csv usando la funcion obtener_datos del archivo cargar_datos.py
    datos_csv = cd.obtener_datos()

    #Obtenemos los numeros redondeados, errores absoluto, relativos y el numero real
    num_red_real_err_abs_rel = er.sacar_numero_redondeado_error_absoluto_relativo(datos_csv)

    #Para este apartado usaremos noviembre 2022 y mayo 2024
    dolar_nov_22 = np.round(num_red_real_err_abs_rel[3][10])
    dolar_may_24 = np.round(num_red_real_err_abs_rel[3][28])

    #Sacaremos la variacion entre estos meses, al igual que el error absoluto de cada mes
    delta_p = er.variacion_entre_meses(dolar_nov_22, dolar_may_24)
    error_abs_nov = er.error_absoluto(num_red_real_err_abs_rel[3][10], dolar_nov_22)
    error_abs_may = er.error_absoluto(num_red_real_err_abs_rel[3][28] , dolar_may_24)

    #Calcularemos el error propagado, sumando los dos errores absolutos, dejaremos el resultado con 3 cifras
    error_propagados = np.round((np.round(error_abs_nov, 3) + np.round(error_abs_may, 3)), 3)
    print(f"ΔP {delta_p} ± {error_propagados}, su error porcentual es {(error_propagados / delta_p) * 100}%")

    er.registrar_evaluacion_error(
        par_puntos="Variacion noviembre 2022 y mayo 2024",
        anio="2022-2024",
        error_absoluto=f"{error_abs_nov:.2f} y {error_abs_may:.2f}",
        error_relativo="N/A",
        error_propagado= error_propagados
    )
    # Zona de Grafico de Barras
    meses_x = ["+", "ΔP", "-"]
    valores_y = [np.float64(delta_p + error_propagados), np.float64(delta_p), np.float64(delta_p - error_propagados)]
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(meses_x, valores_y, color='skyblue', edgecolor='black')

    ax.set_xlabel('Variación del ΔP')
    ax.set_ylabel('Error')
    ax.set_title('Variación mes a mes ΔP')
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()


#A4 Anualidad (variacion enero -> diciembre) V
def variacion_anual():
    #Obtenemos los datos del CSV usando la funcion de obtener_datos de el archivo cargar_datos.py
    datos_csv = cd.obtener_datos()

    # Obtenemos el numero redondeado, error absoluto, error relativo y el numero real.
    num_red_real_err_abs_rel = er.sacar_numero_redondeado_error_absoluto_relativo(datos_csv)
    errores_absolutos = num_red_real_err_abs_rel[0]
    precios_redondeados = num_red_real_err_abs_rel[2]
    errores_propagado = []
    errores_relativos_totales = []
    #Recorreremos la lista de los precios redondeados saltando de a 12 meses, llendo de enero a diciembro
    for i in range(0, len(precios_redondeados), 12):
        precio_enero = precios_redondeados[i]
        precio_diciembre = precios_redondeados[i+11]
        resultado_resta, error_propagado, error_relativo_total = er.propagacion_resta(precio_enero, precio_diciembre, errores_absolutos[i], errores_absolutos[i+11])
        errores_propagado.append(error_propagado)
        errores_relativos_totales.append(error_relativo_total)
    #Buscaremos el maximo error porcentual
    max_er_relativo = max(errores_relativos_totales)
    #Buscaremos el indice del valor maximo, para obtener el año y el mes del error porcentual
    ind_max_er_relativo = errores_relativos_totales.index(max_er_relativo)
    print("El error relativo máximo se encuentra entre el mes enero del año", datos_csv[ind_max_er_relativo*12][0], "y el mes diciembre del año", datos_csv[ind_max_er_relativo*12+11][0], "con un valor de: ", max_er_relativo*100, "%")
    return errores_absolutos, errores_relativos_totales

if __name__ == "__main__":
#Zona de uso de las funciones, solo desmarcar la que se requiera usar.
    #cancelacion()
    #variacion_anual
    #er.exportar_csv_evaluacion("./data/evaluacion_errores.csv")
    pass