from fastapi import FastAPI
import numpy as np
import pandas as pd

#df_complete = pd.read_csv(r'C:\Users\rodal\Documents\Henry_DS_FT_11\Course_HW\Proyecto_Movies_1\ETL_Project_1\complete_movies_and_credits_db.csv', sep=',')
df_complete = pd.read_csv('https://github.com/RodoArellano/Proyecto_Movies_1/blob/main/complete_movies_and_credits.csv', sep=',')

app = FastAPI()

@app.get('/')
def index():
    return {'instrucciones':'Las opciones de consulta son las siguientes'
            ,'1':'cantidad_filmaciones_dia/dia'
            ,'2':'cantidad_filmaciones_mes/mes'
            ,'3':'score_titulo/pelicula_por_buscar'
            ,'4':'votos_titulo/pelicula_por_buscar'
            ,'5':'get_actor/nombre_actor'
            ,'6':'get_director/nombre_director'
            ,'7':'recomendación/pelicula_por_buscar'} 
#\n 1.-/cantidad_filmaciones_mes/mes_a_buscar 2.-/cantidad_filmaciones_mes/mes_a_buscar'

# Función 1
@app.get('/cantidad_filmaciones_mes/''{mes}')
async def cantidad_filmaciones_mes(mes):

    filtered_values = df_complete.loc[df_complete['release_month'] == mes, 'title'].tolist()
    count_values = len(filtered_values)

    return f'En el mes de {mes} se han estrenaron {count_values} películas.'

# Función 2
@app.get('/cantidad_filmaciones_dia/''{dia}')
async def cantidad_filmaciones_dia(dia):

    filtered_values = df_complete.loc[df_complete['release_day'] == dia, 'title'].tolist()
    count_values = len(filtered_values)

    return f'En el dia {dia} se han estrenado {count_values} películas.'

# Función 3
@app.get('/score_titulo/''{titulo}')
async def score_titulo(titulo):

    filtered_year = df_complete.loc[df_complete['title'] == titulo, 'release_year'].tolist()
    filtered_score = df_complete.loc[df_complete['title'] == titulo, 'popularity'].tolist()

    filtered_year = filtered_year[0]
    filtered_score = filtered_score[0]

    return f'la pelicula {titulo} fue estrenada el año {filtered_year} con una calificación/popularidad de {filtered_score}'

# Función 4
@app.get('/votos_titulo/''{titulo}')
async def votos_titulo(titulo):

    filtered_votes = df_complete.loc[df_complete['title'] == titulo, 'vote_count'].tolist()
    filtered_avg_votes = df_complete.loc[df_complete['title'] == titulo, 'vote_average'].tolist()

    filtered_votes = filtered_votes[0]
    filtered_avg_votes = filtered_avg_votes[0]

    if filtered_votes >= 1:
        if filtered_votes >= 2000:
            return f'la pelicula {titulo} cuenta con un total de {filtered_votes} valoraciones quedando con una calificación promedio de {filtered_avg_votes}'
        else:
            return f'Este título no cuenta con los votos suficientes para considerar el resultado confiable no se entregará la calificación promedio.'
    else:
        return f'Este titulo no se encuentra en la base de datos, favor ingresar otro título'

# Función 5
@app.get('/get_actor/''{nombre_actor}')
async def get_actor(nombre_actor):

    # Encuentro los valores de return para el actor y remplazo los infinitos por nan, así ya puedo hacer operaciones matemáticas.
    filtered_return = df_complete[df_complete['cast'].apply(lambda x: nombre_actor in x)]['return']
    filtered_return = filtered_return.replace([np.inf, -np.inf], np.nan)
    sum_return = filtered_return.sum()
    # Encuentro las peliculas totales donde aparece el actor, y también las mismas películas pero donde el valor de 'return' no es infinito
    all_actor_movies = df_complete.loc[df_complete['cast'].apply(lambda x: nombre_actor in x)]['title']
    filtered_not_inf_movies = df_complete.loc[(df_complete['cast'].apply(lambda x: nombre_actor in x)) & (~np.isinf(df_complete['return']))]['title']
    # Ahora puedo mostrar el número total, y utilizar el número correcto para el promedio, ya que no utilizaré los infinitos.
    count_all_movies = len(all_actor_movies)
    count_not_inf_movies = len(filtered_not_inf_movies)
    # el promedio utiliza la cantidad de películas sin valores inf
    avg_return = sum_return/(count_not_inf_movies)

    return f'el actor {nombre_actor} ha participado en {count_all_movies} filmaciones. Lleva un exito de retorno total igual a {sum_return}, y con un promedio de retorno de {avg_return}'

# Función 6
@app.get('/get_director/''{nombre_director}')
async def get_director(nombre_director):

    # Encuentro los valores de return para el actor y remplazo los infinitos por nan, así ya puedo hacer operaciones matemáticas.
    filtered_return = df_complete[df_complete['directors'].apply(lambda x: nombre_director in x)]['return']
    filtered_return = filtered_return.replace([np.inf, -np.inf], np.nan)
    sum_return = filtered_return.sum()
    # Encuentro las peliculas totales donde aparece el actor, y también las mismas películas pero donde el valor de 'return' no es infinito
    all_director_movies = df_complete.loc[df_complete['directors'].apply(lambda x: nombre_director in x)]['title']
    filtered_not_inf_movies = df_complete.loc[(df_complete['directors'].apply(lambda x: nombre_director in x)) & (~np.isinf(df_complete['return']))]['title']
    # Ahora puedo mostrar el número total, y utilizar el número correcto para el promedio, ya que no utilizaré los infinitos.
    count_all_movies = len(all_director_movies)
    count_not_inf_movies = len(filtered_not_inf_movies)

    # Create a new DataFrame with the desired columns
    filtered_df = df_complete.loc[df_complete['directors'].apply(lambda x: nombre_director in x)]
    result_table = pd.DataFrame()
    result_table['Título'] = filtered_df['title']
    result_table['Exito_film'] = filtered_df['return']
    result_table['Costo'] = filtered_df['budget']
    result_table['Ganancia'] = filtered_df['revenue']

    return f'El director {nombre_director} a producido {count_all_movies} películas y tiene un exito total de {sum_return}. \nTabla "Análisis de películas del director {nombre_director}"\n{result_table.to_string(index=False)}'

# Función 7
@app.get('/recomendacion/''{titulo}')
async def recomendacion(titulo):
    filtered_title = df_complete.loc[df_complete['title'] == titulo, 'genres'].tolist()
    filtered_score = df_complete.loc[df_complete['genres'].apply(lambda x: filtered_title[0] in x), 'popularity'].tolist()
    top_scores = sorted(filtered_score, reverse=True)[:6]
    filtered_movies = df_complete.loc[(df_complete['popularity'].isin(top_scores)) & (df_complete['title'] != titulo), 'title'].head(5).tolist()

    return f'Como te gustó {titulo}, 5 recomendaciones de películas que también te pueden gustar son: {filtered_movies}'

