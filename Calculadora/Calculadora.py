from tkinter import *
#MODULO QUE CONTIENE CASI TODAS LAS OPERACIONES MATEMATICAS QUE HE USADO
from math import *

### Definición de la clase Calculadora
class Calculadora():
    #FUNCION PRINCIPAL
    def __init__(self):
        self.numeroMemoria = 0.0
        self.numeroDisplay = 0.0
        self.asignarValorNuevo = True
        self.asignandoParteEntera = True
        self.posicionDecimal = 0
        self.operacionActiva = ""
        self.operacionPendiente = False

    #FUNCION ACTUALIZA LA PANTALLA DESPUES DE CADA OPERACION O ACCION
    def actualizaDisplay(self):
        strNumeroMemoria = str(self.numeroMemoria)
        textNumeroMemoria = ' ' * (125 - len(strNumeroMemoria)) + strNumeroMemoria
        if self.operacionPendiente:
            textNumeroMemoria += ' ' + self.operacionActiva
        textoMemoria.set(textNumeroMemoria)
        
        strNumeroDisplay = str(self.numeroDisplay)
        textNumeroDisplay = ' ' * (125 - len(strNumeroDisplay)) + strNumeroDisplay
        textoDisplay.set(textNumeroDisplay)
        
    #FUNCION PARA EL BOTON DEL DE LA CALCULADORA, NOS SIRVE PARA BORRAR UN NUMERO O ALGO DESPUES DE HABERLO INTRODUCCIDO
    def BorrarNumero(self):
        try:
            resultado=self.numeroDisplay
            resultado=str(resultado)
            resultado=resultado[0:len(resultado)-1]
            self.numeroDisplay=int(resultado)
        except:
            self.numeroDisplay = 0.0
            self.asignarValorNuevo = True
            self.asignandoParteEntera = True
            self.posicionDecimal = 0
            self.operacionActiva = ""
            self.operacionPendiente = False
                
        self.actualizaDisplay()

    #FUNCION QUE AÑADE UN NUMERO CUANDO LO PULSAMOS
    def pulsaBotonNumero(self, valor):
        if self.asignarValorNuevo:
            self.numeroDisplay = 0
            self.asignarValorNuevo = False
        
        if self.asignandoParteEntera:
            self.numeroDisplay = self.numeroDisplay * 10 + valor
        else:
            self.numeroDisplay += valor * (10 ** self.posicionDecimal)
            self.posicionDecimal -= 1
            
        self.actualizaDisplay()
    
    #FUNCION PARA TRABAJAR CON VALORES DECIMALES
    def pulsaBotonDecimal(self):
        self.asignandoParteEntera = False
        self.posicionDecimal = -1
        self.numeroDisplay *= 1.0
        self.actualizaDisplay() 

    #FUNCION QUE REGISTRA CADA UNA DE LAS OPERACIONES
    def ejecutaOperacion(self):
        #ARITMETICAS
        if (self.operacionActiva == "+"):
            self.numeroDisplay = self.numeroMemoria + self.numeroDisplay
        elif (self.operacionActiva == '-'):
            self.numeroDisplay = self.numeroMemoria - self.numeroDisplay
        elif (self.operacionActiva == '*'):
            self.numeroDisplay = self.numeroMemoria * self.numeroDisplay
        elif (self.operacionActiva == '/'):
            self.numeroDisplay = self.numeroMemoria / self.numeroDisplay
        elif (self.operacionActiva == '%'):
            self.numeroDisplay = self.numeroMemoria % self.numeroDisplay
        elif (self.operacionActiva == 'n!'):
            self.numeroDisplay = factorial(self.numeroMemoria)
        
        #FUNCIONES
        elif (self.operacionActiva == "fabs"):
            self.numeroDisplay = fabs(self.numeroMemoria)
        elif (self.operacionActiva == "floor"):
            self.numeroDisplay = floor(self.numeroMemoria)
        elif (self.operacionActiva == "ceil"):
            self.numeroDisplay = ceil(self.numeroMemoria)
           
        #RAICES
        elif (self.operacionActiva == 'raiz'):
            self.numeroDisplay = sqrt(self.numeroMemoria)
        elif (self.operacionActiva == 'raiz3'):
            self.numeroDisplay = round(self.numeroMemoria**(1./3.),0)
        
        #POTENCIAS
        elif (self.operacionActiva == '^2'):
            self.numeroDisplay = pow(self.numeroMemoria,2)
        elif (self.operacionActiva == '^3'):
            self.numeroDisplay = pow(self.numeroMemoria,3)
        elif (self.operacionActiva == 'x^y'):
            self.numeroDisplay = self.numeroMemoria ** self.numeroDisplay
        elif (self.operacionActiva == '10^x'):
            self.numeroDisplay = 10**self.numeroMemoria
        
        
        #EXPONECIALES Y LOGARITMICAS
        elif (self.operacionActiva == 'e'):
            self.numeroDisplay = e
        elif (self.operacionActiva == 'exp'):
            self.numeroDisplay = exp(self.numeroMemoria)
        elif (self.operacionActiva == 'log10'):
            self.numeroDisplay = log10(self.numeroMemoria)
        elif (self.operacionActiva == 'log2'):
            self.numeroDisplay = log2(self.numeroMemoria)
        
        
        #TRIGONOMETICAS
        elif (self.operacionActiva == 'sin'):
            self.numeroDisplay = sin(radians(self.numeroMemoria))
        elif (self.operacionActiva == 'asin'):
            self.numeroDisplay = asin(degrees(self.numeroMemoria))
        elif (self.operacionActiva == 'cos'):
            self.numeroDisplay = cos(radians(self.numeroMemoria))
        elif (self.operacionActiva == 'acos'):
            self.numeroDisplay = acos(degrees(self.numeroMemoria))
        elif (self.operacionActiva == 'tan'):
            self.numeroDisplay = tan(radians(self.numeroMemoria))
        elif (self.operacionActiva == 'atan'):
            self.numeroDisplay = atan(degrees(self.numeroMemoria))
        elif (self.operacionActiva == 'hypo'):
            self.numeroDisplay = hypot(self.numeroMemoria,self.numeroDisplay)
        
        #HIPERBOLICAS
        elif (self.operacionActiva == 'sinh'):
            self.numeroDisplay = sinh(self.numeroMemoria)
        elif (self.operacionActiva == 'asinh'):
            self.numeroDisplay = asinh(self.numeroMemoria)
        elif (self.operacionActiva == 'cosh'):
            self.numeroDisplay = cosh(self.numeroMemoria)
        elif (self.operacionActiva == 'acosh'):
            self.numeroDisplay = acosh(self.numeroMemoria)
        elif (self.operacionActiva == 'tanh'):
            self.numeroDisplay = tanh(self.numeroMemoria)
        elif (self.operacionActiva == 'atanh'):
            self.numeroDisplay = atanh(self.numeroMemoria)
        
        #MCD y mcm
        elif (self.operacionActiva == 'mcd'):
            self.numeroDisplay = gcd(self.numeroMemoria,self.numeroDisplay)
        elif (self.operacionActiva == 'mcm'):
            mcd=gcd(self.numeroMemoria,self.numeroDisplay)
            mcm=self.numeroMemoria*self.numeroDisplay/mcd
            self.numeroDisplay = mcm
        
        #OPERACIONES SUELTAS
        elif (self.operacionActiva == 'pi'):
            self.numeroDisplay = pi
        elif (self.operacionActiva == '1/x'):
            self.numeroDisplay = 1 / self.numeroMemoria
        elif (self.operacionActiva == '+-'):
            if self.numeroMemoria > 0:
                r=self.numeroMemoria=-self.numeroMemoria
                self.numeroDisplay = r
            elif self.numeroMemoria < 0:
                r=self.numeroMemoria=abs(self.numeroMemoria)
                self.numeroDisplay = r
            

        self.asignarValorNuevo = True
        self.asignandoParteEntera = True
        self.operacionPendiente = False

    #FUNCION QUE NOS SIRVE PARA REGISTRAR UNA OPREACION NUEVA Y VERIFICARSU HAY ALGUNA PENDIENTE
    def registraOperacion(self, operacion):
        if (self.operacionPendiente):
            self.ejecutaOperacion()

        self.operacionPendiente = True
        self.operacionActiva = operacion
        self.asignarValorNuevo = True
        self.asignandoParteEntera = True

        self.numeroMemoria = self.numeroDisplay
        self.numeroDisplay = 0.0

        self.actualizaDisplay()

    #FUNCION NOS MUESTRA EL RESULTADO DE ALGUNA OPERACION
    def ejecutaIgual(self):
        if (self.operacionPendiente):
            self.ejecutaOperacion()
        self.numeroMemoria = 0.0
        self.operacionPendiente = False
        self.asignarValorNuevo = True
        self.asignandoParteEntera = True
        
        self.actualizaDisplay()

    #FUNCION QUE NOS REINICIA LA CALCULADORA
    def limpiaCalculadora(self):
        self.numeroMemoria = 0.0
        self.numeroDisplay = 0.0
        self.asignarValorNuevo = True
        self.asignandoParteEntera = True
        self.posicionDecimal = 0
        self.operacionActiva = ""
        self.operacionPendiente = False

        self.actualizaDisplay()  
   

