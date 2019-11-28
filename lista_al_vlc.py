import os


def lista_a_vlc(lista):
    canciones = " ".join(lista)
    rutaVLC = '"C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"'
    comando = rutaVLC + " " + canciones
    return os.popen(comando)
