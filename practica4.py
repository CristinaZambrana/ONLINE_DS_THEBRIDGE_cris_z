import numpy as np
import pandas as pd

titulos = ["Toy Story 4", "Los Incríbles 2", "Buscando a Dory", "Toy Story 3", "Caco", "Inside Out", "Monsters University", "Up"]
lanzamiento = [2015, 2018, 2016, 2010, 2017, 2015, 2013, 2006]
recaudaciones = [1073, 1242, 1029, 1067, 807, 857, 744, 735]  # En millones de dólares
espectadores = [74.91, 93.42, 76.72, 81.35, 62.75, 68.27, 54.74, 54.34] # En millones, estimación hecha por aficionados

#Apartado 1
#Creamos las tres series pandas 
series_lanzamiento = pd.Series(lanzamiento, index=titulos, name='Lanzamiento')
print(f"Series de Lanzamiento: {series_lanzamiento}")
series_recaudaciones = pd.Series(recaudaciones, index=titulos, name='Recaudaciones')
print(f"Series de Recaudaciones: {series_recaudaciones}")
series_espectadores = pd.Series(espectadores, index=titulos, name='Espectadores')
print(f"Series de Espectadores: {series_espectadores}")

#Apartado 2
series_recaudaciones = pd.Series(recaudaciones, index=titulos, name='Recaudaciones ')

recaudaciones_ascendente = series_recaudaciones.sort_values(ascending=True) #ordenamos la serie a mayor
print(f"Recaudaciones Ordenadas menor-mayor: {recaudaciones_ascendente}")

recaudaciones_descendente = series_recaudaciones.sort_values(ascending=False) #ordenamos la serie a menor
print(f"Recaudaciones Ordenadas mayor-menor: {recaudaciones_descendente}")

#Apartado 3
for pelicula, recaudacion in series_recaudaciones.items():
    
    lanzamiento_pelicula = lanzamiento[series_recaudaciones.index.get_loc(pelicula)] #devuelve la posicion del indice, 
    espectadores_pelicula = espectadores[series_recaudaciones.index.get_loc(pelicula)]
    precio_entrada = recaudacion / espectadores_pelicula

    print(f"Película: {pelicula}")
    print(f"Recaudación: ${recaudacion} millones")
    print(f"Año de lanzamiento: {lanzamiento_pelicula}")
    print(f"Número de espectadores: {espectadores_pelicula} millones")

#Apartado 4
pelicula_menor_recaudacion = series_recaudaciones.idxmin()

año_menor = lanzamiento[series_recaudaciones.index.get_loc(pelicula_menor_recaudacion)]
print(f"La película con menor recaudación fue '{pelicula_menor_recaudacion}' y es del año {año_menor}.")

peliculas_condiciones = series_recaudaciones[(series_recaudaciones > 1000) & (espectadores_pelicula < 75)]
pelicula_condiciones = peliculas_condiciones.index[0]
print(f"La película con más de 1000 millones de recaudación y menos de 75 millones de espectadores es '{pelicula_condiciones}'.")

gonzalo = 30

años_vistas = [lanzamiento[series_recaudaciones.index.get_loc(pelicula)] + (gonzalo - 1) for pelicula in series_recaudaciones.index]

for i, pelicula in enumerate(series_recaudaciones.index):
    print(f"Gonzalo fue a ver '{pelicula}' con {gonzalo} años en el año {años_vistas[i]}.")

#Apartado 5

series_lanzamiento["Toy Story 4"] = 2019
series_lanzamiento["Up"] = 2009

series_recaudaciones["Monsters University"] = 754

nuevos_titulos = [titulo.replace("Jaime", "Jaime Corregido") for titulo in titulos]

series_lanzamiento.index = nuevos_titulos #Actualizar indices
print(f"Series de Lanzamiento: {series_lanzamiento}")
series_recaudaciones.index = nuevos_titulos
print(f"Series de Recaudaciones: {series_recaudaciones}")
series_espectadores.index = nuevos_titulos
print(f"Series de Espectadores: {series_espectadores}")

#PARTE II
#Creamos el dataframe con las series de antes pero de indice peliculas
data = {'Lanzamiento': series_lanzamiento, 'Recaudaciones': series_recaudaciones, 'Espectadores': series_espectadores}
df = pd.DataFrame(data)

año = 2023

#Filtramos las peliculas de mas de 10 años
peliculas_mas_10_años = df[df['Lanzamiento'] < año - 10]

print(f"Películas con más de 10 años: {peliculas_mas_10_años}")

# Filtramos las películas entre 800 millones de recaudación y 65 millones de espectadores
peliculas_filtradas = df[(df['Recaudaciones'] > 800) & (df['Espectadores'] > 65)]
print(f"Películas que superan los 800 millones de recaudación y 65 millones de espectadores: {peliculas_filtradas}")

# Añadimos una columna 
#peliculas_filtradas.loc[:, 'Ingreso_espectador'] = peliculas_filtradas['Recaudaciones'] / peliculas_filtradas['Espectadores']
