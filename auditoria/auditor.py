import os
from datetime import datetime
from send2trash import send2trash
from ordenamiento.ficheroinformacion import FicheroInformacion
from ordenamiento.manipulacionarchivo import ManipulacionArchivo


class Auditor(FicheroInformacion, ManipulacionArchivo):
    def __init__(self, nombre: str, modo: str = "r"):
        super().__init__(nombre, modo=modo)

        self.fecha_actual = datetime.now()
        self.ficheros = []

        self.obtener_informacion()

    def comprobar_ficheros(self):
        self.abrir_fichero()

        # Recorremos todos los directorios y comprobamos que la fecha no se haya pasado del
        # límite y que si tengan un registro en el Json
        for directorio, carpetas, archivos in os.walk(self.ruta_destino_json):
            self.ficheros.extend(archivos)

            for archivo in archivos:
                # Comprobamos que el archivo tenga registro en el Json, en caso de no tenerlo, lo registramos
                if not archivo in self.archivos_claves:
                    self.escribir_fecha_archivo(archivo, str(self.fecha_actual.date()))

                # Comprobamos si la fecha del archivo ya expiro, de ser el caso, será eliminado junto a su registro
                # en el Json
                fecha_fichero = datetime.strptime(self.obtener_fecha_archivo(archivo), "%Y-%m-%d")
                if (self.fecha_actual - fecha_fichero).days > self.limite_dias:
                    try:
                        if self.enviar_papelera:
                            send2trash(directorio + "\\" + archivo)
                        else:
                            os.remove(directorio + "\\" + archivo)

                        self.ficheros.remove(archivo)
                        self.eliminar_registro(archivo)
                    except Exception as e:
                        pass

        self.cerrar_fichero()

    def comprobar_registros(self):
        self.obtener_claves_archivos()

        # Analizamos todos los registros y determinamos si alguno de estos ficheros no se encuentran en la carpeta
        registros_sin_ficheros = list(set(self.archivos_claves).difference(self.ficheros))

        for registro in registros_sin_ficheros:
            self.eliminar_registro(registro)
