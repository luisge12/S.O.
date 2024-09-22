import time
import os
import random
#from Processes.Process import Process

class FCFS:
    def __init__(self):
        None

    @staticmethod
    def limpiar_consola():
        os.system('clear')

    @staticmethod
    def mostrar_tabla(procesos, tiempo_actual):
        FCFS.limpiar_consola()
        print(f"Tiempo actual: {tiempo_actual}")
        print(f"{'Proceso':<10}{'Llegada':<10}{'Ejecución':<10}{'Comienzo':<10}{'Restante':<10}{'Final':<10}{'Espera':<10}{'Retorno':<10}")
        for proceso in procesos:
            proceso.tiempo_comienzo = proceso.tiempo_comienzo if proceso.tiempo_comienzo != -1 else ""
            proceso.tiempo_finalizacion = proceso.tiempo_finalizacion if proceso.tiempo_finalizacion != 0 else ""
            print(f"{proceso.nombre:<10}{proceso.tiempo_llegada:<10}{proceso.tiempo_ejecucion:<10}{proceso.tiempo_comienzo:<10}{proceso.tiempo_restante:<10}{proceso.tiempo_finalizacion:<10}{proceso.tiempo_espera:<10}{proceso.tiempo_retorno:<10}")

    @staticmethod
    def fcfs_real_time(processes):
        procesos = processes
        tiempo_actual = 0
        procesos = sorted(procesos, key=lambda p: p.tiempo_llegada)
        resultados_en_tiempo_real = []

        for proceso in procesos:
            # Esperar hasta que el proceso llegue
            if tiempo_actual < proceso.tiempo_llegada:
                while tiempo_actual < proceso.tiempo_llegada:
                    FCFS.mostrar_tabla(procesos, tiempo_actual)
                    tiempo_actual += 1

            # Iniciar el proceso cuando llega su tiempo de llegada
            proceso.tiempo_comienzo = tiempo_actual
            proceso.tiempo_restante = proceso.tiempo_ejecucion

            while proceso.tiempo_restante > 0:
                # Simular la ejecución de cada segundo del proceso
                time.sleep(1)  # Esperar 1 segundo para simular el paso del tiempo real
                proceso.tiempo_restante -= 1
                tiempo_actual += 1
                # Guardar el estado actual del proceso
                estado_actual = {
                    "nombre": proceso.nombre,
                    "tiempo_llegada": proceso.tiempo_llegada,
                    "tiempo_ejecucion": proceso.tiempo_ejecucion,
                    "tiempo_comienzo": proceso.tiempo_comienzo,
                    "tiempo_restante": proceso.tiempo_restante,
                    "tiempo_finalizacion": proceso.tiempo_finalizacion,
                    "tiempo_espera": proceso.tiempo_espera,
                    "tiempo_retorno": proceso.tiempo_retorno,
                    "prioridad" : 0
                }
                resultados_en_tiempo_real.append(estado_actual)
                FCFS.mostrar_tabla(procesos, tiempo_actual)

            proceso.tiempo_finalizacion = tiempo_actual
            proceso.tiempo_retorno = proceso.tiempo_finalizacion - proceso.tiempo_llegada
            proceso.tiempo_espera = proceso.tiempo_comienzo - proceso.tiempo_llegada
            estado_actual = {
                    "nombre": proceso.nombre,
                    "tiempo_llegada": proceso.tiempo_llegada,
                    "tiempo_ejecucion": proceso.tiempo_ejecucion,
                    "tiempo_comienzo": proceso.tiempo_comienzo,
                    "tiempo_restante": proceso.tiempo_restante,
                    "tiempo_finalizacion": proceso.tiempo_finalizacion,
                    "tiempo_espera": proceso.tiempo_espera,
                    "tiempo_retorno": proceso.tiempo_retorno,
                    "prioridad" : 0
                }
            resultados_en_tiempo_real.append(estado_actual)
        return resultados_en_tiempo_real 
    
    
