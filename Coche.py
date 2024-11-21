import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Clase Coche
class Coche:
    def __init__(self, gasolina):
        self.gasolina = gasolina
        print("Tenemos", gasolina, "litros")

    def arrancar(self):
        if self.gasolina > 0:
            return "Arranca"
        else:
            return "No arranca"

    def conducir(self):
        if self.gasolina > 0:
            self.gasolina -= 1
            return f"Conduciendo... Quedan {self.gasolina} litros"
        else:
            return "No se mueve, no hay gasolina"

    def GirarIzquierda(self):
        return "Girando a la Izquierda"

    def GirarDerecha(self):
        return "Girando a la derecha"

# Funciones para interactuar con la interfaz
def arrancar_coche():
    estado = coche.arrancar()
    messagebox.showinfo("Estado del coche", estado)
    actualizar_estado()

def conducir_coche():
    estado = coche.conducir()
    messagebox.showinfo("Estado del coche", estado)
    actualizar_estado()

def actualizar_estado():
    # Actualizar el estado de la gasolina en la interfaz
    etiqueta_gasolina.config(text=f"Gasolina: {coche.gasolina} litros")

def GirarIzq():
    estado = coche.GirarIzquierda()
    messagebox.showinfo("El coche esta", estado)

def GirarDer():
    estado = coche.GirarDerecha()
    messagebox.showinfo("El coche esta", estado)

# Crear una instancia del coche con 5 litros de gasolina
coche = Coche(5)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Coche Interactivo")

# Etiqueta para mostrar la cantidad de gasolina
etiqueta_gasolina = tk.Label(ventana, text=f"Gasolina: {coche.gasolina} litros", font=("Arial", 14))
etiqueta_gasolina.pack(pady=10)

# Botón para arrancar el coche
boton_arrancar = tk.Button(ventana, text="Arrancar", command=arrancar_coche, font=("Arial", 12), bg="green", fg="white")
boton_arrancar.pack(pady=5)

# Botón para conducir el coche
boton_conducir = tk.Button(ventana, text="Conducir", command=conducir_coche, font=("Arial", 12), bg="blue", fg="white")
boton_conducir.pack(pady=5)

#Boton para girar a la izquierda
boton_izquierda = tk.Button(ventana, text="Izquierda",command=GirarIzq, font=("Arial", 12), bg="blue", fg="white")
boton_izquierda.pack(pady=5)

#Boton para girar el coche a la derecha
boton_derecha = tk.Button(ventana, text="Derecha",command=GirarDer, font=("Arial", 12), bg="blue", fg="white")
boton_derecha.pack(pady=5)

# Botón para cerrar la aplicación
boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit, font=("Arial", 12), bg="red", fg="white")
boton_salir.pack(pady=5)

# Iniciar el bucle principal de Tkinter
ventana.mainloop()
