# Calcular el promedio de temperaturas para cada ciudad, semana y día de la semana
for ciudad_idx, ciudad in enumerate('temperaturas'):
    print(f"Promedio de temperaturas para la Ciudad {ciudad_idx + 1}:")

    # Iterar sobre las semanas para la ciudad actual
    for semana_idx, semana in enumerate(ciudad):
        print(f"\nSemana {semana_idx + 1}:")

        # Inicializar la suma de temperaturas para la semana
        suma_temperaturas_semana = 0

        # Inicializar el contador de días
        contador_dias = 0

        # Inicializar las sumas diarias
        sumas_diarias = {'Lunes': 0, 'Martes': 0, 'Miércoles': 0, 'Jueves': 0, 'Viernes': 0, 'Sábado': 0, 'Domingo': 0}

        # Iterar sobre los días de la semana actual
        for dia in semana:
            suma_temperaturas_semana += dia['temp']  # Sumar la temperatura del día actual
            sumas_diarias[dia['day']] += dia['temp']  # Sumar la temperatura del día actual

            # Incrementar el contador de días
            contador_dias += 1

            # Mostrar la temperatura del día actual
            print(f"{dia['day']}: {dia['temp']}°C")

        # Calcular el promedio de temperaturas para la semana actual
        promedio_semana = suma_temperaturas_semana / contador_dias

        # Imprimir el promedio de temperaturas para la semana actual
        print(f"Promedio semana: {promedio_semana:.2f}°C")

        # Calcular y mostrar el promedio de temperaturas diario para la semana
        print("Promedio diario:")
        for dia, suma_dia in sumas_diarias.items():
            promedio_dia = suma_dia / contador_dias
            print(f"{dia}: {promedio_dia:.2f}°C")
