import tkinter as tk
import os
from coty_ver1123 import cotizador

# Variables globales para los valores por defecto "n"
desc_tarj = "n"
desc_pool = "n"
desc_comercial = "n"
desc_continuidad_pp = "n"
# Función para mostrar la pantalla 2 y ejecutar el cotizador


def copiar_al_portapapeles(texto):
    # Borra el contenido actual del portapapeles
    ventana.clipboard_clear()
    # Agrega el texto al portapapeles
    ventana.clipboard_append(texto)
    # Asegúrate de que los cambios se realicen
    ventana.update()


def mostrar_pantalla2():
    global aporte, monotributo_ind, preexistencia, gestion, ages
    aporte = int(aporte_rd_entry.get()) if aporte_rd_entry.get() else 0
    monotributo_ind = int(monto_monotributo_entry.get()
                          ) if monto_monotributo_entry.get() else 0
    preexistencia = int(costo_preexistencias_entry.get()
                        ) if costo_preexistencias_entry.get() else 0

    ubicacion = "C" if ubicacion_var.get() == "Córdoba" else "R"

    if gestion_var.get() == "1_Relación de Dependencia":
        gestion = 1
    elif gestion_var.get() == "2_Monotributo":
        gestion = 2
    elif gestion_var.get() == "3_Prepago":
        gestion = 3

    # Almacena las edades ingresadas como una lista de números enteros
    ages = [int(age) for age in edades_entry.get().split(',')]

    pantalla1.pack_forget()
    pantalla2.pack()
    debug = False
    debug2 = True
    desc_tarj = "s" if desc_tarj_var.get() else "n"
    desc_pool = "s" if desc_pool_var.get() else "n"
    desc_comercial = "s" if desc_comercial_var.get() else "n"
    desc_continuidad_pp = "s" if desc_continuidad_pp_var.get() else "n"

    resultado = cotizador(debug, debug2, ubicacion, gestion, ages, desc_tarj, desc_pool,
                          desc_comercial, desc_continuidad_pp, aporte, monotributo_ind, preexistencia, mes_var.get())
    resultados_text.config(text=resultado)


# Función para mostrar la pantalla 3
def mostrar_pantalla3():
    global aporte, monotributo_ind, preexistencia, gestion, ages
    aporte = int(aporte_rd_entry.get()) if aporte_rd_entry.get() else 0
    monotributo_ind = int(monto_monotributo_entry.get()
                          ) if monto_monotributo_entry.get() else 0
    preexistencia = int(costo_preexistencias_entry.get()
                        ) if costo_preexistencias_entry.get() else 0

    # Almacena las edades ingresadas como una lista de números enteros
    ages = [int(age) for age in edades_entry.get().split(',')]

    pantalla2.pack_forget()
    pantalla3.pack()

    # Cambia el valor de 'choice' a 's' directamente
    choice = "s"

    debug = False
    debug2 = False
    ubicacion = "C" if ubicacion_var.get() == "Córdoba" else "R"
    if gestion_var.get() == "1_Relación de Dependencia":
        gestion = 1
    elif gestion_var.get() == "2_Monotributo":
        gestion = 2
    elif gestion_var.get() == "3_Prepago":
        gestion = 3
    desc_tarj = "s" if desc_tarj_var.get() else "n"
    desc_pool = "s" if desc_pool_var.get() else "n"
    desc_comercial = "s" if desc_comercial_var.get() else "n"
    desc_continuidad_pp = "s" if desc_continuidad_pp_var.get() else "n"
    resultado = cotizador(debug, debug2, ubicacion, gestion, ages, desc_tarj, desc_pool,
                          desc_comercial, desc_continuidad_pp, aporte, monotributo_ind, preexistencia, mes_var.get())
    resultados_text.config(text=resultado)

    copiar_al_portapapeles(resultado)
    ventana.after(500, mostrar_pantalla2)


# Función para volver a la pantalla 1
def volver_a_pantalla1():
    pantalla2.pack_forget()
    pantalla3.pack_forget()
    pantalla1.pack()


ventana = tk.Tk()
ventana.title("Mi Aplicación con Tkinter")
font_style = ('Helvetica', 9)
font_style2 = ('Helvetica', 6)

pantalla1 = tk.Frame(ventana)

