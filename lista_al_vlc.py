import os


def lista_a_vlc(lista):
    assert isinstance(lista, list)
    canciones = " ".join(lista)
    # rutaVLC = '"C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"'
    rutaVLC = '"vlc"'
    comando = rutaVLC + " " + canciones
    return os.popen(comando)

