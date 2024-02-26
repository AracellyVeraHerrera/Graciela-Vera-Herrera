# Matriz definida fuera de la función
matriz_global = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def buscar_valor(matriz_parametro, valor):
    for i in range(len(matriz_parametro)):
        for j in range(len(matriz_parametro[i])):
            if matriz_parametro[i][j] == valor:
                return True, i, j
    return False, None, None

# Llamada a la función buscar_valor con la matriz_global
valor_buscar = 5
encontrado, fila, columna = buscar_valor(matriz_global, valor_buscar)

if encontrado:
    print(f"El valor {valor_buscar} se encontró en la posición [{fila}][{columna}] de la matriz.")
else:
    print(f"El valor {valor_buscar} no se encontró en la matriz.")