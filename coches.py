class Coche: # Declaración de la clase
# Declaración de atributos de la clase
    largo = 250
    ancho = 120
    ruedas = 4
    peso = 900
    color = 'rojo'
    isEnmarcha = False    

# Declaración de métodos de la clase
    def arrancar(self): # Self hace rferencia a la instacia de la clase
      self.isEnmarcha = True # Cambia el estado de isEnmarcha a True
    def estado(self):
      if (self.isEnmarcha == True):
        return "El coche está en marcha"
      else:
        return "El coche está parado"
# Declaración de instancias de la clase, objeto de clase o ejemplar de clase
miCoche = Coche()
miCoche2 = Coche()
# Acceso a los atributos de la clase Coche. Nomenglatura del punto.
print("El largo del coche es :", miCoche.largo, "cm")
miCoche.arrancar()
# print (miCoche.estado())
# Acceso a un método de la clase Coche. Nomenglatura del punto.
print("El coche esta arrancado:", miCoche.arrancar())
# Modificamos el valor de una propiedad de la clase
miCoche2.ruedas = 10
print ("El coche miCoche2 tiene:", miCoche2.ruedas, "ruedas")



