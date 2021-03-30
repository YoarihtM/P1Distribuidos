import relojes, time
from tkinter import *
import tkinter
import threading
import sys


############ cerrar ventana #############
def salir():
    global valor1
    valor1 = False
    global valor2
    valor2 = False
    global valor3
    valor3 = False
    global valor4
    valor4 = False
    root.destroy()

########### editar reloj 1 ################

def edit1():
    global valor1
    valor1 = False
    edicion = Toplevel(root)
    edicion.config(width = 300, height=130)
    edicion.title('Cambiar hora')
    lblHoraEdit = Label(edicion, text='Hora', font=('Open Sans', 13))
    lblHoraEdit.place(x=25, y=20)
    horaEdit = Entry(edicion, width=7)
    horaEdit.place(x=25, y=50)
    lblMinEdit = Label(edicion, text='Minutos', font=('Open Sans', 13))
    lblMinEdit.place(x=95, y=20)
    minEdit = Entry(edicion, width=11)
    minEdit.place(x=95, y=50)
    lblSegEdit = Label(edicion, text='Segundos', font=('Open Sans', 13))
    lblSegEdit.place(x=185, y=20)
    segEdit = Entry(edicion, width=13)
    segEdit.place(x=185, y=50)

    guardarBtn = Button(edicion, text='Guardar', command=salir)
    guardarBtn.place(x=120, y=85)

############ creacion ventana #############
root = Tk()
root.title('Practica 1 - Desarrollo de Sistemas Distribuidos')
frame = Frame()
frame.pack()
frame.config(width=800, height=400)


############ reloj 1 #############
def encender1():
    global valor1
    valor1 = True

    while valor1:
        lblTiempo1.config(text=relojes.imprimirHora(relojes.relojLocal()))
        root.update()

def relojEditado1():
    global valor1
    valor1 = True

    while

############ reloj2 #############
def encender2():
    global valor2
    valor2 = True

    while valor2:
        lblTiempo2.config(text=relojes.imprimirHora(relojes.relojGlobal()))
        root.update()
    time.sleep(2)

############ reloj3 #############
def encender3():
    global valor3
    valor3 = True

    while valor3:
        lblTiempo3.config(text=relojes.imprimirHora(relojes.relojEur()))
        root.update()

############ reloj4 #############
def encender4():
    global valor4
    valor4 = True

    while valor4:
        lblTiempo4.config(text=relojes.imprimirHora(relojes.relojIndia()))
        root.update()

############ reloj1 vista #############
lblReloj1 = Label(frame, text = 'Reloj 1', font=('Open Sans', 15))
lblReloj1.place(x=30, y=15)
editar1Btn = Button(frame, text='', command=edit1)
editar1Btn.place(x=100, y=15)
lblTiempo1 = Label(frame, text='--:--:--', font=('Digital-7 Mono', 70))
lblTiempo1.place(x=30, y=60)

############ reloj2 vista #############
lblReloj2 = Label(frame, text = 'Reloj 2', font=('Open Sans', 15))
lblReloj2.place(x=30, y=160)
editar2Btn = Button(frame, text='', command=edit1)
editar2Btn.place(x=100, y=160)
lblTiempo2 = Label(frame, text='--:--:--', font=('Digital-7 Mono', 70))
lblTiempo2.place(x=30, y=205)

############ reloj3 vista #############
lblReloj3 = Label(frame, text = 'Reloj 3', font=('Open Sans', 15))
lblReloj3.place(x=420, y=15)
editar3Btn = Button(frame, text='', command=edit1)
editar3Btn.place(x=500, y=15)
lblTiempo3 = Label(frame, text='--:--:--', font=('Digital-7 Mono', 70))
lblTiempo3.place(x=420, y=60)

############ reloj4 vista #############
lblReloj4 = Label(frame, text = 'Reloj 4', font=('Open Sans', 15))
lblReloj4.place(x=420, y=160)
editar4Btn = Button(frame, text='', command=salir)
editar4Btn.place(x=500, y=160)
lblTiempo4 = Label(frame, text='--:--:--', font=('Digital-7 Mono', 70))
lblTiempo4.place(x=420, y=205)

############ declaracion de hilos #############
relojMx = threading.Thread(target=encender1)
relojMx2 = threading.Thread(target=encender2)
relojMx3 = threading.Thread(target=encender3)
relojMx4 = threading.Thread(target=encender4)

############ inicializacion de hilos #############
relojMx.start()
relojMx2.start()
relojMx3.start()
relojMx4.start()

############ boton salir #############
terminarBtn = Button(frame, text='Salir', command=salir)
terminarBtn.place(x=730, y=350)

root.mainloop()