class SJF:  # Short Job First
    def __init__(self):
        None

    @staticmethod
    def limpiar_consola():
        os.system('clear')

    @staticmethod
    def mostrar_tabla(procesos, tiempo_actual):
        SJF.limpiar_consola()
        print(f"Tiempo actual: {tiempo_actual}")
        print(f"{'Proceso':<10}{'Llegada':<10}{'Ejecución':<10}{'Comienzo':<10}{'Restante':<10}{'Final':<10}{'Espera':<10}{'Retorno':<10}")
        for proceso in procesos:
            proceso.tiempo_comienzo = proceso.tiempo_comienzo if proceso.tiempo_comienzo != -1 else ""
            proceso.tiempo_finalizacion = proceso.tiempo_finalizacion if proceso.tiempo_finalizacion != 0 else ""
            print(f"{proceso.nombre:<10}{proceso.tiempo_llegada:<10}{proceso.tiempo_ejecucion:<10}{proceso.tiempo_comienzo:<10}{proceso.tiempo_restante:<10}{proceso.tiempo_finalizacion:<10}{proceso.tiempo_espera:<10}{proceso.tiempo_retorno:<10}")

    @staticmethod
    def sjf_real_time(processes):
        procesos = processes
        tiempo_actual = 0
        procesos_restantes = procesos.copy()
        resultados_en_tiempo_real = []  # Lista para almacenar los resultados en tiempo real

        while procesos_restantes:
            # Filtrar los procesos que ya han llegado
            procesos_llegados = [p for p in procesos_restantes if p.tiempo_llegada <= tiempo_actual]

            if procesos_llegados:
                # Seleccionar el proceso con el tiempo de ejecución más corto
                proceso_a_ejecutar = min(procesos_llegados, key=lambda p: p.tiempo_ejecucion)

                # Simular la ejecución del proceso en tiempo real
                proceso_a_ejecutar.tiempo_comienzo = max(tiempo_actual, proceso_a_ejecutar.tiempo_llegada)
                while proceso_a_ejecutar.tiempo_restante > 0:
                    SJF.mostrar_tabla(procesos, tiempo_actual)  # Mostrar la tabla actualizada
                    time.sleep(1)  # Esperar 1 segundo para simular el paso del tiempo
                    proceso_a_ejecutar.tiempo_restante -= 1
                    tiempo_actual += 1

                    # Guardar el estado actual del proceso
                    estado_actual = {
                        "nombre": proceso_a_ejecutar.nombre,
                        "tiempo_llegada": proceso_a_ejecutar.tiempo_llegada,
                        "tiempo_ejecucion": proceso_a_ejecutar.tiempo_ejecucion,
                        "tiempo_comienzo": proceso_a_ejecutar.tiempo_comienzo,
                        "tiempo_restante": proceso_a_ejecutar.tiempo_restante,
                        "tiempo_finalizacion": proceso_a_ejecutar.tiempo_finalizacion,
                        "tiempo_espera": proceso_a_ejecutar.tiempo_espera,
                        "tiempo_retorno": proceso_a_ejecutar.tiempo_retorno,
                        "prioridad" : 0
                    }
                    resultados_en_tiempo_real.append(estado_actual)

                # Calcular los tiempos finales del proceso
                proceso_a_ejecutar.tiempo_finalizacion = tiempo_actual
                proceso_a_ejecutar.tiempo_retorno = proceso_a_ejecutar.tiempo_finalizacion - proceso_a_ejecutar.tiempo_llegada
                proceso_a_ejecutar.tiempo_espera = proceso_a_ejecutar.tiempo_comienzo - proceso_a_ejecutar.tiempo_llegada
                estado_actual = {
                    "nombre": proceso_a_ejecutar.nombre,
                    "tiempo_llegada": proceso_a_ejecutar.tiempo_llegada,
                    "tiempo_ejecucion": proceso_a_ejecutar.tiempo_ejecucion,
                    "tiempo_comienzo": proceso_a_ejecutar.tiempo_comienzo,
                    "tiempo_restante": proceso_a_ejecutar.tiempo_restante,
                    "tiempo_finalizacion": proceso_a_ejecutar.tiempo_finalizacion,
                    "tiempo_espera": proceso_a_ejecutar.tiempo_espera,
                    "tiempo_retorno": proceso_a_ejecutar.tiempo_retorno,
                    "prioridad" : 0
                }
                resultados_en_tiempo_real.append(estado_actual)
                # Añadir el proceso a la lista de procesos ordenados y removerlo de los pendientes
                procesos_restantes.remove(proceso_a_ejecutar)
            else:
                # Si no hay procesos que hayan llegado, avanzar el tiempo
                SJF.mostrar_tabla(procesos, tiempo_actual)  # Mostrar la tabla actualizada

                tiempo_actual += 1

        return resultados_en_tiempo_real
    


