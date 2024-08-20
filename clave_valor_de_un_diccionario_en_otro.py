#  Ejemplo
millos = {'Falcao': 9, 'James': 10, 'Luis': 7}
santafe = {'Falcao': 9, 'James': 10, 'Luis': 7, 'Richard': 6}

# Verifica si todas las clave:valor están presentes usando conjuntos
def verificar_inclusion(millos, santafe):
    return set(millos.items()).issubset(set(santafe.items()))

# Ejemplo de uso
resultado = verificar_inclusion(millos, santafe)
print(resultado)

# si todas las clave: valor de un diccionario se encuentran en otro diccionario devuelve True 
# si no devuelve False
