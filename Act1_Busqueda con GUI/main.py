import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
import statistics
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def busqueda_lineal(lista, x):
    for i, valor in enumerate(lista):
        if valor == x:
            return i
    return -1

def busqueda_binaria(lista, x):
    inicio, fin = 0, len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == x:
            return medio
        elif lista[medio] < x:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Comparación de Búsquedas")

        self.lista = []
        self.tamanios = [100, 1000, 10000, 100000]
        self.resultados = {"lineal": {}, "binaria": {}}

        ttk.Label(root, text="Tamaño de lista:").grid(row=0, column=0, padx=5, pady=5)
        self.combo_tam = ttk.Combobox(root, values=self.tamanios)
        self.combo_tam.grid(row=0, column=1, padx=5, pady=5)

        self.btn_generar = ttk.Button(root, text="Generar datos", command=self.generar_datos)
        self.btn_generar.grid(row=0, column=2, padx=5, pady=5)

        ttk.Label(root, text="Valor a buscar:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_valor = ttk.Entry(root)
        self.entry_valor.grid(row=1, column=1, padx=5, pady=5)

        self.btn_lineal = ttk.Button(root, text="Búsqueda lineal", command=lambda: self.buscar("lineal"))
        self.btn_lineal.grid(row=2, column=0, padx=5, pady=5)

        self.btn_binaria = ttk.Button(root, text="Búsqueda binaria", command=lambda: self.buscar("binaria"))
        self.btn_binaria.grid(row=2, column=1, padx=5, pady=5)

        self.btn_comparar = ttk.Button(root, text="Comparar algoritmos", command=self.comparar)
        self.btn_comparar.grid(row=2, column=2, padx=5, pady=5)

        self.label_resultado = ttk.Label(root, text="Resultados aquí")
        self.label_resultado.grid(row=3, column=0, columnspan=3, pady=10)

        self.fig, self.ax = plt.subplots(figsize=(5, 3))
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().grid(row=4, column=0, columnspan=3)

    def generar_datos(self):
        try:
            tam = int(self.combo_tam.get())
            self.lista = sorted(random.sample(range(tam * 10), tam))
            messagebox.showinfo("Éxito", f"Lista de {tam} elementos generada.")
        except ValueError:
            messagebox.showerror("Error", "Seleccione un tamaño válido.")

    def buscar(self, metodo):
        if not self.lista:
            messagebox.showerror("Error", "Primero genere la lista.")
            return
        try:
            valor = int(self.entry_valor.get())
        except ValueError:
            messagebox.showerror("Error", "Ingrese un valor numérico.")
            return

        inicio = time.perf_counter()
        if metodo == "lineal":
            idx = busqueda_lineal(self.lista, valor)
        else:
            idx = busqueda_binaria(self.lista, valor)
        fin = time.perf_counter()

        tiempo = (fin - inicio) * 1000
        if idx != -1:
            self.label_resultado.config(
                text=f"Tamaño: {len(self.lista)} | {metodo} encontró {valor} en índice {idx} | Tiempo: {tiempo:.6f} ms"
            )
        else:
            self.label_resultado.config(
                text=f"Tamaño: {len(self.lista)} | {metodo} no encontró {valor} | Tiempo: {tiempo:.6f} ms"
            )

    def comparar(self):
        repeticiones = 5

        tam = int(self.combo_tam.get())
        if tam not in self.tamanios:
            messagebox.showerror("Error", "Seleccione un tamaño válido de la lista.")
            return

        if tam not in self.resultados["lineal"]:
            lista = sorted(random.sample(range(tam * 10), tam))

            t_l = []
            for _ in range(repeticiones):
                valor = random.choice(lista)
                inicio = time.perf_counter()
                busqueda_lineal(lista, valor)
                fin = time.perf_counter()
                t_l.append((fin - inicio) * 1000)
            self.resultados["lineal"][tam] = statistics.mean(t_l)

            t_b = []
            for _ in range(repeticiones):
                valor = random.choice(lista)
                inicio = time.perf_counter()
                busqueda_binaria(lista, valor)
                fin = time.perf_counter()
                t_b.append((fin - inicio) * 1000)
            self.resultados["binaria"][tam] = statistics.mean(t_b)

        print("Lineal acumulado:", self.resultados["lineal"])
        print("Binaria acumulado:", self.resultados["binaria"])

        self.ax.clear()
        tamanios_lineal = sorted(self.resultados["lineal"].keys())
        self.ax.plot(tamanios_lineal, [self.resultados["lineal"][t] for t in tamanios_lineal],
                     label="Lineal", marker="o")

        tamanios_binaria = sorted(self.resultados["binaria"].keys())
        self.ax.plot(tamanios_binaria, [self.resultados["binaria"][t] for t in tamanios_binaria],
                     label="Binaria", marker="o")

        self.ax.set_title("Comparación de tiempos")
        self.ax.set_xlabel("Tamaño de la lista")
        self.ax.set_ylabel("Tiempo promedio (ms)")
        self.ax.legend()
        self.ax.grid(True)
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
