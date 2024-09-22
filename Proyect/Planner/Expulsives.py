import time
import os
import random
#from Processes.Process import Process


class RR:  # Round Robin
    def __init__(self):
        pass

    # Función para limpiar la consola
    @staticmethod
    def limpiar_consola():
        os.system('clear')

    # Función para mostrar la tabla en tiempo real
    @staticmethod
    def mostrar_tabla(procesos, tiempo_actual, cola_procesos):
        RR.limpiar_consola()  # Limpiar la consola antes de mostrar la tabla actualizada
        print(f"Tiempo actual: {tiempo_actual}")
        print(f"{'Proceso':<10}{'Llegada':<10}{'Ejecución':<10}{'Comienzo':<10}{'Restante':<10}{'Final':<10}{'Espera':<10}{'Retorno':<10}")
        for proceso in procesos:
            comienzo = proceso.tiempo_comienzo if proceso.tiempo_comienzo != -1 else ""
            final = proceso.tiempo_finalizacion if proceso.tiempo_finalizacion != 0 else ""
            print(f"{proceso.nombre:<10}{proceso.tiempo_llegada:<10}{proceso.tiempo_ejecucion:<10}{comienzo:<10}{proceso.tiempo_restante:<10}{final:<10}{proceso.tiempo_espera:<10}{proceso.tiempo_retorno:<10}")

        # Mostrar los procesos en cola
        print("\nProcesos en cola: ", [proceso.nombre for proceso in cola_procesos])

    # Función para ejecutar Round Robin en tiempo real
    @staticmethod
    def round_robin_real_time(procesos, quantum):
        tiempo_actual = 0
        cola_procesos = []
        finalizados = []
        todos_procesos = procesos[:]  # Copia para mostrar todos los procesos desde el principio
        resultados_en_tiempo_real = []  # Lista para almacenar los resultados en tiempo real

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
                    RR.mostrar_tabla(todos_procesos, tiempo_actual, cola_procesos)
                    time.sleep(1)  # Simulación de 1 segundo por unidad de tiempo
                    tiempo_actual += 1
                    proceso_actual.tiempo_restante -= 1

                    # Guardar el estado actual del proceso
                    estado_actual = {
                        "nombre": proceso_actual.nombre,
                        "tiempo_llegada": proceso_actual.tiempo_llegada,
                        "tiempo_ejecucion": proceso_actual.tiempo_ejecucion,
                        "tiempo_comienzo": proceso_actual.tiempo_comienzo,
                        "tiempo_restante": proceso_actual.tiempo_restante,
                        "tiempo_finalizacion": proceso_actual.tiempo_finalizacion,
                        "tiempo_espera": proceso_actual.tiempo_espera,
                        "tiempo_retorno": proceso_actual.tiempo_retorno,
                        "prioridad" : 0
                    }
                    resultados_en_tiempo_real.append(estado_actual)

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
                    estado_actual = {
                        "nombre": proceso_actual.nombre,
                        "tiempo_llegada": proceso_actual.tiempo_llegada,
                        "tiempo_ejecucion": proceso_actual.tiempo_ejecucion,
                        "tiempo_comienzo": proceso_actual.tiempo_comienzo,
                        "tiempo_restante": proceso_actual.tiempo_restante,
                        "tiempo_finalizacion": proceso_actual.tiempo_finalizacion,
                        "tiempo_espera": proceso_actual.tiempo_espera,
                        "tiempo_retorno": proceso_actual.tiempo_retorno,
                        "prioridad" : 0
                    }
                    resultados_en_tiempo_real.append(estado_actual)
                else:
                    # Si no ha terminado, se vuelve a añadir al final de la cola
                    cola_procesos.append(proceso_actual)
            else:
                # Si no hay procesos en la cola, avanzar el tiempo al siguiente proceso que llegue
                RR.mostrar_tabla(todos_procesos, tiempo_actual, cola_procesos)
                time.sleep(1)
                tiempo_actual += 1

        return resultados_en_tiempo_real  # Retornar los resultados en tiempo real


