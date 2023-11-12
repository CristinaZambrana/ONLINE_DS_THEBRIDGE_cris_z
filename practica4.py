import numpy as np
import pandas as pd

titulos = ["Toy Story 4", "Los Incríbles 2", "Buscando a Dory", "Toy Story 3", "Caco", "Inside Out", "Monsters University", "Up"]
lanzamiento = [2015, 2018, 2016, 2010, 2017, 2015, 2013, 2006]
recaudaciones = [1073, 1242, 1029, 1067, 807, 857, 744, 735]  # En millones de dólares
espectadores = [74.91, 93.42, 76.72, 81.35, 62.75, 68.27, 54.74, 54.34] # En millones, estimación hecha por aficionados

#Apartado 1
series_lanzamiento = pd.Series(lanzamiento, index=titulos, name='Lanzamiento')
print(f"Series de Lanzamiento: {series_lanzamiento}")
series_recaudaciones = pd.Series(recaudaciones, index=titulos, name='Recaudaciones')
print(f"Series de Recaudaciones: {series_recaudaciones}")
series_espectadores = pd.Series(espectadores, index=titulos, name='Espectadores')
print(f"Series de Espectadores: {series_espectadores}")

#Apartado 2
series_recaudaciones = pd.Series(recaudaciones, index=titulos, name='Recaudaciones (en millones de dólares)')
recaudaciones_ascendente = series_recaudaciones.sort_values(ascending=True)
print(f"Recaudaciones Ordenadas Ascendente: {recaudaciones_ascendente}")

recaudaciones_descendente = series_recaudaciones.sort_values(ascending=False)
print(f"Recaudaciones Ordenadas Descendente: {recaudaciones_descendente}")

#Apartado 3
for pelicula, recaudacion in series_recaudaciones.items():
    # Obtener el año de lanzamiento y número de espectadores correspondientes
    lanzamiento_pelicula = lanzamiento[series_recaudaciones.index.get_loc(pelicula)]
    espectadores_pelicula = espectadores[series_recaudaciones.index.get_loc(pelicula)]
    precio_entrada = recaudacion / espectadores_pelicula

    print(f"Película: {pelicula}")
    print(f"Recaudación: ${recaudacion} millones")
    print(f"Año de lanzamiento: {lanzamiento_pelicula}")
    print(f"Número de espectadores: {espectadores_pelicula} millones")

#Apartado 4
pelicula_menor_recaudacion = series_recaudaciones.idxmin()

año_menor = lanzamiento[series_recaudaciones.index.get_loc(pelicula_menor_recaudacion)]
print(f"La película con menor recaudación fue '{pelicula_menor_recaudacion}' y es del año {ano_menor_recaudacion}.")

peliculas_condiciones = series_recaudaciones[(series_recaudaciones > 1000) & (espectadores < 75)]
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