class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_lista_productos(self):
        for producto in self.productos:
            print(f"Nombre: {producto.nombre}, Código: {producto.codigo}")
