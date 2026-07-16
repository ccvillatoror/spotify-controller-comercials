# Reproductor de comerciales

Este proyecto automatiza el proceso de pausar la música de Spotify, reproducir un comercial y reanudar la reproducción de Spotify.

## Prerrequisitos

Obtener credenciales para la Spotify Web API. Puedes seguir la página de [Spotify for Developers](https://developer.spotify.com/documentation/web-api).

Colocar las credenciales en las variables `client_id` y `client_secret` del archivo `spotify_controller`. La variable `redirect_uri` puede quedarse con el valor de 'http://127.0.0.1:3000'.

Tener Spotify corriendo y reproduciendo una canción. Si no, el programa no funcionará.

## Paquetes de Python necesarios

**Versión de Python:** Python 3.14.4

Se necesitan tener los siguientes paquetes de python instalados:

- `playsound3`
- `spotipy`
- `random`
- `pathlib`
- `schedule`

## Para correr el programa
Abrir la terminal, correr el archivo main.
En Linux:
```
python3 main.py
```

Las pistas de audio deben estar en la carpeta `media`. Los tipos de archivos que se han probado son: `.mp3`, `.wav`, `.aiff`.

Los sonidos fueron descargados de [Freesound](https://freesound.org/).

## Posibles errores
- Las credenciales de la API están desactualizadas.
- Spootify no está abierto.
- Se está corriendo muchas veces sin esperar un poco de tiempo.

## Mejoras a futuro
Adecuar el comportamiento del programa a si Spotify está abierto o no, en pausa o no.

Mejorar el manejo de credenciales, de una forma más segura que escribirlos en el código.

Agregarle una interfaz gráfica, drag and drop para agregar más pistas de audio, pantalla para agregar credenciales de la API de Spotify, que te digan si ya van a caducar.

Buscar una manera de que actualice las credenciales automáticamente.

Mejorar el manejo de errores del programa.
