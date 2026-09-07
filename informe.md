# Universidad Católica del Maule
## Ingeniería Civil Informática
### Computación Numérica S2 [INF]

# Laboratorio Computación numérica: punto flotante
**Cancelación y propagación del error con el dólar observado del SII (2022-2025)**

**Integrantes:** Catalina Ibáñez Mondaca y Carlos Granda 
**Profesor:**  Juan Manuel Contardo
**Fecha:** 09/09/2026  

---

## 1. Introducción y Metodología
Este laboratorio se basa en analizar el comportamiento que tuvo el dólar, pero sometiéndolo a restricciones numéricas, exactamente de precisión. limitamos los valores a una pequeña reducción de cifras significativas, siendo estas cifras las más confiables cuando se trata de precisión numérica. Simularemos cómo se comporta un computador con una mantisa corta (que viene siendo el punto flotante).

Nuestro objetivo como equipo es identificar como estos errores se van esparciendo mediante operaciones aritméticas en las cuales tenemos: multiplicación, división y resta.
Todas las compras tienen un monto base de $1.000.000 de pesos chilenos.

## 2. Análisis del Error
Cuando obligamos al computador a usar solamente 2 cifras significativas es como pedirle que memorice el precio del dólar, pero muy poco detallado, entonces lo demás lo tomará como "basura" que son los detalles más pequeños, imaginemos que el computador tiene que tomar 563 porque el dólar cuesta esto, el computador retendrá en su memoria 560, y esa pequeña diferencia es lo que se le llama como Error absoluto, es por eso por lo que en nuestro trabajo identificaremos en que mes el computador cometió el peor error absoluto al hacer el pequeño recorte, en este caso no solo veremos el error en pesos, sino que también, el error relativo que es en este caso el mes que representó un porcentaje grave respecto al precio del dólar de verdad.

## 3. Fenómenos de Cancelación e Incertidumbre
La cancelación ocurre cuando restamos dos precios que claramente son casi iguales, al venir arrastrando pequeños errores de antes por haber recortado números como vimos en el ítem anterior, al restar estos números queda la parte de la basura del redondeo flotando.
el margen de error termina siendo más grande que la propia variación del dólar, que ocurre con esto?, el resultado se vuelve inusable, porque la incertidumbre es tan alta que no es posible afirmar si es que el dólar realmente subió o bajo.

| Año | ΔP Calculado (Pesos) | Error Propagado (±) | Confiabilidad |
| :--- | :--- | :--- | :--- |
| 2024 | 70.00 | 4.31 | Alta (Error ~6.1%) |
| 2025 | -80.00 | 4.60 | Alta (Error ~5.7%) |
| 2022 | 60.00 | 6.39 | Media (Error ~10.6%) |
| 2023 | 40.00 | 8.33 | Baja (Error ~20.8%) |


## 4. Conclusiones y Respuestas

**1.- ¿Cuándo conviene comprar? ¿En qué mes estuvo más barato el dólar, y qué tan seguro es ese mínimo frente a los meses vecinos (¿la diferencia supera el error o cae dentro de él?)?**
**R:** el mejor mes para comprar es febrero de 2023 ahí ocurrió el minimo de todos los datos $798.26, cuando redondeamos a 2 cifras, el valor queda en $800 con un error absoluto de $1.74, y un vecino puede ser Marzo de 2023 con $809.50, tienen una diferencia de 11 pesos, por lo tanto, febrero fue el mejor mes para comprar.

**¿Cuándo conviene vender? ¿En qué mes estuvo más caro, con el mismo análisis de confianza?**
**R:** conviene vender en enero de 2025 porque ahí el dolar registró un maximo de $1000.76, cuando la guardamos con 2 cifras se queda en $1000 igualmente porque tendriamos un error de $0.76, el vecino cercano fue diciembre 2024 $982.30.

**La mejor jugada completa: comprar en el mes X y vender en el mes Y — indica la rentabilidad con su error. ¿Es una recomendación sólida?**
**R:** la mejor jugada es comprar en febrero 2023 y vender en enero 2025, eso lo podemos ver en el desarrollo de A2 pero basicamente tenemos estos calculos: 

**La mejor compraventa**
se simuló la mejor compra y la mejor venta posible que podiamos hacer con los meses: **Febrero 2023**: $800 de compra y la venta en **Enero 2025**: $1000 de venta, tomando en cuenta que nuestra M que es el capital inicial debe ser 1 millon de pesos, nuestra simulación quedaria de esta manera: 
*   **Compra:** $1.000.000 / 800 = 1.250, **Venta:** 1.250* 1000 = $1.250.000, **Ganancia:** $250.000, **Propagado:** 
el error relativo de la compra fue 0.21%  y la venta fue 0.07%, dando como resultado un error relativo de 0.28%

*   **Finalmente para sacar el error relativo por medio de la ganancia ocupamos :** error_absoluto = 1250000 * (0.28 / 100), con esto nos da que el error relativo es 3.500$, y el error porcentual de ganancia es 1.4%

por lo que aseguramos una ganancia de $250.000 con esta jugada.

*   **Los tramos donde NO se puede recomendar: nombra al menos un par de meses (o un año) donde la variación es tan chica frente al error que cualquier afirmación sobre subir o bajar sería irresponsable.**
**R:** por ejemplo no se recomienda en diciembre 2022 $875.66 y diciembre de 2023 $874.67, al tener una variacion real del precio tan minima como lo es 1 peso tenemos falta de precisión, como los valores son tan parecidos se anulan entre sí, entonces no sabremos exactamente si es que el dolar subió o bajó y no podemos regirnos solamente por incertidumbre.

*   **La lección de método: en una frase, ¿qué aprendiste sobre confiar en una “diferencia” cuando viene de restar dos números grandes y parecidos?**
**R:** Restar dos números grandes y que son prácticamente casi iguales es muy peligroso en términos de computación, porque los datos reales de las finanzas se anulan entre sí y el resultado final queda totalmente dominado por los errores de redondeo que traía el computador.