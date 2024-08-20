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
