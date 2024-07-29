import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import plotly.express as px

# Autenticación - sin user
client_id = ""
client_secret = ""
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def encontrarID(artista):
    try:
        resultados = sp.search(q=artista, limit=1, type='artist')
        return resultados['artists']['items'][0]['id']
    except (IndexError, KeyError):
        print(f"No se encontró el artista: {artista}")
        return None

def obtenerData(artista_id):
    canciones_data = []
    try:
        resultados = sp.artist_albums(artista_id, album_type='album', limit=50)
        albums = resultados['items']
        
        for album in albums:
            album_name = album['name']
            album_tipo = album['album_type']
            album_año = album['release_date'][:4]
            
            tracks = sp.album_tracks(album['id'], limit=50)['items']
            for track in tracks:
                cancion_nombre = track['name']
                cancion_artistas = ', '.join([artista['name'] for artista in track['artists']])
                cancion_duracion = track['duration_ms']
                cancion_popularidad = sp.track(track['id'])['popularity']
                
                canciones_data.append([album_name, album_tipo, album_año, cancion_nombre, cancion_artistas, cancion_duracion, cancion_popularidad])
        
        return pd.DataFrame(canciones_data, columns=['Album', 'Tipo', 'Año', 'Canción', 'Artistas', 'Duración_ms', 'Popularidad'])
    except Exception as e:
        print(f"Error obteniendo datos: {e}")
        return pd.DataFrame(columns=['Album', 'Tipo', 'Año', 'Canción', 'Artistas', 'Duración_ms', 'Popularidad'])

def crearGraficos(df_canciones):
    # Convertir la duración de milisegundos a minutos:segundos
    df_canciones['Duración'] = df_canciones['Duración_ms'].apply(lambda x: '{:02d}:{:02d}'.format(x // 60000, (x % 60000) // 1000))
    df_canciones['Duracion_segundos'] = df_canciones['Duración_ms'] // 1000
    
    # Gráfico de canciones más populares
    canciones_populares = df_canciones.sort_values('Popularidad', ascending=False).head(20)
    color_dict = {'album': 'darkblue', 'single': 'darkred', 'compilation': 'darkgreen', 'appears_on': 'darkorange'}
    
    fig = px.bar(canciones_populares,
                x='Canción', 
                y='Popularidad',
                text='Popularidad', 
                color='Tipo', 
                color_discrete_map=color_dict,
                hover_data=['Artistas', 'Album', 'Duración'],
                title='Canciones más populares en Spotify',
                template='plotly_dark')
    fig.update_layout(title={'text': '<i>Canciones más populares</i>', 'y': 0.9, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top', 'font': {'size': 20, 'color': 'white'}},
                    xaxis={'title': 'Canción', 'titlefont': {'size': 16, 'color': 'white'}, 'tickfont': {'size': 14, 'color': 'white'}})
    fig.update_yaxes(range=[50, canciones_populares['Popularidad'].max() + 1], showgrid=False, showticklabels=False)
    fig.update_traces(texttemplate='%{text}', textposition='outside')
    fig.show()

    # Gráfico de canciones más largas
    df_duracion = df_canciones.sort_values('Duracion_segundos', ascending=False).head(20)
    fig = px.bar(df_duracion, 
                x='Canción', 
                y='Duracion_segundos',
                text='Duración', 
                color='Tipo', 
                color_discrete_map=color_dict,
                hover_data=['Artistas', 'Album', 'Popularidad'],
                title='Canciones más largas en Spotify',
                template='plotly_dark')
    fig.update_traces(texttemplate='%{text}', textposition='outside')
    fig.update_layout(title={'text': '<i>Canciones más largas</i>', 'y': 0.9, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top', 'font': {'size': 20, 'color': 'white'}},
                    xaxis={'title': 'Canción', 'titlefont': {'size': 16, 'color': 'white'}, 'tickfont': {'size': 14, 'color': 'white'}})
    fig.update_yaxes(range=[250, df_duracion['Duracion_segundos'].max() + 1], showgrid=False, showticklabels=False)
    fig.show()

# Obtener ID del artista y datos de sus canciones
id_AH = encontrarID('Karol G')
if id_AH:
    df = obtenerData(id_AH)
    if not df.empty:
        crearGraficos(df)
    else:
        print("No se encontraron datos para el artista especificado.")
else:
    print("No se encontró el artista especificado.")
