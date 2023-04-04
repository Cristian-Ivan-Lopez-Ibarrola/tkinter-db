import tkinter as tk
from tkinter import ttk
from conexion import reset, prome, maxProm, genios
from carga_de_datos import crear


class Ventana(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.centrar_ventana()
        self.pack()

        self.label1 = ttk.Label(self, text="El promedio de cada curso")
        self.label1.pack(pady=10)
        self.boton1 = ttk.Button(
            self, text="solucion", command=self.abrir_promedio)
        self.boton1.pack(side="top", pady=10)

        self.label2 = ttk.Label(self, text="El curso que mayor promedio tiene")
        self.label2.pack(pady=10)
        self.boton1 = ttk.Button(
            self, text="solucion", command=self.abrir_mayor_promedio)
        self.boton1.pack(side="top", pady=10)

        self.label3 = ttk.Label(
            self, text="El nombre del alumno que mayor nota obtuvo y a qué curso pertenece.")
        self.label3.pack(pady=10)
        self.boton1 = ttk.Button(
            self, text="solucion", command=self.abrir_genios)
        self.boton1.pack(side="top", pady=10)

        self.boton1 = ttk.Button(
            self, text="crear base de datos", command=crear)
        self.boton1.pack(side="left", padx=10)

        self.boton2 = ttk.Button(
            self, text="borrar la base de datos", command=reset)
        self.boton2.pack(side="right", padx=10)

    def centrar_ventana(self):

        w = self.master.winfo_screenwidth()
        h = self.master.winfo_screenheight()

        w_ventana = 400
        h_ventana = 300

        x = (w - w_ventana) // 2
        y = (h - h_ventana) // 2

        self.master.geometry('{}x{}+{}+{}'.format(w_ventana, h_ventana, x, y))

    def abrir_promedio(self):
        ventana = tk.Toplevel(self)
        w = self.master.winfo_screenwidth()
        h = self.master.winfo_screenheight()
        w_ventana = 200
        h_ventana = 350
        x = (w - w_ventana) // 2
        y = (h - h_ventana) // 2
        ventana.geometry(f"{w_ventana}x{h_ventana}+{x}+{y}")

        ventana.title("promedio de cada curso")
        ventana.grab_set()

        for i in range(11):
            ventana.rowconfigure(i, weight=1)
        ventana.columnconfigure(0, weight=1)
        ventana.columnconfigure(1, weight=1)

        labels = []
        label = ttk.Label(ventana, text=f"nombre curso")
        labels.append(label)
        label = ttk.Label(ventana, text=f"promedio")
        labels.append(label)

        lista = []
        prome(lista)

        for i in range(10):
            for j in range(2):
                label = ttk.Label(ventana, text=(lista[i][j]))
                labels.append(label)

        for i in range(11):
            for j in range(2):
                label = labels[i*2+j]
                label.grid(column=j, row=i, sticky="nsew", padx=5, pady=5)

        boton_cerrar = ttk.Button(
            ventana, text="Cerrar", command=ventana.destroy)
        boton_cerrar.grid(row=11, column=0, columnspan=2)

    def abrir_mayor_promedio(self):
        ventana = tk.Toplevel(self)
        w = self.master.winfo_screenwidth()
        h = self.master.winfo_screenheight()
        w_ventana = 200
        h_ventana = 100
        x = (w - w_ventana) // 2
        y = (h - h_ventana) // 2
        ventana.geometry(f"{w_ventana}x{h_ventana}+{x}+{y}")

        ventana.title("promedio de cada curso")
        ventana.grab_set()

        for i in range(4):
            ventana.rowconfigure(i, weight=1)
        ventana.columnconfigure(0, weight=1)
        ventana.columnconfigure(1, weight=1)

        labels = []
        label = ttk.Label(ventana, text=f"nombre curso")
        labels.append(label)
        label = ttk.Label(ventana, text=f"promedio")
        labels.append(label)

        lista = []
        maxProm(lista)

        for j in range(2):
            label = ttk.Label(ventana, text=(lista[0][j]))
            labels.append(label)

        for i in range(2):
            for j in range(2):
                label = labels[i*2+j]
                label.grid(column=j, row=i, sticky="nsew", padx=5, pady=5)

        boton_cerrar = ttk.Button(
            ventana, text="Cerrar", command=ventana.destroy)
        boton_cerrar.grid(row=11, column=0, columnspan=2)

    def abrir_genios(self):
        ventana = tk.Toplevel(self)
        w = self.master.winfo_screenwidth()
        h = self.master.winfo_screenheight()
        w_ventana = 400
        h_ventana = 300
        x = (w - w_ventana) // 2
        y = (h - h_ventana) // 2
        ventana.geometry(f"{w_ventana}x{h_ventana}+{x}+{y}")

        ventana.title("promedio de cada curso")
        ventana.grab_set()

        for i in range(11):
            ventana.rowconfigure(i, weight=1)
        ventana.columnconfigure(0, weight=1)
        ventana.columnconfigure(1, weight=1)
        ventana.columnconfigure(2, weight=1)
        ventana.columnconfigure(3, weight=1)

        labels = []
        label = ttk.Label(ventana, text=f"nombre")
        labels.append(label)
        label = ttk.Label(ventana, text=f"apellido")
        labels.append(label)
        label = ttk.Label(ventana, text=f"calificacion")
        labels.append(label)
        label = ttk.Label(ventana, text=f"curso")
        labels.append(label)

        lista = []
        genios(lista)

        for i in range(10):
            for j in range(4):
                label = ttk.Label(ventana, text=(lista[i][j]))
                labels.append(label)

        for i in range(11):
            for j in range(4):
                label = labels[i*4+j]
                label.grid(column=j, row=i, sticky="nsew", padx=5, pady=5)

        boton_cerrar = ttk.Button(
            ventana, text="Cerrar", command=ventana.destroy)
        boton_cerrar.grid(row=11, column=0, columnspan=4)


root = tk.Tk()
style = ttk.Style()
style.configure("Red.TSeparator", foreground="red")
app = Ventana(master=root)
app.mainloop()
