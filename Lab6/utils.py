#Diego: Función de bienvenida
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

#Harol: Función promedio
def promedio(numero1, numero2):
    """
    Calcula el promedio de dos números ingresados.

    Parámetros:
        numero1 (float): Primer número.
        numero2 (float): Segundo número.

    Retorno:
        float: Promedio de los dos números.
    """
    # Se suman los dos números y se divide entre 2 para obtener el promedio
    resultado = (numero1 + numero2) / 2
    return resultado
