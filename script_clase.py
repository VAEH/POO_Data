#https://pybonacci.org/2017/01/11/manejo-de-atributos-mediante-propiedades/

class Millas:
	def __init__(self):
		self._distancia = 0

    
	def convertir_a_kilometros(self):
		return (self._distancia * 1.609344)

	# Función para obtener el valor de _distancia
	@property
	def obtener_distancia(self):
		print("Llamada al método getter")
		return self._distancia

	# Función para definir el valor de _distancia
	@obtener_distancia.setter
	def definir_distancia(self, valor):
		if valor < 0:
			raise ValueError("No es posible convertir distancias menores a 0.")
		self._distancia = valor

	# Función para eliminar el atributo _distancia
	@definir_distancia.deleter
	def eliminar_distancia(self):
		del self._distancia

	#distancia = property(obtener_distancia, definir_distancia, eliminar_distancia)


avion = Millas()

# Indicamos la distancia
avion.definir_distancia = 200

# Obtenemos su atributo distancia
print(avion.definir_distancia)
print(avion.convertir_a_kilometros())      



  


