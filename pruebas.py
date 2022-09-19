import random
# Sudoku 9x9

def main():
    # Se crea una matriz de 9x9
    matriz = [[0 for x in range(9)] for i in range(9)]
    
    for fila in range(9):
        for elemento in range(9):
            aleatorio = random.randint(0, 9)
            matriz[fila][elemento] = aleatorio

    for fila in matriz:
        for elemento in fila:
            if fila.count(elemento) > 1:
                print("Sudoku inválido en el sub-arreglo: ", fila)
                print("Elemento repetido: ", elemento)
                print("Veces repetidas: ", fila.count(elemento))
                print()
                break
            
    print(matriz)

main()