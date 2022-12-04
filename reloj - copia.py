import tkinter as tk
from tkinter.ttk import *
from time import strftime

class aplicacion:
    def __init__(self):
        self.app=tk.Tk()
        self.app.title("Reloj digital")  
        self.frameReloj()
        self.actualiza_reloj()
        self.app.mainloop()
         

    def frameReloj(self):    
        self.frame_hora=tk.Frame()
        self.frame_hora.pack() 
        self.etiqueta_hm=Label(self.frame_hora, font=("digitalk", 50), text="H:M", background="dark orange")
        self.etiqueta_hm.grid(row=0, column=0)
        self.etiqueta_s=Label(self.frame_hora, font=("digitalk", 30), text="s", background="dark orange")
        self.etiqueta_s.grid(row=0, column=1, sticky="n")  
        self.etiqueta_fecha=Label(font=("digitalk", 30), text="día d/m/aaaa", background="dark orange")
        self.etiqueta_fecha.pack(anchor="center")

 
    def actualiza_reloj(self):
        self.etiqueta_hm.config(text=strftime ("%H:%M"))
        self.etiqueta_s.config(text=strftime ("%S"))
        self.etiqueta_fecha.config(text=strftime ("data: %A, %d/%m/%y"))
        self.etiqueta_s.after(1000, self.actualiza_reloj)
        

        
aplicacion1=aplicacion()
