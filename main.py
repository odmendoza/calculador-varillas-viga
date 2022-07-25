import tkinter as tk
from tkinter import OptionMenu, ttk

# Ventana principal

ventana = tk.Tk()
ventana.title("Calculadora de volumen de viga y número de varillas")
ventana.config(width=500, height=500)

# Funciones de la calculadora

def calcular():
    volumen = int(longuitud.get()) * int(altura.get()) * int(ancho.get())
    # strVarrespuestaO.set("resultado de la suma = "+str(sumar))

def validar():
    pass

def limpiar():
    pass

def number():
    try:
        int(txt_input_altura.get())
    except ValueError:
        print("pLEASE")

strVarrespuesta = (limpiar or calcular)

# Variables

longuitud = tk.IntVar()
altura = tk.IntVar()
ancho = tk.IntVar()
volumen_acero = tk.IntVar()
diametro_varilla = tk.IntVar()
volumen_viga = tk.IntVar()
cantidad_varillas = tk.StringVar()

# Ingreso de la longuitud de la viga

    # Etiqueta
lab_longuitud = ttk.Label(text="Longuitud de la viga [ m ]")
lab_longuitud.pack(pady=20, padx=300)

    # Menú de opciones
lista_longuitudes = ['9 m', '10 m', '11 m', '12 m']
droplist_longuitudes = OptionMenu(ventana, longuitud, *lista_longuitudes)
# droplist_longuitudes.config(width=200)
longuitud.set('Seleccione la longitud')
# droplist_longuitudes.place(width=200, height=25)
droplist_longuitudes.pack(pady=5)

# Ingreso de la altura de la viga

    # Etiqueta
lab_altura = ttk.Label(text="Altura de la viga [ cm ]")
lab_altura.pack(pady=20, padx=300)

    # Entrada por teclado
txt_input_altura = ttk.Entry(textvariable=altura)
txt_input_altura.pack(pady=5)

# Ingreso del ancho de la viga

    # Etiqueta
lab_ancho = ttk.Label(text="Ancho de la viga [ cm ]")
lab_ancho.pack(pady=20, padx=300)

    # Entrada por teclado
txt_input_ancho = ttk.Entry(textvariable=ancho)
txt_input_ancho.pack(pady=5)

# Ingreso del volumen del acero

    # Etiqueta
lab_volumen_acero = ttk.Label(text="Volumen del acero [ cm3 ]")
lab_volumen_acero.pack(pady=20, padx=300)

    # Entrada por teclado
txt_input_volumen_acero = ttk.Entry(textvariable=volumen_acero)
txt_input_volumen_acero.pack(pady=5)

# Entrada del diámetro de la varilla

    # Etiqueta
lab_diametro_varilla = ttk.Label(text="Diámetro de la varilla [ mm ]")
lab_diametro_varilla.pack(pady=20, padx=300)

    # Entrada por teclado
lista_diametros = ['6 mm', '8 mm', '10 mm', '12 mm']
droplist_diametro_varilla = OptionMenu(ventana, diametro_varilla, *lista_diametros)
# droplist_diametro_varilla.config(width=200)
diametro_varilla.set('Seleccione el diámetro')
# droplist_diametro_varilla.place(x=250, y=140, width=200, height=25)
droplist_diametro_varilla.pack(pady=5)

# Botón de calcular
btn_calcular = ttk.Button(text=".:  Calcular  :.", command=calcular)
btn_calcular.pack(pady=20)

# Salida del volumen de la viga

lab_volumen_viga = ttk.Label(text="")
# lab_volumen_viga.place(x=20, y=250)
lab_volumen_viga.pack(pady=20)

# Salida de la cantidad de varillas

lab_cantidad_varillas = ttk.Label(text="")
lab_cantidad_varillas.pack(pady=20)

# Entrada de datos

# txt_input_longuitud = ttk.Entry(textvariable=longuitud)
# txt_input_longuitud.place(x=250, y=20, width=200)



# txt_volumen_viga = ttk.Entry(textvariable=volumen_viga)
# txt_volumen_viga.place(x=250, y=110, width=200)

# txtInputDiametroVarilla=ttk.Entry(textvariable=diametro_varilla)
# txtInputDiametroVarilla.place(x=250,y=140,width=200)

# txtNumber2=ttk.Entry(textvariable=strVarNumero2)
# txtNumber2.place(x=125,y=50,width=200)
#
# txtSaludo=ttk.Entry(textvariable=strVarrespuestaO)
# txtSaludo.place(x=125,y=270,width=200)

# Botones de la calculadora



# btnrestar= ttk.Button(text=".:Restar:.",command=restar)
# btnrestar.place(x=120,y=75)

# Ejecución de la ventana
ventana.mainloop()