class SRTF:  # Shortest Remaining Time First
    def __init__(self):
        pass

    # Función para limpiar la consola
    @staticmethod
    def limpiar_consola():
        os.system('clear')

    # Función para mostrar la tabla en tiempo real
    @staticmethod
    def mostrar_tabla(procesos, tiempo_actual, cola_procesos):
        SRTF.limpiar_consola()  # Limpiar la consola antes de mostrar la tabla actualizada
        print(f"Tiempo actual: {tiempo_actual}")
        print(f"{'Proceso':<10}{'Llegada':<10}{'Ejecución':<10}{'Comienzo':<10}{'Restante':<10}{'Final':<10}{'Espera':<10}{'Retorno':<10}")
        for proceso in procesos:
            comienzo = proceso.tiempo_comienzo if proceso.tiempo_comienzo != -1 else ""
            final = proceso.tiempo_finalizacion if proceso.tiempo_finalizacion != 0 else ""
            print(f"{proceso.nombre:<10}{proceso.tiempo_llegada:<10}{proceso.tiempo_ejecucion:<10}{comienzo:<10}{proceso.tiempo_restante:<10}{final:<10}{proceso.tiempo_espera:<10}{proceso.tiempo_retorno:<10}")

        # Mostrar los procesos en cola
        print("\nProcesos en cola: ", [proceso.nombre for proceso in cola_procesos])

    # Función para ejecutar SRTF en tiempo real
    @staticmethod
    def srtf_real_time(procesos):
        tiempo_actual = 0
        cola_procesos = []
        finalizados = []
        todos_procesos = procesos[:]  # Copia para mostrar todos los procesos desde el principio
        resultados_en_tiempo_real = []  # Lista para almacenar los resultados en tiempo real

        while procesos or cola_procesos:
            # Añadir procesos que han llegado al sistema al tiempo actual
            for proceso in procesos[:]:
                if proceso.tiempo_llegada <= tiempo_actual:
                    cola_procesos.append(proceso)
                    procesos.remove(proceso)

            if cola_procesos:
                # Elegir el proceso con el menor tiempo restante
                proceso_actual = min(cola_procesos, key=lambda p: p.tiempo_restante)

                # Si el proceso nunca ha comenzado, se marca el tiempo de inicio
                if proceso_actual.tiempo_comienzo == -1:
                    proceso_actual.tiempo_comienzo = tiempo_actual

                # Ejecutar el proceso por 1 unidad de tiempo
                SRTF.mostrar_tabla(todos_procesos, tiempo_actual, cola_procesos)
                time.sleep(1)  # Simulación de 1 segundo por unidad de tiempo
                tiempo_actual += 1
                proceso_actual.tiempo_restante -= 1

                # Guardar el estado actual del proceso
                estado_actual = {
                    "nombre": proceso_actual.nombre,
                    "tiempo_llegada": proceso_actual.tiempo_llegada,
                    "tiempo_ejecucion": proceso_actual.tiempo_ejecucion,
                    "tiempo_comienzo": proceso_actual.tiempo_comienzo,
                    "tiempo_restante": proceso_actual.tiempo_restante,
                    "tiempo_finalizacion": proceso_actual.tiempo_finalizacion,
                    "tiempo_espera": proceso_actual.tiempo_espera,
                    "tiempo_retorno": proceso_actual.tiempo_retorno,
                    "prioridad" : 0
                }
                resultados_en_tiempo_real.append(estado_actual)

                # Si el proceso ha terminado
                if proceso_actual.tiempo_restante == 0:
                    proceso_actual.tiempo_finalizacion = tiempo_actual
                    proceso_actual.tiempo_retorno = proceso_actual.tiempo_finalizacion - proceso_actual.tiempo_llegada
                    proceso_actual.tiempo_espera = proceso_actual.tiempo_retorno - proceso_actual.tiempo_ejecucion
                    finalizados.append(proceso_actual)
                    cola_procesos.remove(proceso_actual)
                    estado_actual = {
                        "nombre": proceso_actual.nombre,
                        "tiempo_llegada": proceso_actual.tiempo_llegada,
                        "tiempo_ejecucion": proceso_actual.tiempo_ejecucion,
                        "tiempo_comienzo": proceso_actual.tiempo_comienzo,
                        "tiempo_restante": proceso_actual.tiempo_restante,
                        "tiempo_finalizacion": proceso_actual.tiempo_finalizacion,
                        "tiempo_espera": proceso_actual.tiempo_espera,
                        "tiempo_retorno": proceso_actual.tiempo_retorno,
                        "prioridad" : 0
                    }
                    resultados_en_tiempo_real.append(estado_actual)
            else:
                # Si no hay procesos disponibles, avanzar el tiempo hasta que uno llegue
                SRTF.mostrar_tabla(todos_procesos, tiempo_actual, cola_procesos)
                time.sleep(1)
                tiempo_actual += 1

        return resultados_en_tiempo_real  # Retornar los resultados en tiempo real
    
    
