class Barco:
    def __init__(self, nombre, longitud):
        self.nombre = nombre
        self.longitud = longitud
        self.golpes_recibidos = 0

    def recibir_impacto(self):
        self.golpes_recibidos += 1


    def esta_hundido(self):
        return self.golpes_recibidos >= self.longitud

    def mostrar_estado(self):

        estado = "HUNDIDO" if self.esta_hundido() else "Aún a flote"
        print(f"Barco: {self.nombre}")
        print(f"Longitud: {self.longitud}")
        print(f"Golpes recibidos: {self.golpes_recibidos}")
        print(f"Estado: {estado}")
        print("-------------")



if __name__ == "__main__":
    print("=== PRUEBA DE CLASE BARCO ===")

    # Submarino longitud 1
    submarino = Barco("Submarino", 1)
    submarino.mostrar_estado()

    submarino.recibir_impacto()
    submarino.mostrar_estado()
    print("¿Está hundido el submarino?", submarino.esta_hundido())
    print()

    # Buque longitud 3
    buque = Barco("Buque", 3)
    buque.mostrar_estado()

    buque.recibir_impacto()
    buque.recibir_impacto()
    buque.mostrar_estado()
    print("¿Está hundido el buque?", buque.esta_hundido())

    buque.recibir_impacto()
    buque.mostrar_estado()
    print("¿Está hundido ahora?", buque.esta_hundido())