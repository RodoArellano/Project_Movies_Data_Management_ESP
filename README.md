# Proyecto_Movies_1
En este proyecto se realizaron las siguientes tareas: 
1.- la limpieza y normalización de una base de datos de películas
2.- Siete funciones diferentes para recibir información específica (querys)
3.- Un análisis exploratorio de datos donde se identificaron los Outliers y comportamientos interesantes
4.- Se presentan las consultas en un entorno virtual utilizando FastAPI
5.- Y se crea un video.

1.- Por cuestiones de capacidad de memoria en mi cuenta Github solamente soy capaz de subir el archivo .csv ya trabajado. Dicho archivo cumple con las acciones requeridas para el MVP, pero además fue necesario eliminar columnas no utilizadas con la finalidad de reducir el peso del archivo. Dichas columnas fueron: 'tagline','original_language','runtime','overview' y 'status'.
Se puede encontrar el archivo en este repositorio con el nombre de 'complete_movies_and_credits.csv'.

2.- Las siete consultas/funciones disponibles son:
- cantidad_filmaciones_mes( Mes ): Se ingresa un mes en idioma Español y minúsculas. Mostrará la cantidad de películas que fueron estrenadas en el mes consultado.

- cantidad_filmaciones_dia( Dia ): Se ingresa un día en idioma Español, acentos y minúsculas, Mostrará la cantidad de películas que fueron estrenadas en el día. 

- score_titulo( titulo_de_la_filmación ): Se ingresa el título de una filmación y devolverá el título, el año de estreno y el score.

- votos_titulo( titulo_de_la_filmación ): Se ingresa el título de una filmación y devolverá como respuesta el título, la cantidad de votos y el valor promedio de las votaciones siempre y cuando la filmación cuente con más de 2000 valoraciones.

- get_actor( nombre_actor ): Se ingresa el nombre de un actor y devolverá el éxito del mismo medido, la cantidad de películas en las que ha participado y el promedio de retorno.

- get_director( nombre_director ): Se ingresa el nombre de un director y devolverá el éxito del mismo, el nombre de cada película con su fecha de lanzamiento, el retorno individual de la filmación, el costo individual y la ganancia de la misma.

- recomendacion( titulo ): Se ingresa el nombre de una película y se devuelve una lista de 5 películas similares que pueden interesarle al espectador.

3.- EDA (Análisis exploratorio de datos):

El análisis será referente al comportamiento e información de las columnas 'popularity' y 'budget':
Como podemos obserbar en la primera imagen mostrada a continuación, se tiene una agrupación en la parte inferior de la gráfica, esto se debe a la presencia de outliers, es decir datos que se salen del comportamiento estandar y afectan a las mediciones. En este caso no se analizará si es o no un error, porque puede que sean correctos y una anomalía.

![Scatter1_with_outliers](https://github.com/RodoArellano/Proyecto_Movies_1/assets/125421658/588e14f9-0c51-45f9-bff6-cf07e27bc204)

Para tener un mejor análisis se presenta la misma gráfica sin tomar en cuenta los outliers de 'popularity':

![Scatter1_without_outliers](https://github.com/RodoArellano/Proyecto_Movies_1/assets/125421658/4a9e53db-8eb1-4576-9e4b-a13aaa5426c0)

Ahora podemos observar una agrupación más extendida, de la cual podemos notar que la cantidad invertida en 'budget' en realidad no es directamente proporcional a la popularidad de la filmación.

Ahora, si analizamos las siguientes 2 imagenes podremos ver que la mayoría de las valoraciones se encuentran más cercanas a las películas sin presupuesto registrado en la base de datos (budget = 0). Debido a esto podemos concluir que a menos que descartemos las películas sin registro de presupuesto no vamos a tener una relación certera entre la popularidad y el presupuesto.

![Scatter1_without_outliers_grouped](https://github.com/RodoArellano/Proyecto_Movies_1/assets/125421658/1603a7d5-e44f-4cd8-ae5a-faa77ba62d36)
![Popularity_density](https://github.com/RodoArellano/Proyecto_Movies_1/assets/125421658/2354a631-731a-4d4a-89ab-773a166e0b0a)

Dicho esto, si procedieramos a ignorar dichas películas nuestra base de datos perdería la mayoría de sus registros.

Una forma de demostrar que la tendencia es regida por la gran cantidad de registros en 0, es calculando la media:

![mean_budget_popularity](https://github.com/RodoArellano/Proyecto_Movies_1/assets/125421658/2f0d9091-ba70-46ba-8603-d9dde24062c4)

Como podemos observar, la media de 'popularity' a pesar de tener valores que llegan a los 50 puntos se encuentra muy cercana a 0. Mismo caso con la media de 'budget'. En conclusión es necesario completar la información, o comenzar a analizar desde dónde ya se comienza a registrar correctamente, lo que nos lleva a incluir una liena del tiempo anual de los registros.

En las 2 siguientes imágenes podemos observar el comportamiento anual de los registros:

![Budget_trough_years](https://github.com/RodoArellano/Proyecto_Movies_1/assets/125421658/cab82ea7-0012-449b-922c-cf213678f019)

budget: Se concluye que a partir del año 2000 D.C la base de datos ah sido llenada de forma más completa, obteniendo así el presupuesto de la mayoría de las películas estrenadas. Una propuesta para predecir un comportamiento sería entrenar con la información que se tiene de budget solamente después del año 2000.

![Popularity_trough_years](https://github.com/RodoArellano/Proyecto_Movies_1/assets/125421658/61456889-87ea-470a-beb3-4e45cf000bd0)

popularity: Podemos concluir que al paso de los años tenemos una tendencia creciente en la popularidad de las películas, es decir que se están produciendo más películas que la audiencia opina son de alta calidad.