class PrioridadExp:

    @staticmethod
    def limpiar_consola() -> None:
        os.system('clear')

    @staticmethod
    def mostrar_tabla(procesos, tiempo_actual, cola_listos, cola_terminado, proceso_actual, tiempo_cpu=None) -> None:
        PrioridadExp.limpiar_consola()
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
    def prioridad_expulsiva_real_time(procesos) -> list:
        tiempo_actual = 0
        todos_procesos = PrioridadExp.generar_prioridad(procesos)
        cola_listos = []
        cola_terminado = []
        proceso_actual = None
        resultados_en_tiempo_real = []

        while True:
            # Agregar procesos a la cola de listos
            for proceso in todos_procesos:
                if proceso.tiempo_llegada == tiempo_actual:
                    cola_listos.append(proceso)

            # Manejo de procesos en cola
            if cola_listos:
                cola_listos.sort(key=lambda proceso: proceso.prioridad)

                # Si no hay proceso actual, toma el de mayor prioridad
                if not proceso_actual:
                    proceso_actual = cola_listos.pop(0)
                    proceso_actual.tiempo_comienzo = tiempo_actual

                # Comprobar si hay un nuevo proceso con mayor prioridad
                elif cola_listos and cola_listos[0].prioridad < proceso_actual.prioridad:
                    # Expulsar el proceso actual
                    cola_listos.insert(0, proceso_actual)  # Regresar el proceso actual a la cola
                    proceso_actual = cola_listos.pop(0)    # Tomar el nuevo proceso de mayor prioridad
                    proceso_actual.tiempo_comienzo = tiempo_actual

            # Mostrar la tabla de estado
            PrioridadExp.mostrar_tabla(todos_procesos, tiempo_actual, cola_listos, cola_terminado, proceso_actual)

            if proceso_actual:
                # Ejecutar el proceso actual
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
                    }
                    resultados_en_tiempo_real.append(estado_actual)
                    cola_terminado.append(proceso_actual)
                    proceso_actual = None
            else:
                # Si no hay procesos en ejecución ni en la cola, avanzar el tiempo
                print("No hay procesos en ejecución ni en cola. Avanzando tiempo...")
                time.sleep(1)  # Opcional: para ver la pausa
                tiempo_actual += 1
                continue  # Volver al inicio del bucle

            # Incrementar el tiempo
            tiempo_actual += 1
            time.sleep(1)

            # Comprobar si todos los procesos han terminado
            if not proceso_actual and len(cola_terminado) == len(todos_procesos):
                PrioridadExp.mostrar_tabla(todos_procesos, 'Finalizó', cola_listos, cola_terminado, proceso_actual, tiempo_actual)
                break

        return resultados_en_tiempo_real  # Retornar los resultados en tiempo real
