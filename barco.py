class Barco:
    def __init__(self, nombre, longitud):
        self.nombre = nombre
        self.longitud = longitud
        self.golpes_recibidos = 0

    def recibir_impacto(self):
        self.golpes_recibidos += 1


    def esta_hundido(self):
        return self.golpes_recibidos >= self.longitud