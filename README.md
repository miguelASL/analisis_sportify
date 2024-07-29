# 🎵 Análisis de Datos de Artistas en Spotify 🎵

Este proyecto analiza las canciones de un artista específico en Spotify utilizando la biblioteca Spotipy, recuperando datos como información de álbumes, duración de las canciones y popularidad. Los datos se visualizan utilizando Plotly.

## 🚀 Características

- 📊 Recupera y muestra información de artistas desde Spotify.
- 🎶 Obtiene detalles de álbumes y canciones, incluyendo duración y popularidad de las canciones.
- 📈 Visualiza las canciones más populares y las más largas del artista mediante gráficos interactivos.

## 🛠 Requisitos

- 🐍 Python 3.6+
- 🔑 Cuenta de desarrollador de Spotify para obtener las credenciales de la API
- 📦 Paquetes de Python requeridos: `spotipy`, `pandas`, `plotly`

## 💻 Instalación

**1. Clona el repositorio:**```
    - ```git clone https://github.com/miguelASL/analisis-datos-artistas-spotify.git```
    - ```cd analisis-datos-artistas-spotify```
      

**2. Instala los paquetes requeridos:**
    - ```pip install spotipy pandas plotly```

**3. Obtén tus credenciales de la API de Spotify creando una aplicación en el [Panel de Desarrolladores de Spotify](https://developer.spotify.com/). Configura el `client_id` y `client_secret` en el script.**

## 📚 Uso

**1. Configura tus credenciales de la API de Spotify:**
   -  ```client_id = "tu_client_id"```
   - ```client_secret = "tu_client_secret"```
    

**2. Ejecuta el script:**
    
- python main.py

**3. Introduce el nombre del artista que deseas analizar cuando se te pida.**

## 🌟 Ejemplo

Para analizar las canciones de la artista Karol G, el script recupera los datos de la artista, procesa los álbumes y las canciones, y visualiza las canciones más populares y las más largas.

## 📊 Visualización

El script genera dos gráficos interactivos de barras:

- **Canciones Más Populares:** Muestra las 20 canciones más populares del artista.
- **Canciones Más Largas:** Muestra las 20 canciones más largas del artista.

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Por favor, sigue los siguientes pasos:

**1. Haz un fork del proyecto y crea una nueva rama:**
    
- ``` git checkout -b feature/nueva-funcionalidad ```

**2. Realiza tus cambios y haz commit:**
- ```git commit -am 'Agrega nueva funcionalidad'```

**3. Sube los cambios:**
- ```git push origin feature/nueva-funcionalidad```

**4. Abre un Pull Request.**

## 📜 Licencia

Este proyecto está licenciado bajo la Licencia MIT.

## 📬 Contacto

**Email**: [![Email](https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white)](mailto:msarmientolevy@gmail.com)

**LinkedIn**: [![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/miguel-sarmiento-)

**Enlace del Proyecto**: [![Repo](https://img.shields.io/badge/Repository-%23121011.svg?logo=github&logoColor=white)](https://github.com/miguelASL/analisis_sportify)
