# Generalidades

Basado en [este paper de la UCI (University of California, Irvine)](https://archive.ics.uci.edu/ml/datasets/wine+quality).


**Sobre la entrega:**
* La entrega deberá realizarla a través de correo electrónico a los correos xxxxxxxxxxxxxxxx
* Puede entregar más de un archivo, en tal caso sugerimos realizar un archivo comprimido zip conteniéndolos.
* Si lo prefiere, puede también subir todo el proyecto a un repositorio Github y compartir la URL al mismo.

* Se recomienda separar cada parte del desafío en un Notebook.

**Sobre el proyecto**
* Le ponemos como restricción al candidato utilizar el lenguaje Python
* Para el análisis de datos puede utilizar cualquier libreria Python, aunque recomendamos utilizar la biblioteca [Pandas](https://pandas.pydata.org/).
* Le pedimos al candidato que implemente todo el análisis utilizando Jupyter Notebook, Google Colab o similar.

# Guía para el desafío

## Parte 2 - Modelos Predictivos

El dataset de la segunda parte contiene ejemplos de características físicas y químicas, de algunos vinos de tipo Blanco y Tinto del conocido vino portugués "Vinho Verde". Estos ejemplos fueron luego catalogados por algunos expertos con un puntaje entre 0 (muy malo) y 10 (muy bueno). Se considera que un puntaje mayor a 6.5 es bueno.

### Dataset

Columnas del dataset:

* fixed acidity - Acidez fija.
* volatile acidity - Acidez volátil.
* citric acid - Ácido cítrico.
* residual sugar - Azúcar residual.
* chlorides - Clorhidratos.
* free sulfur dioxide - Dióxido de azufre libre.
* total sulfur dioxide - Dióxido de azufre total.
* density - Densidad.
* pH - Nivel de pH.
* sulphates - Sulfatos.
* alcohol - Alcohol.

**Variable dependiente**

* quality (score entre 0 y 10)

Algunas consideraciones:

* La acidez total y la acidez fija se determinan mediante valoración o mediante potenciometría. La acidez volátil, es la diferencia entre la acidez total y la acidez fija.
* El dióxido de azufre total ($TSO_2$) es la porción de $SO_2$ que está libre en el vino más la porción que está ligada a otros químicos en el vino, como aldehídos, pigmentos o azúcares.


### Se pide

1. Cargar el dataset con los datos de Vinos.
2. Inspeccionar los datos en el dataset y realizar un pequeño EDA (Exploratory Data Analysis/Profiling de la información) como hicimos en el curso.
3. Estudiar la correlación entre las columnas del dataset y la variable dependiente "quality".
4. Dividir el dataset entre 70 % train y 30 % test.
    1. Entrenar dos algoritmos de modelo de regresión sobre el conjunto de train
    2. Reportar $RMSE$ de los modelos para el conjunto de train
    3. Decidir cuál de los dos modelos es el mejor. Explique.
5. Reportar la métrica $RMSE$ sobre el conjunto de test para ambos modelos. ¿Se cumple qué el modelo elegido en 4 es mejor? Explique muy brevemente.
6. Ahora vamos a utilizar un enfoque de clasificación.
    1. Entrenar tres modelos de clasificación de los vistos en el curso sobre el conjunto de train.
    2. Reportar las métricas _precision, recall y f1-score_ utilizando el reporte de clasificación
    3. Decidir cuál de los modelos es el mejor. Explique
7. Reportar las métricas _precision, recall y f1-score_ sobre el conjunto de test. ¿Se cumple qué el modelo elegido en 6 es mejor? Explique muy brevemente.
8. ¿Cuál modelo de los que entrenó utilizaría? ¿Se le ocurre como comparar el modelo de regresión con los de clasificación? Explique muy brevemente utilizando los resultados obtenidos.

    
    
