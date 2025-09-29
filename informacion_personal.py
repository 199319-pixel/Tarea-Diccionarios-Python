# Tarea: Trabajando con Diccionarios en Python
# Autor: Arturo Geovanni Chalacan Paspuel
# Descripción: Ejemplo que crea y manipula un diccionario con información personal.

# 1) Crear el diccionario
informacion_personal = {
    "nombre": "Arturo Chalacan",              # nombre 
    "edad": 32,                           # edad inicial (luego será eliminada)
    "ciudad": "Tena",                    # ciudad inicial
    "profesion": "Policia Nacional del Ecuador"  # profesión inicial
}

print("Diccionario inicial:")
print(informacion_personal)

# 2) Acceder y modificar valores (modificar ciudad)
print("\nCiudad actual:", informacion_personal["ciudad"])
informacion_personal["ciudad"] = "Quito"  # cambiamos la ciudad
print("Ciudad modificada a:", informacion_personal["ciudad"])

# 3) Agregar nueva clave-valor relacionada con la profesión
informacion_personal["profesion_detalle"] = "Desarrolladora Backend con 3 años de experiencia"
print("\nSe agregó 'profesion_detalle':", informacion_personal["profesion_detalle"])

# 4) Verificar existencia de "telefono" y agregar si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "+593992538876"  # número ficticio
    print("\nLa clave 'telefono' no existía; se añadió:", informacion_personal["telefono"])
else:
    print("\nLa clave 'telefono' ya existía:", informacion_personal["telefono"])

# 5) Eliminar la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]
    print("\nSe eliminó la clave 'edad'.")
else:
    print("\nNo existía la clave 'edad' para eliminar.")

# 6) Imprimir el diccionario final
print("\nDiccionario final resultado de todas las operaciones:")
print(informacion_personal)
