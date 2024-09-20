from tkinter import *
from Planner.Processes.Process import Process
processes = []
def generate_process(event = None):
    processes.append(Process(name.get(),
                             arrival_time.get(),
                             cpu_time.get()))
    
def show_process(event = None):
    for var in processes:
        print(var.nombre, var.tiempo_llegada,var.tiempo_ejecucion)
        
    
    
    

root = Tk()
root.grid()
root.geometry("850x480")

first_box = Frame(root,background="red")
first_box.grid(row=1,column=0,padx=10,pady=5)

define_process = Label(first_box,text="Process generator",background="red",padx=15,pady=2,font=("times",12)).grid(row=0,column=0)
#labels to define process information
process_name = Label(first_box, text="process name",background="red").grid(row=1,column=0,pady=3)
name = StringVar()
process_name_entry = Entry(first_box,
                           width=15,
                           textvariable=name).grid(row=2
                                                ,column=0
                                                ,padx=5)

come_time = Label(first_box,
                  text="arrival time",
                  background="red").grid(row=3,
                                         column=0,
                                         pady=3)
arrival_time = IntVar()
come_time_entry = Entry(first_box,
                        width=15,
                        textvariable=arrival_time).grid(row=4,
                                                        column=0,
                                                        padx=5)

execution_time = Label(first_box,
                       text="execution time",
                       background="red").grid(row=5,
                                              column=0,
                                              pady=3)
cpu_time=IntVar()
execution_time_entry = Entry(first_box,
                             width=15,
                             textvariable=cpu_time).grid(row=6,
                                                         column=0,
                                                         padx=6)



#button to generate process
generate_button = Button(first_box, 
                         text="Generate", 
                         fg="red",
                         width=7,
                         command=generate_process).grid(row=7,
                                                        column=0,
                                                        pady=(5),
                                                        padx=(40,0))

generate_button = Button(first_box,
                         text="Show",
                         fg="red",
                         width=7,
                         command=show_process).grid(row=8,
                                                column=0,
                                                pady=(5),
                                                padx=(40,0))

root.mainloop()

