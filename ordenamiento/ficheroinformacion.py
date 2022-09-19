import json
from io import open


class FicheroInformacion:

    # Recibimos todos los datos del fichero
    def __init__(self, nombre: str, modo: str = "r"):
        self.nombre = nombre
        self.modo = modo

        self.ruta_origen_json = ""
        self.ruta_destino_json = ""

        self.enviar_papelera: bool

        self.limite_tamanio: int
        self.limite_dias: int

        self.archivos_claves: list[str]
        self.archivos_valores: list[str]

        self.extension_claves = list[str]
        self.extension_valores = list[str]

        self.abrir = open(self.nombre, self.modo)
        self.cargar: dict

    # Abrimos el fichero y lo devolvemos
    def abrir_fichero(self, modo: str = "r"):

        if modo == "w":
            self.abrir = open(self.nombre, "r")

            self.cargar = json.loads(self.abrir.read())
            self.abrir.close()

            self.abrir = open(self.nombre, "w")
        else:
            self.abrir = open(self.nombre, modo)
            self.cargar = json.loads(self.abrir.read())

    # Cerramos el fichero que hemos abierto
    def cerrar_fichero(self):
        self.abrir.close()

    # Devolvemos el fichero ya abierto
    def obtener_json(self):
        self.abrir_fichero()
        self.abrir.close()

        return dict(self.cargar)

    # ------------ Restricciones de tamaño y días ---------------------
    def obtener_restricciones(self):
        self.limite_dias = self.cargar["limiteDias"]
        self.limite_tamanio = self.cargar["limiteTamanio"]
        self.enviar_papelera = self.cargar["enviarAPapelera"]

    # ------------- Rutas -----------------------------
    def obtener_rutas(self):
        self.abrir_fichero()

        self.ruta_origen_json = self.cargar["rutas"]["rutaOrigen"]
        self.ruta_destino_json = self.cargar["rutas"]["rutaDestino"]

        self.abrir.close()

    # ------------ Archivos ----------------------------------------
    # Escribimos la fecha de creación del archivo
    def escribir_fecha_archivo(self, nombre: str, fecha: str):
        self.abrir_fichero("w")
        self.cargar["archivos"][nombre] = fecha

        self.abrir.write(json.dumps(self.cargar, indent=4))
        self.abrir.close()

    # Obtenemos la fecha de creación del archivo
    def obtener_fecha_archivo(self, nombre: str):
        
        fecha = self.cargar["archivos"][nombre]

        return fecha
    
    # Obtenemos los nombres de los archivos
    def obtener_claves_archivos(self):
        self.abrir_fichero()
        self.abrir.close()

        self.archivos_claves = list(self.obtener_json()["archivos"].keys()) 
    
    def eliminar_registro(self, clave: str):
        self.abrir_fichero("w")

        self.cargar["archivos"].pop(clave)
        self.abrir.write(json.dumps(self.cargar, indent=4))

        self.cerrar_fichero()

    # ------------- Extensiones ---------------------
    def obtener_claves_extensiones(self):
        self.abrir_fichero()
        self.abrir.close()

        self.extension_claves = list(self.obtener_json()["extensiones"].keys())

    def obtener_valores_extensiones(self):
        self.abrir_fichero()
        self.abrir.close()

        lista_valores = list(self.obtener_json()["extensiones"].values())
        self.extension_valores = [extension for sublista in lista_valores for extension in sublista]

    def obtener_informacion(self):
        self.obtener_rutas()
        self.obtener_restricciones()
        self.obtener_claves_extensiones()
        self.obtener_valores_extensiones()
        self.obtener_claves_archivos()
