# main.py
import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
import Algoritmo_huffman

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class HuffmanApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Compresor Huffman")
        self.geometry("700x600")

        self.texto_original = ""
        self.codificado = ""
        self.raiz = None
        self.codigos = {}

        # --- UI ---
        self.boton_cargar = ctk.CTkButton(self, text="Cargar archivo", command=self.cargar_archivo)
        self.boton_cargar.pack(pady=10)

        self.boton_codificar = ctk.CTkButton(self, text="Codificar", command=self.codificar)
        self.boton_codificar.pack(pady=10)

        self.boton_decodificar = ctk.CTkButton(self, text="Decodificar", command=self.decodificar)
        self.boton_decodificar.pack(pady=10)

        self.resultado = ctk.CTkTextbox(self, width=600, height=300)
        self.resultado.pack(pady=15)

        self.etiqueta_info = ctk.CTkLabel(self, text="")
        self.etiqueta_info.pack(pady=5)

    def cargar_archivo(self):
        ruta = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
        if not ruta:
            return
        with open(ruta, "r", encoding="utf-8") as f:
            self.texto_original = f.read()
        self.resultado.delete("1.0", "end")
        self.resultado.insert("end", f"Archivo cargado: {os.path.basename(ruta)}\n\n{self.texto_original}")
        self.etiqueta_info.configure(text=f"Tamaño original: {len(self.texto_original)} caracteres")

    def codificar(self):
        if not self.texto_original:
            messagebox.showwarning("Aviso", "Primero carga un archivo.")
            return

        frec = Algoritmo_huffman.calcular_frecuencias(self.texto_original)
        self.raiz = Algoritmo_huffman.construir_arbol(frec)
        self.codigos = Algoritmo_huffman.generar_codigos(self.raiz)

        self.codificado = Algoritmo_huffman.codificar_texto(self.texto_original, self.codigos)
        eficiencia = Algoritmo_huffman.calcular_eficiencia(self.texto_original, self.codificado)

        self.resultado.delete("1.0", "end")
        self.resultado.insert("end", "=== Códigos Huffman ===\n")
        for c, code in self.codigos.items():
            self.resultado.insert("end", f"'{c}': {code}\n")

        self.resultado.insert("end", f"\n=== Texto codificado ===\n{self.codificado}")
        self.etiqueta_info.configure(text=f"Eficiencia: {eficiencia:.2f}% de compresión")

    def decodificar(self):
        if not self.codificado or not self.raiz:
            messagebox.showwarning("Aviso", "Primero codifica un archivo.")
            return

        texto_decodificado = Algoritmo_huffman.decodificar_texto(self.codificado, self.raiz)
        self.resultado.delete("1.0", "end")
        self.resultado.insert("end", "=== Texto decodificado ===\n")
        self.resultado.insert("end", texto_decodificado)
        self.etiqueta_info.configure(text="Texto decodificado correctamente.")

if __name__ == "__main__":
    app = HuffmanApp()
    app.mainloop()
