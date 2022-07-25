import tkinter as tk
import math
import numpy as np
from tkinter import OptionMenu, ttk

# Ventana principal

ventana = tk.Tk()
ventana.title("Calculadora de volumen de viga y número de varillas")
ventana.config(width=500, height=500)

# Funciones

def calcular():
    # Validamos los datos de entrada a través de la función datos_entrada_validos()
    if datos_entrada_validos():

        # Como los datos de entrada son válidos, obtenemos dichos valores
        longuitud_ = int(longuitud.get().replace(" m", ""))
        altura_ = int(altura.get())
        ancho_ = int(ancho.get())
        volumen_acero_ = int(volumen_acero.get())
        diametro_varilla_ = int(diametro_varilla.get().replace(" mm", ""))

        # Cálculo de el volumen de la viga
        volumen_viga_cm3 = longuitud_ * altura_ * ancho_
        volumen_viga_m3 = volumen_viga_cm3 / 100
        lab_volumen_viga.config(text=f'El volumen de la viga es { volumen_viga_m3 } m3')

        # Cálculo del volumen de una varilla en cm
        # (( pi * d**2 ) / 4 ) * long
        volumen_1_varilla = ((math.pi * ((diametro_varilla_ / 10) ** 2)) / 4) * (longuitud_ * 100)

        # Cálculo del número de varillas
        cantidad_varillas_sin_ajustar = volumen_acero_ / volumen_1_varilla

            # Primer ajuste, sacamos la parte entera del resultado de la división
        cantidad_varillas_ajustadas = math.trunc(cantidad_varillas_sin_ajustar)

            # Segundo ajuste, si la división no es exacta redondeamos al inmediato superior
        if cantidad_varillas_sin_ajustar - cantidad_varillas_ajustadas != 0:
            cantidad_varillas_ajustadas += 1

            # Tercer ajuste, la cantidade de varillas debe ser par
        if cantidad_varillas_ajustadas % 2 != 0:
            cantidad_varillas_ajustadas += 1

        # Mostramos por pantalla la cantidad de varillas
        lab_cantidad_varillas.config(text=f'La cantidad de varillas es { cantidad_varillas_ajustadas}')

        # Graficar viga y cantidad de varillas
        graficar(altura_, ancho_, cantidad_varillas_ajustadas)


def graficar(altura, ancho, cantidad_varillas):

    # Iniciamos con una fila y dos columnas
    filas = 1
    columnas = 2

    # Aumentamos filas y columnas según la cantidad de varillas que se desea representar
    while True:
        varillas = filas * columnas
        if varillas >= cantidad_varillas:
            lab_grafico_cantidad_varillas.config(text=imprimir(altura, ancho, cantidad_varillas, filas, columnas))
            break

        # Aumentamos filas
        filas += 1

        varillas = filas * columnas
        if varillas >= cantidad_varillas:
            lab_grafico_cantidad_varillas.config(text=imprimir(altura, ancho, cantidad_varillas, filas, columnas))
            break

        # Aumentamos columnas
        columnas += 1


def imprimir(altura, ancho, varillas, filas, columnas):

    # Inicializamos un arreglo de numpy con *'s
    viga = np.full((filas, columnas), "*")

    # Calculamos las varillas iniciales que tiene el arreglo inicializado
    varillas_iniciales = filas * columnas

    # y calculamos las varillas que debemos quitar
    quitar_varillas = varillas_iniciales - varillas

    f = 1
    c = 1

    # Quitamos las varillas de la diagonal principal del arreglo de numpy
    while quitar_varillas != 0:
        # Reemplazamos las varillas que deseamos quitar por el signo de ?
        viga[f][c] = "?"
        quitar_varillas -= 1
        if c + 1 == columnas - 1 or f + 1 == filas -1:
            f += 1
            c = 1
        else:
            c += 1
            f += 1

    # Construmos la vida con las varillas que contiene, la altura y el ancho
    viga_str = f"Altura -> { altura } m\n\n"
    viga_str += np.array2string(viga).replace("[["," [").replace("]]","]").replace("'", "   ").replace("[", " |  [")
    viga_str += f"\n"
    viga_str += "_" * 20
    viga_str += f"\n\nAncho -> { ancho } m"

    return viga_str


def datos_entrada_validos():
    # Si se produce un error de conversión a entero signfica que el usuario ingresó mal el número,
    # se retorna False y el programa se detiene indicándo al usuario cuál es el error.

    # Validamos la entrada de la longuitud de la viga
    try:
        int(longuitud.get().replace(" m", ""))
    except ValueError:
        lab_volumen_viga.config(text="Por favor, seleccione la longuitud de la viga")
        return False

    # Validamos la entrada de la altura de la viga
    try:
        altura_ = int(altura.get())
        if altura_ == 0:
            lab_volumen_viga.config(text="Por favor, ingrese una altura mayor que cero (0)")
            return False
    except ValueError:
        lab_volumen_viga.config(text="Por favor, ingrese correctamente la altura de la viga")
        return False

    # Validamos la entrada del ancho de la viga
    try:
        ancho_ = int(ancho.get())
        if ancho_ == 0:
            lab_volumen_viga.config(text="Por favor, ingrese un ancho mayor que cero (0)")
            return False
    except ValueError:
        lab_volumen_viga.config(text="Por favor, ingrese correctamente el ancho de la viga")
        return False

    # Validamos la entrada del volumen del acero
    try:
        volumen_acero_ = int(volumen_acero.get())
        if volumen_acero_ == 0:
            lab_volumen_viga.config(text="Por favor, ingrese un volumen de acero mayor que cero (0)")
            return False
    except ValueError:
        lab_volumen_viga.config(text="Por favor, ingrese correctamente el volumen del acero")
        return False

    # Validamos la entrada del diametro de la varilla
    try:
        int(diametro_varilla.get().replace(" mm", ""))
    except ValueError:
        lab_volumen_viga.config(text="Por favor, seleccione el diámetro de varilla")
        return False
    # Si no se lanza ningún error, significa que el usuario ingresó todos los valores correctamente,
    # se devuelve un valor True y el programa continía con la ejecución normal

    return True


# Variables

longuitud = tk.StringVar()
altura = tk.IntVar()
ancho = tk.IntVar()
volumen_acero = tk.IntVar()
diametro_varilla = tk.StringVar()

# Ingreso de la longuitud de la viga

# Etiqueta
lab_longuitud = ttk.Label(text="Longuitud de la viga [ m ]")
lab_longuitud.pack(pady=20, padx=300)

# Menú de opciones
lista_longuitudes = ['9 m', '10 m', '11 m', '12 m']
droplist_longuitudes = OptionMenu(ventana, longuitud, *lista_longuitudes)
longuitud.set('Seleccione la longitud')
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
diametro_varilla.set('Seleccione el diámetro')
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

# Salida gráfico de la cantidad de varillas

lab_grafico_cantidad_varillas = ttk.Label(text="")
lab_grafico_cantidad_varillas.pack(pady=20, padx=300)

# Ejecución de la ventana
ventana.mainloop()
