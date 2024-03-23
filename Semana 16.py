# Creación y escritura en el archivo my_notes.txt
with open("my_notes.txt", "w") as file:
    # Escribir el título de las notas personales
    file.write("Notas personales:\n")

    # Escribir las notas una por una
    file.write("- Recordar comprar leche.\n")  # Primera línea de notas
    file.write("- Llamar a Juan a las 3 PM.\n")  # Segunda línea de notas
    file.write("- Preparar presentación para reunión de mañana.\n")  # Tercera línea de notas

# Lectura del archivo my_notes.txt
print("Contenido de my_notes.txt:")
with open("my_notes.txt", "r") as file:
    # Leer cada línea del archivo y mostrarla en la consola
    for line in file.readlines():
        print(line.strip())  # Eliminar espacios en blanco adicionales alrededor de la línea

# El archivo se cerrará automáticamente después de salir del bloque "with"