class SA:  # Random Selection
    def __init__(self):
        None

    @staticmethod
    def limpiar_consola():
        os.system('clear')

    @staticmethod
    def mostrar_tabla(procesos, tiempo_actual, procesos_disponibles):
        SA.limpiar_consola()
        print(f"Tiempo actual: {tiempo_actual}")
        print(f"{'Proceso':<10}{'Llegada':<10}{'Ejecución':<10}{'Comienzo':<10}{'Restante':<10}{'Final':<10}{'Espera':<10}{'Retorno':<10}")
        for proceso in procesos:
            comienzo = proceso.tiempo_comienzo if proceso.tiempo_comienzo != -1 else ""
            final = proceso.tiempo_finalizacion if proceso.tiempo_finalizacion != 0 else ""
            print(f"{proceso.nombre:<10}{proceso.tiempo_llegada:<10}{proceso.tiempo_ejecucion:<10}{comienzo:<10}{proceso.tiempo_restante:<10}{final:<10}{proceso.tiempo_espera:<10}{proceso.tiempo_retorno:<10}")

        # Mostrar los procesos disponibles
        print("\nProcesos disponibles: ", [proceso.nombre for proceso in procesos_disponibles])

    @staticmethod
    def seleccion_aleatoria_real_time(processes):
        procesos = processes
        tiempo_actual = 0
        procesos_restantes = procesos.copy()
        resultados_en_tiempo_real = []  # Lista para almacenar los resultados en tiempo real

        while procesos_restantes:
            # Filtrar los procesos que ya han llegado
            procesos_disponibles = [p for p in procesos_restantes if p.tiempo_llegada <= tiempo_actual]

            if procesos_disponibles:
                # Elegir un proceso aleatorio entre los disponibles
                proceso_actual = random.choice(procesos_disponibles)

                # Marcar el tiempo de comienzo
                proceso_actual.tiempo_comienzo = max(tiempo_actual, proceso_actual.tiempo_llegada)
                while proceso_actual.tiempo_restante > 0:
                    SA.mostrar_tabla(procesos, tiempo_actual, procesos_disponibles)  # Mostrar la tabla actualizada

                    proceso_actual.tiempo_restante -= 1
                    tiempo_actual += 1

                    # Guardar el estado actual del proceso
                    estado_actual = {
                        "nombre": proceso_actual.nombre,
                        "tiempo_llegada": proceso_actual.tiempo_llegada,
                        "tiempo_ejecucion": proceso_actual.tiempo_ejecucion,
                        "tiempo_comienzo": proceso_actual.tiempo_comienzo,
                        "tiempo_finalizacion": proceso_actual.tiempo_finalizacion,
                        "tiempo_espera": proceso_actual.tiempo_espera,
                        "tiempo_retorno": proceso_actual.tiempo_retorno,
                        "prioridad" : 0
                    }
                    resultados_en_tiempo_real.append(estado_actual)

                # Calcular los tiempos finales del proceso
                proceso_actual.tiempo_finalizacion = tiempo_actual
                proceso_actual.tiempo_retorno = proceso_actual.tiempo_finalizacion - proceso_actual.tiempo_llegada
                proceso_actual.tiempo_espera = proceso_actual.tiempo_retorno - proceso_actual.tiempo_ejecucion
                
                # Guardar resultados finales del proceso
                estado_final = {
                    "nombre": proceso_actual.nombre,
                    "tiempo_llegada": proceso_actual.tiempo_llegada,
                    "tiempo_ejecucion": proceso_actual.tiempo_ejecucion,
                    "tiempo_comienzo": proceso_actual.tiempo_comienzo,
                    "tiempo_finalizacion": proceso_actual.tiempo_finalizacion,
                    "tiempo_espera": proceso_actual.tiempo_espera,
                    "tiempo_retorno": proceso_actual.tiempo_retorno,
                    "prioridad" : 0
                }
                resultados_en_tiempo_real.append(estado_final)
                
                # Remover el proceso de los pendientes
                procesos_restantes.remove(proceso_actual)
            else:
                # Si no hay procesos que hayan llegado, avanzar el tiempo
                SA.mostrar_tabla(procesos, tiempo_actual, procesos_disponibles)  # Mostrar la tabla actualizada
                time.sleep(1)
                tiempo_actual += 1

        return resultados_en_tiempo_real  # Retornar solo los resultados

 
    
