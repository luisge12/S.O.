import sys
import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Planner.Processes.Process import Process
from Planner.Non_expulsives import FCFS, SJF, SA, PrioridadNE
from Planner.Expulsives import SRTF, PrioridadExp, RR

results = []  # Lista de resultados
processes = []  # Lista de procesos


    

def update_table(data):
    # Limpiar la tabla antes de insertar nuevos datos
    for row in tree.get_children():
        tree.delete(row)
    
    # Insertar los nuevos resultados
    for resul in data:
        tree.insert("", "end", values=(
            resul["nombre"],
            resul["tiempo_llegada"],
            resul["tiempo_ejecucion"],
            resul["tiempo_comienzo"],
            resul["tiempo_restante"],
            resul["tiempo_finalizacion"],
            resul["tiempo_espera"],
            resul["tiempo_retorno"],
            resul["prioridad"]
        ))
        
def clear_results(event=None):
    global results
    results = []  # Limpiar resultados
    update_table(results)  # Actualizar la tabla para que esté vacía
    
    
# Modifica las funciones de selección de algoritmo para actualizar la tabla
def select_fcfs(event=None):
    clear_results()  # Limpiar resultados antes de ejecutar
    global results
    results = FCFS.fcfs_real_time(processes) 
    update_table(results) 

def select_sjf(event=None):
    clear_results()  # Limpiar resultados antes de ejecutar
    global results
    results = SJF.sjf_real_time(processes)
    update_table(results)

def select_rs(event=None):
    clear_results()  # Limpiar resultados antes de ejecutar
    global results
    results = SA.seleccion_aleatoria_real_time(processes)
    update_table(results)

def select_prio_ne(event=None):
    clear_results()  # Limpiar resultados antes de ejecutar
    global results
    results = PrioridadNE.prioridad_no_expulsiva_real_time(processes)
    update_table(results)

def select_rr(event=None):
    clear_results()  # Limpiar resultados antes de ejecutar
    global results
    results = RR.round_robin_real_time(processes, 3)
    update_table(results)

def select_srtf(event=None):
    clear_results()  # Limpiar resultados antes de ejecutar
    global results
    results = SRTF.srtf_real_time(processes)
    update_table(results)

def select_prio_e(event=None):
    clear_results()  # Limpiar resultados antes de ejecutar
    global results
    results = PrioridadExp.prioridad_expulsiva_real_time(processes)
    update_table(results)


def validate_data():  # Función que verifica los datos de entrada
    if name.get().strip() == "":
        messagebox.showerror("Error", "El nombre del proceso no puede estar vacío.")
        return False
    
    try:
        arrival = int(arrival_time.get())
        if arrival < 0:
            messagebox.showerror("Error", "El tiempo de llegada debe ser un número positivo.")
            return False
    except ValueError:
        messagebox.showerror("Error", "El tiempo de llegada debe ser un número entero.")
        return False

    try:
        execution = int(cpu_time.get())
        if execution <= 0:
            messagebox.showerror("Error", "El tiempo de ejecución debe ser un número mayor que 0.")
            return False
    except ValueError:
        messagebox.showerror("Error", "El tiempo de ejecución debe ser un número entero.")
        return False
    
    return True

def generate_process(event=None):  # Función para generar los procesos a ejecutar
    if not validate_data():
        return

    # Verificar si el proceso ya existe en la lista antes de agregarlo
    for p in processes:
        if p.nombre == name.get():
            messagebox.showerror("Error", "El proceso con este nombre ya existe.")
            return
    
    processes.append(Process(name.get(), arrival_time.get(), cpu_time.get()))
    messagebox.showinfo("Proceso generado", "El proceso ha sido generado con éxito")

def show_process(event=None):
    for var in processes:
        print(var.nombre, var.tiempo_llegada, var.tiempo_ejecucion)

root = Tk()
root.grid()
root.geometry("1040x680")
root.config(background="black")

# Primer cuadro para generar procesos
first_box = Frame(root, background="blue", width=200, height=300)
first_box.grid(row=1, column=0, padx=50, pady=5)
first_box.grid_propagate(False)

define_process = Label(first_box, text="Process generator", background="blue", padx=20, pady=5, font=("times", 12))
define_process.grid(row=0, column=0)

process_name = Label(first_box, text="Process name", background="blue")
process_name.grid(row=1, column=0)

name = StringVar()
process_name_entry = Entry(first_box, width=15, textvariable=name)
process_name_entry.grid(row=2, column=0, padx=5)

