import os


def lista_a_vlc(lista):
    assert isinstance(lista, list)
    canciones = " ".join(lista)
    rutaVLC = '"C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"'
    # rutaVLC = '"vlc"'
    try:
        exec(rutaVLC)
    except OSError:
        print('El sistema no puede encontrar la ruta especificada')
    else:
        pass
    comando = rutaVLC + " " + canciones
    assert isinstance(comando, str)
    return os.popen(comando)
