from typing import List
from fuzzywuzzy import fuzz


# Función para determinar la similitud entre dos carpetas
def determinar_similitud(nombre_archivo: str, nombre_carpeta: str):
    return fuzz.token_set_ratio(nombre_archivo, nombre_carpeta)


def busqueda_binaria(arreglo: List[str], valor: str) -> int:
    izquierda = 0
    derecho = len(arreglo) - 1

    while izquierda <= derecho:
        medio = int((izquierda + derecho) / 2)

        # Si encuentro el valor que estoy buscando
        if determinar_similitud(valor, arreglo[medio]) > 90:
            return medio

        elif arreglo[medio] > valor:
            derecho = medio - 1

        else:
            izquierda = medio + 1

    return 0


def busqueda_lineal(arreglo: dict[str], valor: str) -> str:

    for clave in arreglo:
        if valor in arreglo[clave]:
            return clave

    return "Otro"