# Creación de un objeto de tipo Calculadora            
calculadora = Calculadora()

# Creación de la ventana principal del GUI
#Creamos una variable que pertenece a la clase ventana por lo cual es una ventana
ventanaprin = Tk()

#ahora debemos de agregar los atributos de la ventana principal
ventanaprin.title("CALCULADORA CIENTIFICA WINDOWS 10 #made in china")
ventanaprin.geometry("500x630")
ventanaprin.resizable(width=False,height=False)
ventanaprin.iconbitmap("calculator.ico")
ventanaprin.config(background="Gray22")

#CREAMOS Y CONFIGURAJMOS UN FRAME PRINCIPAL QUE ALOJARA LOS DEMAS FRAMES
marcoPrin=Frame(ventanaprin,cursor="pirate")
marcoPrin.pack()
marcoPrin.config(bg="Gray22",width=780,height=630)

#CREAMOS UN FRAME SEGUNDARIO QUE SERA EL QUE CONTENGA LAS PANTALLAS,ESTE FRAME VA DENTRO DEL PRINCIPAL
marcoDisplay=Frame(marcoPrin,bg="Gray22")
marcoDisplay.grid(row=0, column = 0,pady=10)

#CREAMOS OTRO FRAME SEGUNDARIO QUE SERA EL QUE CONTENGA LOS BOTONES,ESTE FFRAME VA DENTRO DEL PRINCIPAL PERO EN OTRA FILA
marcoButton=Frame(marcoPrin,bg="Gray22")
marcoButton.grid(row=1,column=0)

