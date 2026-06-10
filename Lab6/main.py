from utils import bienvenida, promedio, validar_email


def main():
    """
    Ejecuta el programa principal utilizando las funciones importadas
    desde el archivo utils.py.

    Parámetros:
        Ninguno

    Retorno:
        None
    """
    # Se llama a la función que muestra el mensaje inicial
    bienvenida()

    print("\n--- Cálculo de promedio ---")

    try:
        # Se solicitan dos números al usuario
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))

        # Se llama a la función promedio y se guarda el resultado
        resultado_promedio = promedio(numero1, numero2)

        print(f"El promedio de {numero1} y {numero2} es: {resultado_promedio}")

    except ValueError:
        # Mensaje que aparece si el usuario ingresa texto en lugar de números
        print("Error: Debe ingresar valores numéricos.")
    #Victoria:
        print("\n--- Validación de correo electrónico ---")

    # Se solicita un correo para validar su formato
    correo = input("Ingrese un correo electrónico: ")

    # Se verifica si el correo ingresado cumple con el formato correcto
    if validar_email(correo):
        print("El correo ingresado es válido.")
    else:
        print("El correo ingresado no es válido.")


# Esta condición permite ejecutar el programa solo cuando se corre este archivo directamente
if _name_ == "_main_":
    main()
