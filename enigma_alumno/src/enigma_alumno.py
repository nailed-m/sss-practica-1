


from ast import Index
from operator import le


class Enigma:
	alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	rotores = {"ROTOR_I": "EKMFLGDQVZNTOWYHXUSPAIBRCJ", 
				"ROTOR_II": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
				"ROTOR_III": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
				"ROTOR_IV": "",
				"ROTOR_V": "",
				"REFLECTOR_B": "YRUHQSLDPXNGOKMIEBFZCWVJAT"}

	saltos = {"ROTOR_I": "R", 
				"ROTOR_II": "F",
				"ROTOR_III": "W",
				"ROTOR_IV": "",
				"ROTOR_V": ""}
	

	def __init__(self, r_izquierdo = "ROTOR_I", r_central = "ROTOR_II", r_derecho = "ROTOR_III", reflector = "REFLECTOR_B", c_izquierdo = "A", c_central = "A", c_derecho = "A", lista_clavijas = []):
		#TO DO
		self.r_izquierdo_posicion = self.alfabeto.index(c_izquierdo)
		self.r_central_posicion = self.alfabeto.index(c_central)
		self.r_derecho_posicion = self.alfabeto.index(c_derecho)

		self.r_izquierdo = self.rotores[r_izquierdo]
		self.r_central = self.rotores[r_central]
		self.r_derecho = self.rotores[r_derecho]
		self.reflector = self.rotores[reflector]

		self.r_izquierdo_salto = self.saltos["ROTOR_I"]
		self.r_central_salto = self.saltos["ROTOR_II"]
		self.r_derecho_salto = self.saltos["ROTOR_III"]
	

	def codifica(self, texto):
		texto_codificado = ""
		letra_actual = ""
		desplazamiento_actual = 0

		#TO DO		
		for i in range(len(texto)):
			#pulsamos la letra
			letra_actual=texto[i]
			#movemos el rotor derecho
			self.r_derecho_posicion+=1
			if (self.r_derecho_posicion == 26):
				self.r_derecho_posicion = 0
			#si es necesario, movemos el rotor central
			if (self.r_derecho[self.r_derecho_posicion] == self.r_derecho_salto):
				self.r_central_posicion+=1
			if (self.r_central_posicion == 26):
				self.r_central_posicion = 0
			#si es necesario, movemos el rotor izquierdo
			if (self.r_central[self.r_central_posicion] == self.r_central_salto):
				self.r_izquierdo_posicion+=1
			if (self.r_izquierdo_posicion == 26):
				self.r_izquierdo_posicion = 0
			#si forma parte de una clavija, se hace la sustitución

			
			#el desplazamiento hacia el ROTOR DERECHO se calcula con la posición de la letra en el string del alfabeto
			desplazamiento_actual = self.alfabeto.index(letra_actual)
			#movemos la letra desde la clave del rotor derecho las posiciones del desplazamiento
			try:
				letra_actual = self.alfabeto[self.r_derecho_posicion + desplazamiento_actual]
			except IndexError as e:
				letra_actual = self.alfabeto[self.r_derecho_posicion + desplazamiento_actual - 26]
			#hacemos la sustitución del rotor derecho
			letra_actual = self.r_derecho[self.alfabeto.index(letra_actual)]

			#el desplazamiento hacia el ROTOR CENTRAL se calcula usando la posición en el alfabeto de nuestra letra actual y de la posición del rotor derecho
			desplazamiento_actual = self.alfabeto.index(letra_actual) - self.r_derecho_posicion
			#movemos la letra desde la clave del rotor central las posiciones del desplazamiento
			try:
				letra_actual = self.alfabeto[self.r_central_posicion + desplazamiento_actual]
			except IndexError as e:
				letra_actual = self.alfabeto[self.r_central_posicion + desplazamiento_actual - 26]
			#hacemos la sustitución del rotor central
			letra_actual = self.r_central[self.alfabeto.index(letra_actual)]

			#el desplazamiento hacia el ROTOR IZQUIERDO se calcula usando la posición en el alfabeto de nuestra letra actual y de la posición del rotor central
			desplazamiento_actual = self.alfabeto.index(letra_actual) - self.r_central_posicion
			#movemos la letra desde la clave del rotor izquierdo las posiciones del desplazamiento
			try:
				letra_actual = self.alfabeto[self.r_izquierdo_posicion + desplazamiento_actual]
			except IndexError as e:
				letra_actual = self.alfabeto[self.r_izquierdo_posicion + desplazamiento_actual - 26]
			#hacemos la sustitución del rotor izquierdo
			letra_actual = self.r_izquierdo[self.alfabeto.index(letra_actual)]

			#el desplazamiento hacia el REFLECTOR se calcula usando la posición en el alfabeto de nuestra letra actual y de la posición del rotor izquierdo
			desplazamiento_actual = self.alfabeto.index(letra_actual) - self.r_izquierdo_posicion
			#movemos la letra desde el principio del alfabeto (el reflector no tiene clave) las posiciones del desplazamiento
			try:
				letra_actual = self.alfabeto[desplazamiento_actual]
			except IndexError as e:
				letra_actual = self.alfabeto[desplazamiento_actual - 26]
			#hacemos la sustitución del reflector
			letra_actual = self.reflector[self.alfabeto.index(letra_actual)]

			#el desplazamiento hacia el ROTOR IZQUIERDO se calcula usando la posición en el alfabeto de nuestra letra actual
			desplazamiento_actual = self.alfabeto.index(letra_actual)
			#movemos la letra desde la clave del rotor izquierdo las posiciones del desplazamiento (dentro del alfabeto natural)
			try:
				letra_actual = self.alfabeto[self.r_izquierdo_posicion + desplazamiento_actual]
			except IndexError as e:
				letra_actual = self.alfabeto[self.r_izquierdo_posicion + desplazamiento_actual - 26]
			#encontramos la posición de esta letra en el rotor izquierdo y hacemos la sustitución 
			letra_actual = self.alfabeto[self.r_izquierdo.index(letra_actual)]

			#el desplazamiento hacia el ROTOR CENTRAL se calcula usando la posición en el alfabeto de nuestra letra actual y de la posición del rotor izquierdo
			desplazamiento_actual = self.alfabeto.index(letra_actual) - self.r_izquierdo_posicion
			#movemos la letra desde la clave del rotor central las posiciones del desplazamiento (dentro del alfabeto natural)
			try:
				letra_actual = self.alfabeto[self.r_central_posicion + desplazamiento_actual]
			except IndexError as e:
				letra_actual = self.alfabeto[self.r_central_posicion + desplazamiento_actual - 26]
			#encontramos la posición de esta letra en el rotor central y hacemos la sustitución
			letra_actual = self.alfabeto[self.r_central.index(letra_actual)]

			#el desplazamiento hacia el ROTOR DERECHO se calcula usando la posición en el alfabeto de nuestra letra actual y de la posición del rotor central
			desplazamiento_actual = self.alfabeto.index(letra_actual) - self.r_central_posicion
			#movemos la letra desde la clave del rotor derecho las posiciones del desplazamiento (dentro del alfabeto natural)
			try:
				letra_actual = self.alfabeto[self.r_derecho_posicion + desplazamiento_actual]
			except IndexError as e:
				letra_actual = self.alfabeto[self.r_derecho_posicion + desplazamiento_actual - 26]
			#encontramos la posición de esta letra en el rotor derecho y hacemos la sustitución
			letra_actual = self.alfabeto[self.r_derecho.index(letra_actual)]

			#el desplazamiento hacia el CLAVIJERO se calcula usando la posición en el alfabeto de nuestra letra actual y de la posición del rotor derecho
			desplazamiento_actual = self.alfabeto.index(letra_actual) - self.r_derecho_posicion
			#movemos la letra desde el inicio del alfabeto (el clavijero no tiene claves, al contrario que los rotores)
			try:	
				letra_actual = self.alfabeto[desplazamiento_actual]
			except IndexError as e:
				letra_actual = self.alfabeto[desplazamiento_actual - 26]
			#si esta letra está conectada a otra clavija, hacemos la sustitución



			texto_codificado += letra_actual
		return texto_codificado
			