#CREAMOS LA VARIABLE QUE ALAMCENARA LAS OPERACIONES Y NUMEROS EN MEMORIA Y SERA DE TIPO STRING
textoMemoria = StringVar()
textoMemoria.set('')

#CONFIGURAMOS UNA PRIMERA ETQUETA QUE MOSTRARA LOS VALORES GUARDADOS EN MEMORIA
ShowMemoria=Label(marcoDisplay,textvariable=textoMemoria,
                     width = 65, height = 3,
                     bd=5, relief='ridge',
                     bg = 'white',
                     padx = 3, pady = 0).grid(row = 0, column = 0, pady = 7,padx = 5)

#CREAOS LA VARIABLE DONDE VAMOS INTRODUCIENDO NUMEROS Y OPERACIONES SIN ENTRAR EN MEMORIA, SERA DE TIPO STRING
textoDisplay = StringVar()
textoDisplay.set('')

#CONFIGURAMOS LA SEGUNDA ETIQUETA QUE MOSTRAR LOS VALORES GUARDADOS EN DISPLAY
ShowDisplay=Label(marcoDisplay,textvariable=textoDisplay,
                  width = 65, height = 3,
                  bd=5, relief='ridge',
                  bg = 'white',
                  padx = 3, pady = 0).grid(row = 1, column = 0, pady = 0,padx=5)



                     
# DEFINIR BARRA DE MENÚ DE LA APLICACION DONDE IRAN MAS OPERACIONES(TRIGONOMETRICAS(HIPERBOLAS(FUNCIONES):
barramenu = Menu(ventanaprin)
ventanaprin['menu'] = barramenu

#CADA UNO DE LOS MENUS DE LA BARRA
menu1 = Menu(barramenu,activebackground="Gray80",bg="Gray22",bd="5",fg="white",activeforeground="black")
menu2 = Menu(barramenu,activebackground="Gray80",bg="Gray22",bd="5",fg="white",activeforeground="black")
menu3 = Menu(barramenu,activebackground="Gray80",bg="Gray22",bd="5",fg="white",activeforeground="black")

#COMO MOSTRARAN LAS OPCIONES QUE SERA EN FORMA DE CASCADA
barramenu.add_cascade(menu=menu1, label='Trigonometicas')
barramenu.add_cascade(menu=menu2, label='Hiperbolas')
barramenu.add_cascade(menu=menu3, label='Funciones')

