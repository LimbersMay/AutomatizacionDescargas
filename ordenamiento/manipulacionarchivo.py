import shutil


class ManipulacionArchivo:

    # Constructor
    def __init__(self, ruta_origen: str = "", nombre_archivo: str = ""):
        # Configuraciones necesarias para realizar la operación del archivo
        self.ruta_origen = ruta_origen + "/"
        self.nombre_archivo = nombre_archivo
        self.ruta_destino = None

    # Métodos necesarios de la clase
    def mover_fichero(self):
        try:
            shutil.move(self.ruta_origen + self.nombre_archivo, self.ruta_destino + self.nombre_archivo)
        except:
            return

    def copiar_fichero(self):
        shutil.copy(self.ruta_origen + self.nombre_archivo, self.ruta_destino + self.nombre_archivo)
            
    # Métodos de rutas
    def set_ruta_origen(self, ruta_origen: str):
        self.ruta_origen = ruta_origen + "\\"

    def set_ruta_destino(self, ruta_destino: str):
        self.ruta_destino = ruta_destino + "\\"

    def set_nombre_archivo(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo
