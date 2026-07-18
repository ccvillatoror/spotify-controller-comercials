# Reproductor de comerciales

Este proyecto automatiza el proceso de pausar la música de Spotify, reproducir un comercial y reanudar la reproducción de Spotify.

## Prerrequisitos

Obtener credenciales para la Spotify Web API. Puedes seguir la página de [Spotify for Developers](https://developer.spotify.com/documentation/web-api).

Generar un arvico `.env` con las variables `SPOTIFY_CLIENT_ID` y `SPOTIFY_CLIENT_SECRET`, en la misma carpeta del `main` con las claves correspondientes de la API de Spotify. De la siguiente manera:
```
SPOTIFY_CLIENT_ID='clave'
SPOTIFY_CIENT_SECRET='secreto' 
```

La variable `redirect_uri` del archivo `spotify-controller` puede quedarse con el valor de 'http://127.0.0.1:3000'.

Tener Spotify corriendo y reproduciendo una canción. Si no, el programa no funcionará.

## Paquetes de Python necesarios

**Versión de Python:** Python 3.14.4

Se necesitan tener los siguientes paquetes de python instalados:

- `playsound3`
- `spotipy`
- `random`
- `pathlib`
- `schedule`
- `dotenv`

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

## Mejoras a futuro (no en orden de preferencia)
Adecuar el comportamiento del programa a si Spotify está abierto o no, en pausa o no.

Agregarle una interfaz gráfica, _drag and drop_ para agregar más pistas de audio, pantalla para agregar credenciales de la API de Spotify, que te digan si ya van a caducar.

Buscar una manera de que actualice las credenciales automáticamente. 

También actualizar el **token**, que caduca cada hora, sin cerrar el programa.

Mejorar el manejo de errores del programa.

Otro caso de uso que puede ser implementado: alarma. Que reproduzca música a cierta hora de la mañana, con un Alexa.

Considerar cambiar `playsound3` por `pygame` para reproducir el comercial.
