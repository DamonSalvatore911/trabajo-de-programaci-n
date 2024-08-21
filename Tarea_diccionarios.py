#Ejercicio numero 1
# Ejemplo
cars = {'ferrari': 488,'porsche': 911,'mclaren': 765,'aston': 77}

# Ordenar y imprimir los valores de forma ascendente
valores_ordenados = sorted(cars.values())
for valor in valores_ordenados:
    print(valor)




#Ejercicio numero 2
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





#Ejercicio numero 3
def mezclar_diccionarios(dic1, dic2):
    # Se debe crear una copia del segundo diccionario
    diccionario_mezclado = dic2.copy()
    
    # Se actualiza con los valores del primer diccionario
    diccionario_mezclado.update(dic1)
    
    return diccionario_mezclado

# Ejemplo de uso
dic1 = {'a': 100, 'b': 250, 'd': 505}
dic2 = {'b': 356, 'c': 477, 'd': 150}
resultado = mezclar_diccionarios(dic1, dic2)
print(resultado)

# El metodo 'update' lo que hace es que actualiza los elemento(s) del diccionario
# pero si no esta entonces añade el elemento(s)





#Ejercicio numero 4
# Lista de personas
personas = [
    {"nombres": "Johan Samuel", "apellidos": "Fuquene Torres", "edad": 27},
    {"nombres": "Julian Andres", "apellidos": "Mendez Sierra", "edad": 19},
    {"nombres": "Juan Manuel", "apellidos": "Berdugo Torres", "edad": 35},
    {"nombres": "David Felipe", "apellidos": "Pinzon Polania", "edad": 67},
]

# Rango de edades
edad_minima = 25
edad_maxima = 47

# Se usa filter para filtrar personas en el rango de edad
personas_en_rango = filter(
    lambda persona: edad_minima <= persona["edad"] <= edad_maxima,
    personas
)

# Imprime los nombres y apellidos de las personas en el rango
for persona in personas_en_rango:
    print(f'{persona["nombres"]} {persona["apellidos"]}')
