class Process:
    def __init__(self, nombre, tiempo_llegada, tiempo_ejecucion):
        self.nombre = nombre
        self.tiempo_llegada = tiempo_llegada
        self.tiempo_ejecucion = tiempo_ejecucion
        self.tiempo_comienzo = 0
        self.tiempo_finalizacion = 0
        self.tiempo_espera = 0
        self.tiempo_retorno = 0
        self.tiempo_restante = tiempo_ejecucion  # Para seguir el progreso