class PrioridadNE:

    @staticmethod
    def limpiar_consola() -> None:
        os.system('clear')

    @staticmethod
    def mostrar_tabla(procesos, tiempo_actual, cola_listos, cola_terminado, proceso_actual, tiempo_cpu=None) -> None:
        PrioridadNE.limpiar_consola()
        print(f"Tiempo actual: {tiempo_actual}")
        print(f"{'Proceso':<10}{'Llegada':<10}{'Prioridad':<10}{'Ejecución':<10}{'Comienzo':<10}{'Restante':<10}{'Final':<10}{'Espera':<10}{'Retorno':<10}")
        for proceso in procesos:
            comienzo = proceso.tiempo_comienzo if proceso.tiempo_comienzo != -1 else ""
            final = proceso.tiempo_finalizacion if proceso.tiempo_finalizacion != 0 else ""
            print(f"{proceso.nombre:<10}{proceso.tiempo_llegada:<10}{proceso.prioridad:<10}{proceso.tiempo_ejecucion:<10}{comienzo:<10}{proceso.tiempo_restante:<10}{final:<10}{proceso.tiempo_espera:<10}{proceso.tiempo_retorno:<10}")
    
        print("\nProceso en ejecucion: ", proceso_actual.nombre if proceso_actual else '')
        print("Procesos en cola de listos: ", [proceso.nombre for proceso in cola_listos])
        print("Procesos terminados: ", [proceso.nombre for proceso in cola_terminado])
        print("Tiempo total de la CPU: ", tiempo_cpu if tiempo_cpu else '')

    @staticmethod
    def generar_prioridad(procesos: list) -> list:
        copia = procesos[:]
        for i in range(len(copia)):
            copia[i].prioridad = random.randint(1, len(copia))
        return copia

    @staticmethod
    def prioridad_no_expulsiva_real_time(processes) -> list:
        procesos = processes
        tiempo_actual = 0
        todos_procesos = PrioridadNE.generar_prioridad(procesos)
        cola_listos = []
        cola_terminado = []
        proceso_actual = None
        resultados_en_tiempo_real = []  # Lista para almacenar resultados en tiempo real

        while True:
            for i in range(len(todos_procesos)):
                if todos_procesos[i].tiempo_llegada == tiempo_actual:
                    cola_listos.append(todos_procesos[i])
            if len(cola_listos) > 0:
                cola_listos.sort(key=lambda proceso: proceso.prioridad)
                if not proceso_actual:
                    proceso_actual = cola_listos.pop(0)
                    proceso_actual.tiempo_comienzo = tiempo_actual

            PrioridadNE.mostrar_tabla(todos_procesos, tiempo_actual, cola_listos, cola_terminado, proceso_actual)
            tiempo_actual += 1


            if proceso_actual:
                proceso_actual.tiempo_restante -= 1
                
                estado_actual = {
                    "nombre": proceso_actual.nombre,
                    "tiempo_llegada": proceso_actual.tiempo_llegada,
                    "tiempo_ejecucion": proceso_actual.tiempo_ejecucion,
                    "prioridad": proceso_actual.prioridad,
                    "tiempo_comienzo": proceso_actual.tiempo_comienzo,
                    "tiempo_restante": proceso_actual.tiempo_restante,
                    "tiempo_finalizacion": proceso_actual.tiempo_finalizacion,
                    "tiempo_espera": proceso_actual.tiempo_espera,
                    "tiempo_retorno": proceso_actual.tiempo_retorno,
                    "prioridad" : 0
                }
                resultados_en_tiempo_real.append(estado_actual)

                if proceso_actual.tiempo_restante == 0: 
                    proceso_actual.tiempo_finalizacion = tiempo_actual
                    proceso_actual.tiempo_retorno = proceso_actual.tiempo_finalizacion - proceso_actual.tiempo_llegada
                    proceso_actual.tiempo_espera = proceso_actual.tiempo_comienzo - proceso_actual.tiempo_llegada
                    estado_actual = {
                        "nombre": proceso_actual.nombre,
                        "tiempo_llegada": proceso_actual.tiempo_llegada,
                        "tiempo_ejecucion": proceso_actual.tiempo_ejecucion,
                        "prioridad": proceso_actual.prioridad,
                        "tiempo_comienzo": proceso_actual.tiempo_comienzo,
                        "tiempo_restante": proceso_actual.tiempo_restante,
                        "tiempo_finalizacion": proceso_actual.tiempo_finalizacion,
                        "tiempo_espera": proceso_actual.tiempo_espera,
                        "tiempo_retorno": proceso_actual.tiempo_retorno,
                        "prioridad" : 0
                    }
                    resultados_en_tiempo_real.append(estado_actual)
                    cola_terminado.append(proceso_actual)
                    proceso_actual = None

            if not proceso_actual and len(cola_terminado) == len(todos_procesos):
                PrioridadNE.mostrar_tabla(todos_procesos, 'Finalizó', cola_listos, cola_terminado, proceso_actual, tiempo_actual)
                break

        return resultados_en_tiempo_real  # Retornar los resultados en tiempo real


