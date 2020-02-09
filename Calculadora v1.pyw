from tkinter import *

raiz = Tk()
raiz.title("Calculadora - Santi R.")
raiz.iconbitmap("calculadora.ico")
raiz.resizable(0,0)

miFrame = Frame(raiz)
miFrame.pack()
miFrame.config(bd=20, background="#D9D9D9")

operacion = ""
resultado = 0
operacion_anterior = ""

#------------------------------pantalla---------------------------------
numeroPantalla = StringVar()
numeroPantalla.set("0")

pantalla = Entry(miFrame, width=20, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, pady=10, padx=10, columnspan=4)
pantalla.config(background="#BFBFBF", fg="#0D0D0D", justify="right",
                font="Courier 25 bold")

#---------------------------Pulsaciones Teclado------------------------------

def numeroPulsado(num):
    global operacion_anterior
    if operacion_anterior or numeroPantalla.get() == "0":
        numeroPantalla.set(num)
        resultado = numeroPantalla.get()
        operacion_anterior = False
    else:
        numeroPantalla.set(numeroPantalla.get() + num)
        resultado = numeroPantalla.get()

def borrarContenido():
    global resultado
    global operacion
    numeroPantalla.set("0")
    operacion = ""
    resultado = 0

def colocarComa():
    tieneComa = 0
    for i in numeroPantalla.get():
        if i == ".":
            tieneComa += 1
        else:
            pass
    if tieneComa == 0:
        numeroPulsado(".")
    else:
        pass

def sumar():
    global operacion
    global operacion_anterior
    global resultado
    if operacion != "":
        resultado_parcial(float(numeroPantalla.get()))
    else:
        resultado = float(numeroPantalla.get())
    operacion_anterior = True
    operacion = "s"


def restar():
    global operacion
    global operacion_anterior
    global resultado
    if operacion != "":
        resultado_parcial(float(numeroPantalla.get()))
    else:
        resultado = float(numeroPantalla.get())
    operacion = "r"
    operacion_anterior = True


def multiplicar():
    global operacion
    global resultado
    global operacion_anterior

    if operacion != "":
        resultado_parcial(float(numeroPantalla.get()))
    else:
        resultado = float(numeroPantalla.get())

    operacion = "m"
    operacion_anterior = True

def dividir():
    global operacion
    global operacion_anterior
    global resultado
    if operacion != "":
        resultado_parcial(float(numeroPantalla.get()))
    else:
        resultado = float(numeroPantalla.get())

    operacion = "d"
    operacion_anterior = True

def elResultado():
    global resultado
    global operacion
    resultado_parcial(float(numeroPantalla.get()))
    resultado = 0
    operacion = "resultado"

#----------- Funcion que entrega el resultado cuando se apreta + - * / -------------

def resultado_parcial(num):
    global resultado
    global operacion

    if operacion == "s":
        resultado += num
    elif operacion == "r":
        resultado -= num
    elif operacion == "m":
        resultado *= num
    elif operacion == "d":
        try:
            resultado /= num
        except ZeroDivisionError:
            resultado = "Math Error"
    numeroPantalla.set(resultado)



#---------------------------Botones fila 2------------------------------
boton7 = Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton7.config(bd=4, font="Arial 28")
boton8 = Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton8.config(bd=4, font="Arial 28")
boton9 = Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
boton9.config(bd=4, font="Arial 28")
botonMult = Button(miFrame, text="X", width=3, command=lambda:multiplicar())
botonMult.grid(row=2, column=4)
botonMult.config(bd=4, font="Arial 28")

#---------------------------Botones fila 3------------------------------
boton4 = Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton4.config(bd=4, font="Arial 28")
boton5 = Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton5.config(bd=4, font="Arial 28")
boton6 = Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
boton6.config(bd=4, font="Arial 28")
botonRest = Button(miFrame, text="-", width=3, command=lambda:restar())
botonRest.grid(row=3, column=4)
botonRest.config(bd=4, font="Arial 28")

#---------------------------Botones fila 4------------------------------
boton1 = Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton1.config(bd=4, font="Arial 28")
boton2 = Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton2.config(bd=4, font="Arial 28")
boton3 = Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
boton3.config(bd=4, font="Arial 28")
botonSum = Button(miFrame, text="+", width=3, command=lambda:sumar())
botonSum.grid(row=4, column=4)
botonSum.config(bd=4, font="Arial 28")

#---------------------------Botones fila 5------------------------------
botonDiv = Button(miFrame, text="/", width=3, command=lambda:dividir())
botonDiv.grid(row=5, column=1)
botonDiv.config(bd=4, font="Arial 28")
boton0 = Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=2)
boton0.config(bd=4, font="Arial 28")
botonComa = Button(miFrame, text=",", width=3, command=lambda:colocarComa())
botonComa.grid(row=5, column=3)
botonComa.config(bd=4, font="Arial 28")
botonIgual = Button(miFrame, text="=", width=3, command=lambda:elResultado())
botonIgual.grid(row=5, column=4)
botonIgual.config(bd=4, font="Arial 28")

#---------------------------Botones fila 6------------------------------
botonBorr = Button(miFrame, text="C", width=3, command=borrarContenido)
botonBorr.grid(row=6, column=1)
botonBorr.config(bd=4, font="Arial 28")
# boton0 = Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
# boton0.grid(row=5, column=2)
# botonComa = Button(miFrame, text=",", width=3, command=lambda:numeroPulsado(","))
# botonComa.grid(row=5, column=3)
# botonIgual = Button(miFrame, text="=", width=3)
# botonIgual.grid(row=5, column=4)

raiz.mainloop()

#------------------------------ PROBLEMAS ----------------------------------
# El boton de sumar
# Division por cero

