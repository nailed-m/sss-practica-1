


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
	

	def codifica(self, texto):
		texto_codificado = ""
		letra_actual = ""
		desplazamiento_actual = 0

		#TO DO
		#pulsamos la primera letra
		letra_actual=texto[0]
		#movemos el rotor derecho
		self.r_derecho_posicion+=1
		#si forma parte de una clavija, se hace la sustitución

		
		#el desplazamiento hacia el rotor derecho se calcula con la posición de la letra en el string del alfabeto
		desplazamiento_actual = self.alfabeto.index(texto[0])
		#movemos la letra desde la clave del rotor derecho las posiciones del desplazamiento
		letra_actual = self.alfabeto[self.r_derecho_posicion + desplazamiento_actual]
		#hacemos la sustitución con el rotor derecho
		letra_actual = self.r_derecho[self.alfabeto.index(letra_actual)]

		#el desplazamiento hacia el rotor central se calcula usando la posición en el alfabeto de nuestra letra actual y de la posición del rotor derecho
		desplazamiento_actual = self.alfabeto.index(letra_actual) - self.r_derecho_posicion
		#movemos la letra desde la clave del rotor central las posiciones del desplazamiento
		letra_actual = self.alfabeto[self.r_central_posicion + desplazamiento_actual]
		#hacemos la sustitución con el rotor central
		letra_actual = self.r_central[self.alfabeto.index(letra_actual)]

		#el desplazamiento hacia el rotor izquierdo se calcula usando la posición en el alfabeto de nuestra letra actual y de la posición del rotor central
		desplazamiento_actual = self.alfabeto.index(letra_actual) - self.r_central_posicion
		#movemos la letra desde la clave del rotor izquierdo las posiciones del desplazamiento
		letra_actual = self.alfabeto[self.r_izquierdo_posicion + desplazamiento_actual]
		#hacemos la sustitución con el rotor izquierdo
		letra_actual = self.r_izquierdo[self.alfabeto.index(letra_actual)]

		#el desplazamiento hacia el reflector se calcula usando la posición en el alfabeto de nuestra letra actual y de la posición del rotor izquierdo
		desplazamiento_actual = self.alfabeto.index(letra_actual) - self.r_izquierdo_posicion
		#movemos la letra desde el principio del alfabeto (el reflector no tiene clave) las posiciones del desplazamiento
		letra_actual = self.alfabeto[desplazamiento_actual]
		#hacemos la sustitución con el reflector
		letra_actual = self.reflector[self.alfabeto.index(letra_actual)]

		texto_codificado += letra_actual
		return texto_codificado
			

