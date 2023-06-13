# Proyecto_Movies_1
En este proyecto se realizaron las siguientes tareas: 
1.- la limpieza y normalización de una base de datos de películas
2.- Siete funciones diferentes para recibir información específica (querys)
3.- Un análisis exploratorio de datos donde se identificaron los Outliers y comportamientos interesantes
4.- Y al final se presentan las consultas en un entorno virtual utilizando FastAPI

1.- Por cuestiones de capacidad de memoria en mi cuenta Github solamente soy capaz de subir el archivo .csv ya trabajado. Dicho archivo cumple con las acciones requeridas para el MVP, pero además fue necesario eliminar columnas no utilizadas con la finalidad de reducir el peso del archivo. Dichas columnas fueron: 'tagline','origin_language','runtime','overview' y 'status'.
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

![Scatter1_with_outliers](https://github.com/RodoArellano/Proyecto_Movies_1/assets/125421658/588e14f9-0c51-45f9-bff6-cf07e27bc204)

![Scatter1_without_outliers](https://github.com/RodoArellano/Proyecto_Movies_1/assets/125421658/4a9e53db-8eb1-4576-9e4b-a13aaa5426c0)

![Scatter1_without_outliers_grouped](https://github.com/RodoArellano/Proyecto_Movies_1/assets/125421658/1603a7d5-e44f-4cd8-ae5a-faa77ba62d36)

![mean_budget_popularity](https://github.com/RodoArellano/Proyecto_Movies_1/assets/125421658/2f0d9091-ba70-46ba-8603-d9dde24062c4)

![Popularity_density](https://github.com/RodoArellano/Proyecto_Movies_1/assets/125421658/2354a631-731a-4d4a-89ab-773a166e0b0a)

![Budget_trough_years](https://github.com/RodoArellano/Proyecto_Movies_1/assets/125421658/cab82ea7-0012-449b-922c-cf213678f019)

![Popularity_trough_years](https://github.com/RodoArellano/Proyecto_Movies_1/assets/125421658/61456889-87ea-470a-beb3-4e45cf000bd0)
