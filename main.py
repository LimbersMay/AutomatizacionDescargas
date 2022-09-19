from ordenamiento.ordenamiento import Ordenamiento
from auditoria.auditor import Auditor


def main():
    ruta_json = "json/informacion.json"

    # Ordenamos y creamos las carpetas del Json
    ordenamiento = Ordenamiento(ruta_json)
    ordenamiento.crear_carpetas()
    ordenamiento.ordenar_recurso()

    # Comprobamos si hay ficheros sin registro o registros sin ficheros
    auditor = Auditor(ruta_json)
    auditor.comprobar_ficheros()
    auditor.comprobar_registros()


if __name__ == '__main__':
    main()
