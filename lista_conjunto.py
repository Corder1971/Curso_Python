list = list() # crear lista vacía
set =set() # crear conjunto vacío
l = int(input("Introduzca el tamaño de la lista: ")) # variable para el tamaño de la lista
s = int(input("Introduzca el tamaño del set:")) # variable para el tamaño del set
print("Introduzca los numeros de la lista: ") # mostrar mensaje para introducir los números de la lista
for i in range(0, 1): # bucle para introducir los números de la lista
    list.append(int(input())) # añadir el número introducido a la lista
print ("Introduzca los elementos del set: ") # mostrar mensaje
for i in range(0, 5): # bucle para introducir los números delm set
    set.add(int(input())) # añadir el número al cunjunto
print(list) # mostrar la lista
print(set) # mostrar el conjunto


