Tu tarea es crear una API que permita obtener la fecha actual en dos formatos distintos: larga y corta. El formato de la fecha debe ser determinado por la presencia del parámetro booleano 'formato_largo' en un request POST. Si el valor de este parámetro es True, la respuesta debe devolver la fecha en formato largo YMDHMS. Si el valor es False, la respuesta debe devolver la fecha en formato corto YDM. 

Además, la API debe contar el número de veces que se hizo una llamada a ella y ese número debe ser devuelto en una respuesta GET.

Puedes usar FastAPI o Flask, y puedes usar cualquier librería de Python que te ayude a resolver el problema.