come_time = Label(first_box, text="Arrival time", background="blue")
come_time.grid(row=3, column=0)

arrival_time = IntVar()
come_time_entry = Entry(first_box, width=15, textvariable=arrival_time)
come_time_entry.grid(row=4, column=0, padx=5)

execution_time = Label(first_box, text="Execution time", background="blue")
execution_time.grid(row=5, column=0)

cpu_time = IntVar()
execution_time_entry = Entry(first_box, width=15, textvariable=cpu_time)
execution_time_entry.grid(row=6, column=0, padx=6)

generate_button = Button(first_box, text="Generate", fg="black", width=7, command=generate_process)
generate_button.grid(row=7, column=0, pady=(5), padx=(40, 0), sticky="e")

send_button = Button(first_box, text="Send", fg="black", width=10, command=show_process)
send_button.grid(row=8, column=0, pady=(10), sticky="s")

# Segundo cuadro para seleccionar los algoritmos
second_box = Frame(root, background="blue", width=700, height=300)
second_box.grid(row=1, column=1, padx=5, pady=5)
second_box.grid_propagate(False)

algoritm = Label(second_box, text="Select an algorithm", background="blue", padx=20, pady=5, font=("times", 12))
algoritm.grid(row=0, column=0, sticky="s")

select_algorithm = Label(second_box, text="No expulsives", background="blue", padx=0, pady=5)
select_algorithm.grid(row=1, column=0, sticky="s")

# Botones para algoritmos no expulsivos
FCFS_button = Button(second_box, text="FCFS", fg="black", width=12, command=select_fcfs)
FCFS_button.grid(row=2, column=0, pady=(10), padx=(0, 20))

SJF_button = Button(second_box, text="SJF", fg="black", width=12, command=select_sjf)
SJF_button.grid(row=2, column=1, pady=(10), padx=(0, 20))

RS_button = Button(second_box, text="Random Selection", fg="black", width=12, command=select_rs)
RS_button.grid(row=2, column=2, pady=(10), padx=(0, 20))

priorities_button = Button(second_box, text="Base on priorities", fg="black", width=12, command=select_prio_ne)
priorities_button.grid(row=2, column=3, pady=(10), padx=(0, 20))

# Etiqueta para algoritmos expulsivos
expulsives = Label(second_box, text="Expulsives algorithms", background="blue", padx=0, pady=5)
expulsives.grid(row=3, column=0, sticky="s")

# Botones para algoritmos expulsivos
RR_button = Button(second_box, text="Round Robin", fg="black", width=12, command=select_rr)
RR_button.grid(row=4, column=0, pady=(10))

SRTF_button = Button(second_box, text="SRTF", fg="black", width=12, command=select_srtf)
SRTF_button.grid(row=4, column=1, pady=(10))

PE_button = Button(second_box, text="Base on priorities", fg="black", width=12, command=select_prio_e)
PE_button.grid(row=4, column=2, pady=(10), padx=(50, 20))

# Tercer cuadro para mostrar la tabla
table_box = Frame(root, background="blue", width=1030, height=350)
table_box.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
table_box.grid_propagate(False)

columns = ("Nombre", "Llegada", "Ejecución", "Comienzo","Restante", "Final", "Espera", "Retorno","Prioridad")
tree = ttk.Treeview(table_box, columns=columns, show="headings")

tree.heading("Nombre", text="Nombre")
tree.column("Nombre", width=100)

tree.heading("Llegada", text="Llegada")
tree.column("Llegada", width=100)

tree.heading("Ejecución", text="Ejecución")
tree.column("Ejecución", width=100)

tree.heading("Comienzo", text="Comienzo")
tree.column("Comienzo", width=100)

tree.heading("Restante", text="Restante")
tree.column("Restante", width=100)

tree.heading("Final", text="Final")
tree.column("Final", width=100)

tree.heading("Espera", text="Espera")
tree.column("Espera", width=100)

tree.heading("Retorno", text="Retorno")
tree.column("Retorno", width=100)

tree.heading("Prioridad", text="Prioridad")
tree.column("Prioridad", width=100)

scrollbar = Scrollbar(table_box, orient="vertical", command=tree.yview)
scrollbar.pack(side="right", fill="y")

tree.configure(yscrollcommand=scrollbar.set)

tree.pack(side="left", fill="both", expand=True)

root.mainloop()
