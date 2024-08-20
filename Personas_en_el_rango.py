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
