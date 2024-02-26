def ordenar_fila(matriz_parametro, fila):
    matriz_parametro[fila].sort()

# Definimos una matriz de ejemplo
matriz_ejemplo = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Llamamos a la función ordenar_fila con la matriz de ejemplo y la fila a ordenar
fila_a_ordenar = 1
print("Matriz original:")
for fila in matriz_ejemplo:
    print(fila)

ordenar_fila(matriz_ejemplo, fila_a_ordenar)

print("\nMatriz con la fila ordenada:")
for fila in matriz_ejemplo:
    print(fila)
