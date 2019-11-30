import os


def lista_a_vlc(lista):
    assert isinstance(lista, list)
    canciones = " ".join(lista)
    # rutaVLC = '"C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"'
    rutaVLC = '"vlc"'
    try:
        os.popen(rutaVLC)
    except OSError:
        print('El sistema no puede encontrar la ruta especificada')
    else:
        pass
    comando = rutaVLC + " " + canciones
    return os.popen(comando)


if __name__ == "__main__":
    lista_a_vlc(['/home/mateu/Escritorio/CancionesVLC/Insert_coin.mp3',
                 '/home/mateu/Escritorio/CancionesVLC/Because.mp3'])
