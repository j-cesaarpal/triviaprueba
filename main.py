import random  #Importamos la libreria random
import time  # Importamos la librería time
#Para el tiempo utilize la librería time en el cual se esperara 3 segundos para continuar
print("Empezamos...")
time.sleep(2)
#Definimos los colores de los titulos para que se diferencien
BLUE = '\033[34m'
GREEN = '\033[32m'
RED = '\033[31m'
YELLOW = '\033[33m'
RESET = '\033[39m'
# Para implementar puntajes, crearemos una nueva variable llamada "puntaje", la que inicializamos en 0.
puntaje = random.randint(0, 10)

iniciar_trivia = True  # Iniciamos la variable en True
intentos = 0  # variable que almacenará el número de veces que el usuario intenta nuestra trivia.

# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print ("Bienvenido a mi trivia sobre computación")
time.sleep(1)
print ("Pondremos a prueba tus conocimientos")
time.sleep(1)
print("Tienes", puntaje, "puntos, para empezar\n")

# Agregaremos personalización para nuestros jugadores, preguntando y almacenando sus nombres en una variable

nombre = input("Ingresa tu nombre: ")

# Es importante dar instrucciones sobre cómo jugar:
# Ahora, lo personalizaremos con el nombre del jugador, diciéndole a print() que muestre el contenido de la variable "nombre". Cada cosa distinta que queremos que muestre en la pantalla, la separamos con comas
print ("\n Hola", nombre, "responde las siguientes preguntas escribiendo \nla letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n")
# OJO, el \n al final de la línea 6 es para dar un "salto de línea"
print("Entonces", nombre, "comenzamos con las preguntas")
time.sleep(1)
while iniciar_trivia == True:  #  Mientras iniciar_trivia sea True, repite:
	intentos += 1
	puntaje = 0
	print("\nIntento número:", intentos)
	input("Presiona Enter para continuar\n")
	print("Primera pregunta de la Trivia\n")
	# Pregunta 1
	print(BLUE + "1.- ¿Quién creo python?\n" + RESET)
	print("a) Steve Jobs")
	print("b) Guido van Rossum")
	print("c) Bill Gates")
	print("d) Paul Allen")
    
	# Almacenamos la respuesta del usuario en la variable "respuesta_1"

	respuesta_1 = input("\nTu respuesta: ")
	while respuesta_1 not in ("b","B"):
		respuesta_1 = input(
		    "No es la respuesta correcta.\n\nIngresa nuevamente tu respuesta: "
		)
	# Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
	if respuesta_1 == "b" or respuesta_1 == "B":
		puntaje += 10
		print("Muy bien", nombre, "!\n")
	else:
		print("Incorrecto", nombre, "!\n")

	print(nombre, "llevas", puntaje, "puntos\n")
	# Pregunta 2
	print(BLUE +"2.- ¿Cual NO es un lenguaje de programación?\n" +RESET)
	print("a) python")
	print("b) java")
	print("c) github")
	print("d) Java Script")
        
	# Almacenamos la respuesta del usuario en la variable "respuesta_2"
	respuesta_2 = input("\nTu respuesta: ")
	while respuesta_2 not in ("c","C"):
		respuesta_2 = input(
		    "No es la respuesta correcta.\n\nIngresa nuevamente tu respuesta: "
		)
	# Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
	if respuesta_2 == "a":
		print("Incorrecto!", nombre,
		      "python si es un lenguaje de programación")
	elif respuesta_2 == "b":
		print("Incorrecto!", nombre,
		      "java si es un lenguaje de programación")
	elif respuesta_2 == "d":
		print(
		    "Incorrecto!", nombre,
		    "java script si es un lenguaje de programación")
	else:
		puntaje += 10
		print(
		    "Muy bien!", nombre,
		    "\ngithub no es un lenguaje de programacion\n"
		)

	print(nombre, "llevas", puntaje, "puntos\n")
	# Pregunta 3
	print(BLUE + "3.- ¿Python es?" + RESET)
	print("3.- ¿Python es?")
	print("a) Lenguaje de programación")
	print("b) conjunto de herramientas de edición")
	print("c) Gestor de base de datos")
	print("d) Framework para aplicaciones web")
	# Almacenamos la respuesta del usuario en la variable "respuesta_3"
	respuesta_3 = input("\nTu respuesta: ")
	while respuesta_3 not in ("a","A"):
		respuesta_3 = input(
		    "No es la respuesta correcta.\n\nIngresa nuevamente tu respuesta: "
		)
	if respuesta_3 == "c":
		print("Totalmente incorrecto!\n")
		puntaje = puntaje / 2
	elif respuesta_3 == "b":
		print("Incorrecto\n")
		puntaje = puntaje + 5
	elif respuesta_3 == "d":
		print("Incorrecto!\n")
		puntaje = puntaje - 5
	else:
		print("Correcto!\n")
		puntaje = puntaje * 2

	print(nombre, "tienes", puntaje, "puntos\n")

	time.sleep(2)  # para ayudarnos a imaginar que vamos jugando
	print("Jugando la Trivia de computación")
	time.sleep(2)
	puntaje = puntaje + 0  # Se dara el total del puntaje en el desarrollo de la trivia
	print(YELLOW + "Excelente, has obtenido", puntaje, "puntos" + RESET)

	print("\n¿Deseas intentar la trivia nuevamente?")
	repetir_trivia = input(
	    "Ingresa 'si' para repetir, o cualquier tecla para finalizar: "
	).lower()

	if repetir_trivia != "si":  # != significa "distinto"
		print(BLUE + "\nEspero", nombre,
		      "que lo hayas pasado bien, hasta pronto!" + RESET)
		iniciar_trivia = False  # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.
