# Laboratorio 1: La ganancia que se evapora


## Respuestas a Preguntas del Error

**A1. Error de representación mes a mes**
Redondeamos todas las cifras con la fórmula = (round(valor real/10))*10 asi se nos redondea de manera exitosa, con esto en mente, nuestro mejor resultado fue: 
 **Abril de 2022**. 
*   **Valor real (en csv):** $815.12, **Valor aprox (redondeado) $820, **Absoluto:** $4.88, **Relativo:** 0.59%

**A2. Evaluación entre dos puntos (una compra-venta)**
se simuló la mejor compra y la mejor venta posible que podiamos hacer con los meses: **Febrero 2023**: $800 de compra y la venta en **Enero 2025**: $1000 de venta, tomando en cuenta que nuestra M que es el capital inicial debe ser 1 millon de pesos, nuestra simulación quedaria de esta manera: 
*   **Compra:** $1.000.000 / 800 = 1.250, **Venta:** 1.250* 1000 = $1.250.000, **Ganancia:** $250.000, **Propagado:** 
el error relativo de la compra fue 0.21%  y la venta fue 0.07%, dando como resultado un error relativo de 0.28%

*   **Finalmente para sacar el error relativo por medio de la ganancia ocupamos :** error_absoluto = 1250000 * (0.28 / 100), con esto nos da que el error relativo es 3.500$, y el error porcentual de ganancia es 1.4%

**A3. Cancelación (dos meses casi iguales)**
nosotros elegimos los meses: Noviembre 2022 (917.05) y Mayo 2024 (917.88) para probar este ejercicio:
*   **en 3 cifras** : el error absoluto de noviembre es 0.05 pesos y el de mayo es 0.12 pesos
*   **La Variación vendria siendo:** 918 - 917 = 1 peso
*   **La suma de errores absolutos es:** 0.05 + 0.12 = 0.17 pesos
*   **Error porcentual %:** (0.17 / 1.0) x 100 = 17%.
*   **Finalmente:** entonces podemos afirmar exitosamente que el dolar subió

**A4. Anualidad (variación enero a diciembre)**
Calculamos los errores porcentuales de enero y diciembre de cada año respectivamente y nos arrojaron estos resultados:
1.  **2022:** enero (822.05) -> 820 diciembre (875.66) -> 880, variacion : 880 - 820 = 60 pesos, error propagado : enero (2.04) diciembre (4.34), error porcentual: (6.39 / 60) * 100 = 10.65%
2.  **2023** : enero (826.34) -> 830 diciembre (874.67) -> 870, variacion : 870 - 830 = 40.00 pesos, error propagado : enero (3.66) diciembre (4.67), error porcentual: (8.33 / 40) * 100 = 20.82%
3.  **2024**: enero (907.99) -> 910 diciembre (982.30) -> 980, variacion : 980 - 910 = 70.00 pesos, error propagado : enero (2.01) diciembre (2.30), error porcentual: (4.31 / 70) * 100 = 6.16%
4.  **2025**: enero (1000.76) -> 1000 diciembre (916.16) -> 920, variacion : 920 - 1000 = -80.00 pesos, error propagado : enero (0.76) diciembre (3.84), error porcentual: (4.60 / 80) * 100 = 5.75%
*   **¿Qué tienen en común los años poco confiables?:** que algo que no se pensaba es que cuando tenemos errores pequeños osea una variación pequeña el "pequeño error" matematico toma un protagonismo grande cuando estamos ya en el toque final que es el porcentaje final.

**A5. Mejor compra y mejor venta**
*   **Mejor compra:** Febrero 2023 ($798.26).
*   **Mejor Venta:** Enero 2025 ($1000.76).
*   **¿La conclusión sobrevive al error?:** la rentabilidad de $250.000 es mucho mas que el error de $3.675, asi que es super buen plan


---

## 7. Respuestas a Preguntas del Punto Flotante (Sección B)

**B1. Cifras significativas = mantisa corta**
es como usar una mantisa corta porque estamos haciendo restricciones de memoria importantes, ya que, estamos diciendole al sistema que deseche datos con detalle como lo son los decimales, por ejemplo con 1000.76 obligamos a guardar solamente 1000, entonces ese 0.76 se elimina, entonces finalmente no tenemos la información completa por falta de espacio.


**B2. La ida y vuelta que no vuelve**
Aqui es como que fueras a comprar dolares y luego vuelves de inmediato a venderlos, cuando utilizamos los datos de memoria float32, el millon de pesos que originalmente podiamos poner no se va a recuperar sin ningun cambio, porque se hará un recorte decimal y eso afectará finalmente al precio, porque estamos calculando con una calculadora más basica, no así como ocurre con float64 que sí guarda mas infromación.

**B4. Cancelación en la máquina**
Al ejecutar la operación (874.67 - 875.66) utilizando distintas precisiones en Python:
*   **Resultado en float32:** `-0.98999023`
*   **Resultado en float64:** `-0.99000000`
El formato de 32 bits (calculadora basica) introduce decimales basura al final.
---

## Estructura del Repositorio
*   `data/`: Contiene el archivo CSV original del SII.
*   `src/`: Contiene los scripts en Python (`cargar_datos.py`, `errores.py`, `anualidad.py`, `punto_flotante.py`).
*   `graficos/`: Imágenes PNG generadas con Matplotlib evidenciando la deriva y el error.
*   `INFORME.md`: Documento final con la evaluación financiera de cuándo comprar y vender.