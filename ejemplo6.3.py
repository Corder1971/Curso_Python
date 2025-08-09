import pickle
from pathlib import Path # Importa la clase path de pathlib
d = dict() # Creamos un diccionario vacío
file_name = input("Introduce el nombre del archivo con los datos:") # Pedimos el nombre del archivo de donde cargar los datos
path = Path(file_name) # Creamos un objeto path con el nombre del archivo
if path.is_file(): # Comprobamos si el archivo existe
    input_file = open(file_name, "rb") # Abrimos el archivo en modo lectura binaria
    d = pickle.load(input_file) # Cargamos el diccionario desde el archivo
    input_file.close() # Cerramos el archivo
else:
    print("El archivo no existe crearemos un nuevo diccionario vacío.")
document_number = input("Introduce un número de DNI: ") # Pedimos el número de DNI al usuario
if document_number in d: # Comprobamos si el DNI está en el diccionario
    print:("La edad de " + document_number + " es " + str(d[document_number]))
else:
    age = input("El DNI no existe. Introduce tú edad: ")
    if age.isnumeric(): # Comprobamos si la edad es un número
        num = int(age) # Convertimos la edad a entero
        d[document_number] = num # Añadimos el DNI y la edad al diccionario
        print("Se ha añadido al diccionario")
        output_file = open(file_name, "wb") # Abrimos el archivo en modo escritura binaria
        pickle.dump(d, output_file) # Guardamos el diccionario en el archivo
        output_file.close() # Cerramos el archivo



