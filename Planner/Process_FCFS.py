import time
import os
from Processes.Process import Process

class FCFS:
    def __init__(procesos):
        None
    
    
    # Función para limpiar la consola
    def limpiar_consola():
        os.system('clear')

    # Función para mostrar la tabla en tiempo real
    def mostrar_tabla(procesos, tiempo_actual):
        FCFS.limpiar_consola()  # Limpiar la consola antes de mostrar la tabla actualizada
        print(f"Tiempo actual: {tiempo_actual}")
        print(f"{'Proceso':<10}{'Llegada':<10}{'Ejecución':<10}{'Comienzo':<10}{'Restante':<10}{'Final':<10}{'Espera':<10}{'Retorno':<10}")
        for proceso in procesos:
            print(f"{proceso.nombre:<10}{proceso.tiempo_llegada:<10}{proceso.tiempo_ejecucion:<10}{proceso.tiempo_comienzo:<10}{proceso.tiempo_restante:<10}{proceso.tiempo_finalizacion:<10}{proceso.tiempo_espera:<10}{proceso.tiempo_retorno:<10}")
    
    # Función para calcular FCFS en tiempo real
    def fcfs_real_time(procesos):
        procesos = sorted(procesos, key=lambda p: p.tiempo_llegada)
        tiempo_actual = 0
        for proceso in procesos:
            
            proceso.tiempo_comienzo = tiempo_actual
            while proceso.tiempo_restante > 0:
                # Simular la ejecución de cada segundo del proceso
                FCFS.mostrar_tabla(procesos, tiempo_actual)
                
                proceso.tiempo_restante -= 1
                tiempo_actual += 1
                time.sleep(1)  # Esperar 1 segundo para simular el paso del tiempo real
            proceso.tiempo_finalizacion = tiempo_actual
            proceso.tiempo_retorno = proceso.tiempo_finalizacion - proceso.tiempo_llegada
            proceso.tiempo_espera = proceso.tiempo_comienzo - proceso.tiempo_llegada

# Lista de procesos
procesos = [
Process("P1",0,3),
Process("P2",5,4),
Process("P3",2,3),
Process("P4",4,2)
]

# Ejecutar algoritmo FCFS en tiempo real
FCFS.fcfs_real_time(procesos)

# Mostrar la tabla final después de que todos los procesos hayan terminado
FCFS.mostrar_tabla(procesos, tiempo_actual="Final")
