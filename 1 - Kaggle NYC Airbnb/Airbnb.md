# Generalidades

Basado en [este challenge de kaggle](https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data).


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

## Pate 1 - Calidad de datos

La idea de esta parte es demostrar de forma práctica, conceptos de calidad y limpieza de datos sobre el dataset provisto. El mismo cuenta con 48895 registros de publicaciones de hospedajes en la plataforma AirBnB para la ciudad de Nueva York.

El hipotético cliente pretende una vez finalizada la limpieza de datos construir un reporte por barrio de los precios de los hospedajes.

### Dataset

Columnas del dataset:

* id - Identificador de la publicación
* name - Nombre de la publicación
* host_id - Identificador del usuario que hizo la publicación
* host_name - Nombre del usuario que hizo la publicación
* neighbourhood_group - Región geográfica de la ciudad
* neighbourhood - Barrio
* latitude - Latitud
* longitude - Longitud
* room_type - Tipo de habitación 
* price - Precio en dólares
* minimum_nights - Mínima cantidad de noches
* number_of_reviews - Cantidad de revisiones
* last_review - Fecha de la última revisión
* reviews_per_month - Cantidad promedio de revisiones por mes
* calculated_host_listings_count - Cantidad de publicaciones estimadas del usuario
* availability_365 - 

### Se pide

1. Cargar el dataset con los datos de AirBnB disponibles para los hospedajes de NYC.
2. Inspeccionar los vacios en el dataset:
    1. Verificar el tipo de datos de cada columna luego de cargada
    2. Contar la cantidad de vacíos, ceros y valores especiales por columna
    3. Indicar qué columnas tienen vacíos y como se podrían reparar
    4. Modificar las columnas con los datos corregidos
3. Inspeccionar el campo de precio:
    1. Verificar valores extraños en la columna precio
    2. Modificar la columna de precio con los valores corregidos
4. Generar un reporte gráfico con los precios por barrios/zonas de la ciudad.
    1. Generar una visualización gráfica de los precios
    2. Generar estadísticas por barrio, precio máximo, mínimo, promedio, mediano
    3. Generar estadísticas por grupos de barrios, precio máximo, mínimo, promedio, mediano
    4. ¿Cuál es la completitud de los datos que pudo utilizar para las últimas dos partes? ¿Puede mejorarla de alguna manera? 

