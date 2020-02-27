from tkinter import *
#import tkinter as tk
from math import *
from cmath import pi, acos, asin, sin



#class ordenador():
    #def __inni__(self):
     
        
        #Ubicar Botones
        #botones=[button1,button2,button3,button4,button5,button6,button7,button8,button9,button10,button2nd]


#calculadora = ordenador()
    

#####################################################################################################################
#Creamos una variable que pertenece a la clase ventana por lo cual es una ventana
ventanaprin = Tk()
#ahora debemos de agregar los atributos de la ventana principal
ventanaprin.title("CALCULADORA CIENTIFICA")
ventanaprin.geometry("700x625")
ventanaprin.iconbitmap("calculator.ico")
ventanaprin.config(background="Gray22")

estado = IntVar()
estado.set(1)  # Mostrar Barra de Estado
                         
# DEFINIR BARRA DE MENÚ DE LA APLICACION:
        
barramenu = Menu(ventanaprin)
ventanaprin['menu'] = barramenu

menu1 = Menu(barramenu)
menu2 = Menu(barramenu)
barramenu.add_cascade(menu=menu1, label='Triglometria')
barramenu.add_cascade(menu=menu2, label='Funciones')

menu1.add_command(label='Sin',command=lambda:btnClick(sin),underline=0,compound=LEFT)
menu1.add_separator()  # Agrega un separador
menu1.add_command(label='Cos',command=lambda:btnClick(cos),underline=0,compound=RIGHT)
menu1.add_separator()  # Agrega un separador
menu1.add_command(label='Tan',command=lambda:btnClick(tan),underline=0,compound=LEFT)


#DEFINIR VARIABLES DE LAS FUNCIONES
input_text=StringVar()
operador=""

#DEFINIR FUNCIONES
def btnClick(num):
    global operador
    operador=operador+str(num)
    if num is None:
        operador-=operador
    input_text.set(operador)

def operacion():
    global operador
    try:
        opera=eval(operador)
    except:
        clear()
        opera("ERROR")
    input_text.set(opera)

def clear():
    global operador
    operador=("")
    input_text.set(operador)


History=Label(ventanaprin,font=("arial",20,"bold"),width=10,height=20,fg="black",bd=10,relief="solid",bg="gray22",justify="right").pack(side="right",fill="y")
Display=Entry(ventanaprin,font=("arial",20,"bold"),width=22,fg="black",bd=20,insertwidth=4,bg="white",justify="right",textvariable=input_text).pack(side="top",fill="x")#place(x=10,y=60)
#operaciones=Label(ventanaprin,font=("arial",20,"bold"),width=10,height=20,fg="black",bd=10,relief="solid",bg="gray70",justify="left").pack(side="bottom",fill="x")

#DEFINIR EL TAMAÑO Y COLOR DE LOS BOTONES
button_w=11
button_h=3
button_c=("gray11")
acti_bg=("white")
acti_fg=("black")
#DEFINIR EL COLOR DEL FONDO
button_text_c=("white")

#DEFINIR BOTONES

button2nd=Button(ventanaprin,text="2^nd",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:btnClick("pi")).place(x=17,y=125)

buttonPi=Button(ventanaprin,text="π",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:btnClick(pi)).place(x=107,y=125)

buttonE=Button(ventanaprin,text="e",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:btnClick(e)).place(x=197,y=125)

buttonC=Button(ventanaprin,text="C",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=clear).place(x=287,y=125)

buttonDel=Button(ventanaprin,text="DEL",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:btnClick(None)).place(x=377,y=125)

#Segunda Fila
buttonx2=Button(ventanaprin,text="x"+ u"\2072",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:btnClick("pi")).place(x=17,y=190)

button1x=Button(ventanaprin,text="1/x",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:btnClick("pi")).place(x=107,y=190)

buttonxx=Button(ventanaprin,text="[x]",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:btnClick("pi")).place(x=197,y=190)

buttonExp=Button(ventanaprin,text="EXP",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:btnClick("**")).place(x=287,y=190)

buttonMod=Button(ventanaprin,text="MOD",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:btnClick("pi")).place(x=377,y=190)

#Tercera Fila
buttonx3=Button(ventanaprin,text="x"+u"\2073",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:btnClick("pi")).place(x=17,y=255)

buttonPiz=Button(ventanaprin,text="(",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:btnClick("pi")).place(x=107,y=255)

buttonPde=Button(ventanaprin,text=")",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:btnClick("pi")).place(x=197,y=255)

buttonN=Button(ventanaprin,text="n!",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:btnClick("pi")).place(x=287,y=255)

buttonDiv=Button(ventanaprin,text=u"\00F7",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:btnClick("pi")).place(x=377,y=255)

#Cuarta Fila
buttonxy=Button(ventanaprin,text="x"+u"\209F",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:btnClick("pi")).place(x=17,y=320)

button7=Button(ventanaprin,text="7",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:btnClick(7)).place(x=107,y=320)

button8=Button(ventanaprin,text="8",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:btnClick(8)).place(x=197,y=320)

button9=Button(ventanaprin,text="9",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:btnClick(9)).place(x=287,y=320)

buttonX=Button(ventanaprin,text="X",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:btnClick("pi")).place(x=377,y=320)

#Quinta Fila
button10=Button(ventanaprin,text="10^x",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:btnClick("pi")).place(x=17,y=385)

button4=Button(ventanaprin,text="4",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:btnClick(4)).place(x=107,y=385)

button5=Button(ventanaprin,text="5",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:btnClick(5)).place(x=197,y=385)

button6=Button(ventanaprin,text="6",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:btnClick(6)).place(x=287,y=385)

buttonMenos=Button(ventanaprin,text="-",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:btnClick("-")).place(x=377,y=385)

#Sexta Fila
buttonLog=Button(ventanaprin,text="Log",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:btnClick("pi")).place(x=17,y=450)

button1=Button(ventanaprin,text="1",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:btnClick(1)).place(x=107,y=450)

button2=Button(ventanaprin,text="2",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:btnClick(2)).place(x=197,y=450)

button3=Button(ventanaprin,text="3",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:btnClick(3)).place(x=287,y=450)

buttonMas=Button(ventanaprin,text="+",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:btnClick("+")).place(x=377,y=450)

#Septima Fila
buttonIn=Button(ventanaprin,text="In",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:btnClick("Log")).place(x=17,y=515)

buttonMasoMenos=Button(ventanaprin,text="±",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:btnClick("pi")).place(x=107,y=515)

button0=Button(ventanaprin,text="0",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:btnClick(0)).place(x=197,y=515)

buttonDeci=Button(ventanaprin,text=",",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:btnClick(".")).place(x=287,y=515)

buttonIgual=Button(ventanaprin,text="=",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=operacion).place(x=377,y=515)


#Idicamos que no pare de ejecutarse la ventana
ventanaprin.mainloop()