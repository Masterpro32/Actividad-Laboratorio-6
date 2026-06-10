def bienvenida():
    """
    Muestra un mensaje inicial de bienvenida al usuario.

    Parámetros:
        Ninguno

    Retorno:
        None
    """
    # Mensaje que se muestra al iniciar el programa
    print("Bienvenido al programa de funciones reutilizables.")


import re

def validar_email(correo):
    """
    Verifica si una cadena de texto tiene formato de correo electrónico.

    Parámetros:
        correo (str): Correo ingresado por el usuario.

    Retorno:
        bool: True si el correo es válido, False si no lo es.
    """
    # Eliminamos espacios al inicio o al final del texto ingresado
    correo = correo.strip()

    # Patrón básico para validar que el texto tenga estructura de correo
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    # Se compara el correo ingresado con el patrón definido
    if re.match(patron, correo):
        return True
    else:
        return False