#TRIGONOMETRICAS
menu1.add_command(label='Sin',command=lambda:calculadora.registraOperacion("sin"),underline=0)
menu1.add_command(label='Cos',command=lambda:calculadora.registraOperacion("cos"),underline=0)
menu1.add_command(label='Tan',command=lambda:calculadora.registraOperacion("tan"),underline=0,)
menu1.add_separator()  # Agrega un separador
menu1.add_command(label='Asin',command=lambda:calculadora.registraOperacion("asin"),underline=0)
menu1.add_command(label='Acos',command=lambda:calculadora.registraOperacion("acos"),underline=0)
menu1.add_command(label='Atan',command=lambda:calculadora.registraOperacion("atan"),underline=0)
menu1.add_separator()  # Agrega un separador
menu1.add_command(label='Hypo',command=lambda:calculadora.registraOperacion("hypo"),underline=0)


#HIPERBOLICAS
menu2.add_command(label='Sinh',command=lambda:calculadora.registraOperacion("sinh"),underline=0)
menu2.add_command(label='Cosh',command=lambda:calculadora.registraOperacion("cosh"),underline=0)
menu2.add_command(label='Tanh',command=lambda:calculadora.registraOperacion("tanh"),underline=0)
menu2.add_separator()  # Agrega un separador
menu2.add_command(label='Asinh',command=lambda:calculadora.registraOperacion("asinh"),underline=0)
menu2.add_command(label='Acosh',command=lambda:calculadora.registraOperacion("acosh"),underline=0)
menu2.add_command(label='Atanh',command=lambda:calculadora.registraOperacion("atanh"),underline=0)

#FUNCIONES
menu3.add_command(label='|x|',command=lambda:calculadora.registraOperacion("fabs"),underline=0)
menu3.add_separator()  # Agrega un separador
menu3.add_command(label='|_x_|',command=lambda:calculadora.registraOperacion("floor"),underline=0)
menu3.add_separator()  # Agrega un separador
menu3.add_command(label='[x]',command=lambda:calculadora.registraOperacion("ceil"),underline=0)

calculadora.actualizaDisplay()

#DEFINIR EL TAMAÑO Y COLOR DE LOS BOTONES
button_w=11
button_h=3
button_c=("gray11")
acti_bg=("white")
acti_fg=("black")
#DEFINIR EL COLOR DEL FONDO
button_text_c=("white")

#DEFINIR BOTONES
#Primera Fila
buttonX2=Button(marcoButton,text="x2",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:calculadora.registraOperacion('^2')).grid (row = 0, column = 0, padx = 5, pady = 5)#.place(x=17,y=125)
buttonPi=Button(marcoButton,text="π",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:calculadora.registraOperacion('pi')).grid (row = 0, column = 1, padx = 5, pady = 5)#.place(x=107,y=125)
buttonE=Button(marcoButton,text="e",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:calculadora.registraOperacion("e")).grid (row = 0, column = 2, padx = 5, pady = 5)#.place(x=197,y=125)
buttonC=Button(marcoButton,text="C",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:calculadora.limpiaCalculadora()).grid (row = 0, column = 3, padx = 5, pady = 5)#.place(x=287,y=125)
buttonDEL=Button(marcoButton,text="DEL",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:calculadora.BorrarNumero()).grid (row = 0, column = 4, padx = 5, pady = 5)#.place(x=377,y=125)

#Segunda Fila
buttonX3=Button(marcoButton,text="x3",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:calculadora.registraOperacion('^3')).grid (row = 1, column = 0, padx = 5, pady = 5)#.place(x=17,y=190)
button1x=Button(marcoButton,text="1/x",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:calculadora.registraOperacion('1/x')).grid (row = 1, column = 1, padx = 5, pady = 5)#.place(x=107,y=190)
buttonx=Button(marcoButton,text="Log2",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:calculadora.registraOperacion("Log2")).grid (row = 1, column = 2, padx = 5, pady = 5)#.place(x=197,y=190)
buttonEXP=Button(marcoButton,text="Exp",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:calculadora.registraOperacion("exp")).grid (row = 1, column = 3, padx = 5, pady = 5)#.place(x=287,y=190)
buttonTPC=Button(marcoButton,text="Mod",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:calculadora.registraOperacion('%')).grid (row = 1, column = 4, padx = 5, pady = 5)#.place(x=377,y=190)

#Tercera Fila
buttonxy=Button(marcoButton,text="x^y",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:calculadora.registraOperacion('x^y')).grid (row = 2, column = 0, padx = 5, pady = 5)#.place(x=17,y=255)
buttonPiz=Button(marcoButton,text="MCD",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:calculadora.registraOperacion("mcd")).grid (row = 2, column = 1, padx = 5, pady = 5)#.place(x=107,y=255)
buttonPde=Button(marcoButton,text="MCM",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:calculadora.registraOperacion("mcm")).grid (row = 2, column = 2, padx = 5, pady = 5)#.place(x=197,y=255)
buttonN=Button(marcoButton,text="n!",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:calculadora.registraOperacion("n!")).grid (row = 2, column = 3, padx = 5, pady = 5)#.place(x=287,y=255)
buttonDiv=Button(marcoButton,text="/",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:calculadora.registraOperacion('/')).grid (row = 2, column = 4, padx = 5, pady = 5)#.place(x=377,y=255)

