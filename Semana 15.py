# Crear un diccionario con la información personal de Domenica
informacion_personal = {
    "nombre": "Domenica",
    "edad": 25,
    "ciudad": "Quito",
    "profesion": "Ingeniera"
}

# Acceder y modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Guayaquil"

# Agregar una nueva clave-valor para representar la profesión
informacion_personal["profesion"] = "Ingeniera de Sistemas"

# Verificar la existencia de la clave "telefono" y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0999999999"

# Asignar el número de teléfono de Domenica
informacion_personal["telefono"] = "0954123876"

# Eliminar la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario resultante
print("Diccionario Final:")
print(informacion_personal)