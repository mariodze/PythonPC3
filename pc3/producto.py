class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def __str__(self):
        pais, lote, anio = self.codigo.split('-')
        return f"Nombre: {self.nombre}, País: {pais}, Lote: {lote}, Año: {anio}"