label_mes = tk.Label(pantalla1, text="*Mes:", font=font_style)
label_mes.pack(pady=10)

mes_var = tk.StringVar()
mes_menu = tk.OptionMenu(pantalla1, mes_var, "10", "11")
mes_menu.pack()

label_ubicacion = tk.Label(pantalla1, text="*Ubicación:", font=font_style)
label_ubicacion.pack(pady=10)

ubicacion_var = tk.StringVar()
ubicacion_menu = tk.OptionMenu(pantalla1, ubicacion_var, "Córdoba", "La Rioja")
ubicacion_menu.pack()

label_gestion = tk.Label(pantalla1, text="*Gestión:", font=font_style)
label_gestion.pack(pady=10)

gestion_var = tk.StringVar()
gestion_menu = tk.OptionMenu(
    pantalla1, gestion_var, "1_Relación de Dependencia", "2_Monotributo", "3_Prepago")
gestion_menu.pack()

label_edades = tk.Label(pantalla1, text="*Edades:", font=font_style)
label_edades.pack(pady=10)

edades_entry = tk.Entry(pantalla1, font=font_style)
edades_entry.pack()

# Establecer valores predeterminados
mes_var.set("11")
ubicacion_var.set("La Rioja")
gestion_var.set("1_Relación de Dependencia")


desc_comercial_var = tk.BooleanVar()
desc_pool_var = tk.BooleanVar()
desc_tarj_var = tk.BooleanVar()
desc_continuidad_pp_var = tk.BooleanVar()

check_desc_tarj = tk.Checkbutton(
    pantalla1, text="Desc. Tarjeta", variable=desc_tarj_var, font=font_style, anchor="w")
check_desc_tarj.pack(anchor="w")

check_desc_pool = tk.Checkbutton(
    pantalla1, text="Desc. Pool", variable=desc_pool_var, font=font_style, anchor="w")
check_desc_pool.pack(anchor="w")

check_desc_comercial = tk.Checkbutton(
    pantalla1, text="Desc. Comercial", variable=desc_comercial_var, font=font_style, anchor="w")
check_desc_comercial.pack(anchor="w")

check_desc_continuidad_pp = tk.Checkbutton(
    pantalla1, text="Desc. Continuidad/Prepago", variable=desc_continuidad_pp_var, font=font_style, anchor="w")
check_desc_continuidad_pp.pack(anchor="w")

label_aporte_rd = tk.Label(
    pantalla1, text="Aporte (entrada de texto - RD):", font=font_style)
label_aporte_rd.pack(pady=10)

aporte_rd_entry = tk.Entry(pantalla1, font=font_style)
aporte_rd_entry.pack()

label_monto_monotributo = tk.Label(
    pantalla1, text="Monto Monotributo Individual:", font=font_style)
label_monto_monotributo.pack(pady=10)

monto_monotributo_entry = tk.Entry(pantalla1, font=font_style)
monto_monotributo_entry.pack()

label_costo_preexistencias = tk.Label(
    pantalla1, text="Costo de Preexistencias:", font=font_style)
label_costo_preexistencias.pack(pady=10)

costo_preexistencias_entry = tk.Entry(pantalla1, font=font_style)
costo_preexistencias_entry.pack()

cotizar_button = tk.Button(pantalla1, text="Cotizar",
                           font=font_style, command=mostrar_pantalla2)
cotizar_button.pack(pady=20)

pantalla1.pack()

pantalla2 = tk.Frame(ventana)

resultados_text = tk.Label(pantalla2, text="", font=font_style2)
resultados_text.pack(pady=20)

siguiente_button = tk.Button(
    pantalla2, text="Copiar", font=font_style, command=mostrar_pantalla3)
siguiente_button.pack(pady=20)

volver_button = tk.Button(pantalla2, text="Volver a Formulario",
                          font=font_style, command=volver_a_pantalla1)
volver_button.pack()

pantalla3 = tk.Frame(ventana)

# Aquí puedes agregar elementos adicionales para mostrar los resultados finales para el cliente

volver_button2 = tk.Button(
    pantalla3, text="Volver a Formulario", font=font_style, command=volver_a_pantalla1)
volver_button2.pack()


aporte = 0
monotributo_ind = 0
preexistencia = 0
gestion = 1  # Valor por defecto, puede ser modificado por el usuario

ventana.mainloop()
