import time
import os
from Processes.Process import Process

# Clase que representa un proceso
class RR:
    def __init__(procesos):
        None

    # Función para limpiar la consola
    def limpiar_consola():
        os.system('clear')

    # Función para mostrar la tabla en tiempo real
    def mostrar_tabla(procesos, tiempo_actual, cola_procesos):
        RR.limpiar_consola()  # Limpiar la consola antes de mostrar la tabla actualizada
        print(f"Tiempo actual: {tiempo_actual}")
        print(f"{'Proceso':<10}{'Llegada':<10}{'Ejecución':<10}{'Comienzo':<10}{'Restante':<10}{'Final':<10}{'Espera':<10}{'Retorno':<10}")
        for proceso in procesos:
            # Mostrar la información de los procesos, aún si no han comenzado
            comienzo = proceso.tiempo_comienzo if proceso.tiempo_comienzo != -1 else ""
            final = proceso.tiempo_finalizacion if proceso.tiempo_finalizacion != 0 else ""
            print(f"{proceso.nombre:<10}{proceso.tiempo_llegada:<10}{proceso.tiempo_ejecucion:<10}{comienzo:<10}{proceso.tiempo_restante:<10}{final:<10}{proceso.tiempo_espera:<10}{proceso.tiempo_retorno:<10}")
    
        # Mostrar los procesos en cola
        print("\nProcesos en cola: ", [proceso.nombre for proceso in cola_procesos])

    # Función para ejecutar Round Robin en tiempo real
    def round_robin_real_time(procesos, quantum):
        tiempo_actual = 0
        cola_procesos = []
        finalizados = []
        todos_procesos = procesos[:]  # Copia para mostrar todos los procesos desde el principio
    
        while procesos or cola_procesos:
            # Añadir procesos que han llegado al sistema al tiempo actual
            for proceso in procesos[:]:
                if proceso.tiempo_llegada <= tiempo_actual:
                    cola_procesos.append(proceso)
                    procesos.remove(proceso)
        
            if cola_procesos:
                # Tomar el primer proceso de la cola
                proceso_actual = cola_procesos.pop(0)
            
                # Si el proceso nunca ha comenzado, se marca el tiempo de inicio
                if proceso_actual.tiempo_comienzo == -1:
                    proceso_actual.tiempo_comienzo = tiempo_actual
            
                # Ejecutar el proceso por el tiempo del quantum o el tiempo restante del proceso
                tiempo_a_ejecutar = min(quantum, proceso_actual.tiempo_restante)
            
                for _ in range(tiempo_a_ejecutar):
                    time.sleep(1)  # Simulación de 1 segundo por unidad de tiempo
                    tiempo_actual += 1
                    proceso_actual.tiempo_restante -= 1
                    RR.mostrar_tabla(todos_procesos, tiempo_actual, cola_procesos)
            
                for proceso in procesos[:]:
                    if proceso.tiempo_llegada <= tiempo_actual:
                        cola_procesos.append(proceso)
                        procesos.remove(proceso)
    
                # Si el proceso ha terminado
                if proceso_actual.tiempo_restante == 0:
                    proceso_actual.tiempo_finalizacion = tiempo_actual
                    proceso_actual.tiempo_retorno = proceso_actual.tiempo_finalizacion - proceso_actual.tiempo_llegada
                    proceso_actual.tiempo_espera = proceso_actual.tiempo_retorno - proceso_actual.tiempo_ejecucion
                    finalizados.append(proceso_actual)
                else:
                    # Si no ha terminado, se vuelve a añadir al final de la cola
                    cola_procesos.append(proceso_actual)
            else:
                RR.mostrar_tabla(todos_procesos, tiempo_actual, cola_procesos)
                # Si no hay procesos en la cola, avanzar el tiempo al siguiente proceso que llegue
                time.sleep(1) 
                tiempo_actual += 1

        return finalizados

# Lista de procesos
procesos = [
    Process("P1", 12, 5),
    Process("P2", 6, 1),
    Process("P3", 6, 4),
    Process("P4", 5, 12)
]

# Quantum de tiempo
quantum = 3

# Ejecutar algoritmo Round Robin en tiempo real
procesos_finalizados = RR.round_robin_real_time(procesos, quantum)

# Mostrar la tabla final después de que todos los procesos hayan terminado
RR.mostrar_tabla(procesos_finalizados, tiempo_actual="Final", cola_procesos=[])
