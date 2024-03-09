def calcular_temperatura_promedio(datos):
    promedios_ciudades = {}
    for ciudad, temperaturas_semanales in datos.items():
        total_temperaturas = 0
        for semana in temperaturas_semanales:
            total_temperaturas += sum(semana)
        promedio_ciudad = total_temperaturas / (len(temperaturas_semanales) * 7)  # Suponiendo que hay 7 días en una semana
        promedios_ciudades[ciudad] = promedio_ciudad
    return promedios_ciudades

# Ejemplo de uso
datos = {
    "Ciudad A": [[20, 21, 22, 23, 24, 25, 26], [21, 22, 23, 24, 25, 26, 27], [22, 23, 24, 25, 26, 27, 28], [23, 24, 25, 26, 27, 28, 29]],
    "Ciudad B": [[18, 19, 20, 21, 22, 23, 24], [19, 20, 21, 22, 23, 24, 25], [20, 21, 22, 23, 24, 25, 26], [21, 22, 23, 24, 25, 26, 27]],
    "Ciudad C": [[15, 16, 17, 18, 19, 20, 21], [16, 17, 18, 19, 20, 21, 22], [17, 18, 19, 20, 21, 22, 23], [18, 19, 20, 21, 22, 23, 24]]
}

resultados = calcular_temperatura_promedio(datos)
for ciudad, promedio in resultados.items():
    print(f"Temperatura promedio en {ciudad}: {promedio:.2f} grados Celsius")
