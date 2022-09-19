import os


class Carpeta:

    def __init__(self, ruta: str, carpetas=None) -> None:
        self.carpetas = carpetas
        self.ruta = ruta

    def set_carpetas(self, carpetas: list[str]):
        self.carpetas = carpetas

    def crear_carpetas(self):
        for carpeta in self.carpetas:
            ruta_carpeta = self.ruta + "\\" + carpeta

            # Si la carpeta no existe, la creamos
            if not os.path.exists(ruta_carpeta):
                os.mkdir(ruta_carpeta)
