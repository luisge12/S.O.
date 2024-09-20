import time
import os
import random
from Processes.Process import Process

class PrioridadNE:

	# Función para limpiar la consola
	@staticmethod
	def limpiar_consola() -> None:
		os.system('clear')

	# Función para mostrar la tabla en tiempo real
	@staticmethod
	def mostrar_tabla(procesos, tiempo_actual, cola_listos, cola_terminado, proceso_actual) -> None:
		PrioridadNE.limpiar_consola()  # Limpiar la consola antes de mostrar la tabla actualizada
		print(f"Tiempo actual: {tiempo_actual}")
		print(f"{'Proceso':<10}{'Llegada':<10}{'Prioridad':<10}{'Ejecución':<10}{'Comienzo':<10}{'Restante':<10}{'Final':<10}{'Espera':<10}{'Retorno':<10}")
		for proceso in procesos:
			# Mostrar la información de los procesos, aún si no han comenzado
			comienzo = proceso.tiempo_comienzo if proceso.tiempo_comienzo != -1 else ""
			final = proceso.tiempo_finalizacion if proceso.tiempo_finalizacion != 0 else ""
			print(f"{proceso.nombre:<10}{proceso.tiempo_llegada:<10}{proceso.prioridad:<10}{proceso.tiempo_ejecucion:<10}{comienzo:<10}{proceso.tiempo_restante:<10}{final:<10}{proceso.tiempo_espera:<10}{proceso.tiempo_retorno:<10}")
    
        # Mostrar el proceso en ejecucion, los procesos en cola de listos y los procesos terminados
		print("\nProceso en ejecucion: ", proceso_actual.nombre if proceso_actual else '')
		print("Procesos en cola de listos: ", [proceso.nombre for proceso in cola_listos])
		print("Procesos terminados: ", [proceso.nombre for proceso in cola_terminado])

	@staticmethod
	def generar_prioridad(procesos: list) -> list:
		# codigo para generar los numeros de prioridades
		copia = procesos[:]
		prioridades = list(range(1, (len(copia) + 1)))
		# cabiamos el orden del arreglo para parecer que la asignacion de prioridades es aleatoria
		random.shuffle(prioridades)
		#asignamos las prioridades a cada uno de los procesos
		for i in range(len(copia)):
			copia[i].prioridad = prioridades[i]

		return copia

	@staticmethod
	def prioridad_no_expulsiva_real_time(procesos) -> list:
		tiempo_actual = 0
		todos_procesos = PrioridadNE.generar_prioridad(procesos)
		cola_listos = []
		cola_terminado = []
		proceso_actual = None

		while True:
			# si el tiempo de llegada del proceso es igual al tiempo del simulador, lo agregaos en la cola de listos
			for i in range(len(todos_procesos)):
				if todos_procesos[i].tiempo_llegada == tiempo_actual:
					cola_listos.append(todos_procesos[i])
			# si hay uno o mas proceso en la cola de listos, los ordenamos de manera ascendente segun su peso
			if len(cola_listos) > 0:
				cola_listos.sort(key = lambda proceso: proceso.prioridad)
				# proceso_actual almacena el proceso que se va a ejecutar
				if not proceso_actual:
					proceso_actual = cola_listos.pop(0)
					proceso_actual.tiempo_comienzo = tiempo_actual
			#imprimimos la informacion de los procesos
			PrioridadNE.mostrar_tabla(todos_procesos, tiempo_actual, cola_listos, cola_terminado, proceso_actual)

			tiempo_actual += 1 #aumentamos nuestro contador de tiempo
			time.sleep(1)  # Esperar 1 segundo para simular el paso del tiempo real

			if proceso_actual:
				proceso_actual.tiempo_restante -= 1 # si se esta ejecutando un proceso decrementamos el valor de tiempo restante
				# al finalizar la ejecucion del proceso actualizamos sus valores de tiempo y lo agregamos en la lista de terminados
				if proceso_actual.tiempo_restante == 0: 
					proceso_actual.tiempo_finalizacion = tiempo_actual
					proceso_actual.tiempo_retorno = proceso_actual.tiempo_finalizacion - proceso_actual.tiempo_llegada
					proceso_actual.tiempo_espera = proceso_actual.tiempo_comienzo - proceso_actual.tiempo_llegada
					cola_terminado.append(proceso_actual)
					proceso_actual = None
			# si terminaron la ejecucion todos nuestros procesos, imprimimos por ultima vez la tabla de valores
			if not proceso_actual and len(cola_terminado) == len(todos_procesos):
				PrioridadNE.mostrar_tabla(todos_procesos, tiempo_actual, cola_listos, cola_terminado, proceso_actual)
				break

		return todos_procesos



# Lista de procesos
procesos = [
    Process("P1", 0, 7),
    Process("P2", 2, 4),
    Process("P3", 3, 3),
    Process("P4", 5, 2)
]

PrioridadNE.prioridad_no_expulsiva_real_time(procesos)