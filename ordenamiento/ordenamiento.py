import os
import datetime
from utilidades.busqueda import *
from utilidades.carpeta import Carpeta
from ordenamiento.ficheroinformacion import FicheroInformacion
from ordenamiento.manipulacionarchivo import ManipulacionArchivo
from utilidades.notificacion import mandar_notificacion


class Ordenamiento(FicheroInformacion, ManipulacionArchivo):

    # Constructor de la clase
    def __init__(self, nombre: str, modo: str = "r"):
        super().__init__(nombre, modo)
        self.fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d")
        self.obtener_informacion()

    # Métodos de la clase
    # Algoritmos de ordenamiento
    def ordenar_recurso(self):

        # Listamos todas las carpetas de la ruta de origen
        listado_origen = os.listdir(self.ruta_origen_json.strip())

        # Contador para conocer la cantidad de archivos que se movieron
        contador: int = 0

        # Recorremos los archivos de la ruta de origen
        for archivo in listado_origen:

            # Definimos la ruta del archivo en su carpeta de origen para determinar si es un fichero o una carpeta
            comprobante = self.ruta_origen_json + "\\" + archivo
            tamanio_fichero = os.path.getsize(comprobante)
            
            if os.path.isfile(comprobante) and tamanio_fichero < self.limite_tamanio:
                contador += 1

                # Obtenemos el nombre  y la extensión del archivo
                nombre, extension = os.path.splitext(archivo)
            
                nombre_carpeta = busqueda_lineal(self.obtener_json()["extensiones"], extension)

                self.ruta_destino_json += '\\' + nombre_carpeta 

                self.set_nombre_archivo(nombre.title() + extension)
                self.set_ruta_origen(self.ruta_origen_json)
                self.set_ruta_destino(self.ruta_destino_json)

                self.escribir_fecha_archivo(nombre.title() + extension, self.fecha_actual)
                self.mover_fichero()

                self.obtener_rutas()
        
        mandar_notificacion(contador)
        
    def crear_carpetas(self):
        carpeta = Carpeta(self.ruta_destino_json, self.extension_claves)

        carpeta.crear_carpetas()
        

# Tiempo promedio de 10000 ejecuciones
# Tiempo promedio del método 1(Busqueda lineal): 11.77 segundos
# Tiempo promedio del método 2(Busqueda lineal): 11.31
# Tiempo promedio del método 3(Busqueda binaria): 9.83 segundos