#Cuarta Fila
button10=Button(marcoButton,text="10^x",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:calculadora.registraOperacion("10^x")).grid (row = 3, column = 0, padx = 5, pady = 5)#.place(x=17,y=320)
button7=Button(marcoButton,text="7",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:calculadora.pulsaBotonNumero(7)).grid (row = 3, column = 1, padx = 5, pady = 5)#.place(x=107,y=320)
button8=Button(marcoButton,text="8",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:calculadora.pulsaBotonNumero(8)).grid (row = 3, column = 2, padx = 5, pady = 5)#.place(x=197,y=320)
button9=Button(marcoButton,text="9",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:calculadora.pulsaBotonNumero(9)).grid (row = 3, column = 3, padx = 5, pady = 5)#.place(x=287,y=320)
buttonX=Button(marcoButton,text="X",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:calculadora.registraOperacion('*')).grid (row = 3, column = 4, padx = 5, pady = 5)#.place(x=377,y=320)

#Quinta Fila
buttonR2=Button(marcoButton,text="√",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:calculadora.registraOperacion("raiz")).grid (row = 4, column = 0, padx = 5, pady = 5)#.place(x=17,y=385)
button4=Button(marcoButton,text="4",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:calculadora.pulsaBotonNumero(4)).grid (row = 4, column = 1, padx = 5, pady = 5)#.place(x=107,y=385)
button5=Button(marcoButton,text="5",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:calculadora.pulsaBotonNumero(5)).grid (row = 4, column = 2, padx = 5, pady = 5)#.place(x=197,y=385)
button6=Button(marcoButton,text="6",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:calculadora.pulsaBotonNumero(6)).grid (row = 4, column = 3, padx = 5, pady = 5)#.place(x=287,y=385)
buttonMenos=Button(marcoButton,text="-",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:calculadora.registraOperacion('-')).grid (row = 4, column = 4, padx = 5, pady = 5)#.place(x=377,y=385)

#Sexta Fila
buttonx3=Button(marcoButton,text="√3",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:calculadora.registraOperacion('raiz3')).grid (row = 5, column = 0, padx = 5, pady = 5)#.place(x=17,y=450)
button1=Button(marcoButton,text="1",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:calculadora.pulsaBotonNumero(1)).grid (row = 5, column = 1, padx = 5, pady = 5)#.place(x=107,y=450)
button2=Button(marcoButton,text="2",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:calculadora.pulsaBotonNumero(2)).grid (row = 5, column = 2, padx = 5, pady = 5)#.place(x=197,y=450)
button3=Button(marcoButton,text="3",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:calculadora.pulsaBotonNumero(3)).grid (row = 5, column = 3, padx = 5, pady = 5)#.place(x=287,y=450)
buttonMas=Button(marcoButton,text="+",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:calculadora.registraOperacion('+')).grid (row =5, column = 4, padx = 5, pady = 5)#.place(x=377,y=450)

#Septima Fila
buttonLog=Button(marcoButton,text="Log10",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:calculadora.registraOperacion('log10')).grid (row = 6, column = 0, padx = 5, pady = 5)#.place(x=17,y=515)
buttonMasoMenos=Button(marcoButton,text="±",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:calculadora.registraOperacion("+-")).grid (row = 6, column = 1, padx = 5, pady = 5)#.place(x=107,y=515)
button0=Button(marcoButton,text="0",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:calculadora.pulsaBotonNumero(0)).grid (row = 6, column = 2, padx = 5, pady = 5)#.place(x=197,y=515)
buttonDeci=Button(marcoButton,text=".",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:calculadora.pulsaBotonDecimal()).grid (row = 6, column = 3, padx = 5, pady = 5)#.place(x=287,y=515)
buttonIgual=Button(marcoButton,text="=",width=button_w,height=button_h,bg=button_c,fg=button_text_c,activebackground=acti_bg,activeforeground=acti_fg,command=lambda:calculadora.ejecutaIgual()).grid (row = 6, column = 4, padx = 5, pady = 5)#.place(x=377,y=515)

#Idicamos que no pare de ejecutarse la ventana
ventanaprin.mainloop()
