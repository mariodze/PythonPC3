import os

if __name__ == '__main__':
    # Ejercicio 2 - CIRCULO
    from circulo import Circulo
    circulo = Circulo(5)
    area = circulo.calcular_area()
    print(f"\nEjercicio 2 - CIRCULO\nÁrea del círculo: {area}\n")

    # Ejercicio 3 - Catálogo y Producto
    from catalogo import Catalogo, Producto
    catalogo = Catalogo()
    producto1 = Producto("Llanta", "USA-001-2023")
    producto2 = Producto("Aceite", "MEXICO-002-2023")
    catalogo.agregar_producto(producto1)
    catalogo.agregar_producto(producto2)
    print("\nEjercicio 3 - Catálogo y Producto\nLista de productos en el catálogo:")
    catalogo.mostrar_lista_productos()
    print()

    # Ejercicio 4 - Menú iterativo con importación de módulos y manejo de errores
    import modulo_operaciones
    while True:
        try:
            opcion = int(input("Ejercicio 4 - Menú iterativo\n1. Dividir dos números\n2. Salir\nIngrese una opción: "))
            if opcion == 1:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                resultado = modulo_operaciones.dividir(num1, num2)
                print(f"Resultado: {resultado}")
            elif opcion == 2:
                break
            else:
                print("Opción inválida. Intente de nuevo.")
        except ValueError:
            print("Error: Ingrese un número válido.")
        except ZeroDivisionError:
            print("Error: No se puede dividir por cero.")
        else:
            print(f"Directorio de trabajo: {os.getcwd()}")
        finally:
            print("Proceso terminado.\n")

    # Ejercicio 5 - Clase Producto con formato de código
    from producto import Producto
    producto = Producto("Motor", "ARGENTINA-003-2023")
    print(f"\nEjercicio 5 - Clase Producto con formato de código\n{producto}\n")

    # Ejercicio 7 - Método nuevo en la clase Phone
    from phone import Phone
    phone = Phone("Samsung", "Galaxy S20")
    phone.nuevo_metodo()
    print("\nEjercicio 7 - Método nuevo en la clase Phone\n")

    # Ejercicio 8 - Clase Persona con datos ingresados desde teclado
    from persona import Persona
    persona = Persona()
    print(f"\nEjercicio 8 - Clase Persona con datos ingresados desde teclado\nNombre: {persona.nombre}, Edad: {persona.edad}\n")
