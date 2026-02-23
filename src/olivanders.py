class Producto:
    def __init__(self, nombre: str, sell_in: int, calidad: int):
        self.nombre = nombre
        self.sell_in = sell_in
        self.calidad = calidad

    def actualizar(self):
        raise NotImplementedError