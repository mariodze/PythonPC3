import os

def dividir(num1, num2):
    try:
        resultado = num1 / num2
        return resultado
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
        raise
    finally:
        print(f"Directorio de trabajo: {os.getcwd()}")
