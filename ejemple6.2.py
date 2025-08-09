d = {"50862634" :37 , "43394932" : 32} # Creamos un diccionario con dos claves y sus respectivos valores
texto = input("Introduce un numero de DNI: ")
if texto in d: # comprobamos si esta eln el diccionario
    print(f"La edad de  {texto} es {d[texto]}") 
else:
    edad = input("El DNI no se encuentra en el diccionario. Introduce tú edad:")
    if edad.isnumeric():
        num = int(edad)
        d[texto] = num # añadimos el DNI y la edad al diccionario
d[texto] = num
print("Se a añadido el DNI al diccionario")
print(d) # mostramos el diccionario
