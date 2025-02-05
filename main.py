from customtkinter import CTkButton, CTk, CTkEntry
from tkinter import StringVar
import customtkinter as ctk
import math as m
from operator import neg

# Classe Botão
class Button(CTkButton):
    def __init__(self, master=None, text='', command=None, hover_color=None, fg_color=None):
        super().__init__(master=master, text=text, command=command)
        self.configure(width=40, height=50, corner_radius=20,
                       hover_color=hover_color if hover_color else cor4,
                       fg_color=fg_color if fg_color else cor2,
                       font=('Arial', 16),
                       text_color='black')
        self.grid(padx=3, pady=6, sticky='nsew')

# Função para adicionar numeros
def adicionar_ao_imput(num):
    global expresao
    expresao.set(expresao.get() + num)

# Função para calcular
def calcular():
    global expresao
    try:
        if (expresao == ''):
            return
        else:
            resultado = 0.0
            resultado = eval(expresao.get())
            expresao.set(str(resultado))
    except Exception as SyntaxError:
        expresao.set('')
        print('Entrada Invalida')   

# Função Tangente
def tan(num):
    global expresao
    if(num == ''):
        print('Entrada Invalida')
    else:
        resultado = m.tan(float(num))
        expresao.set(resultado)

# Função Seno
def sin(num):
    global expresao
    if(num == ''):
        print('Entrada Invalida')
    else:
        resultado = m.sin(float(num))
        expresao.set(resultado)

# Função Cosseno
def cos(num):
    global expresao
    if(num == ''):
        print('Entrada Invalida')
    else:
        resultado = m.cos(float(num))
        expresao.set(resultado)

# Função da Raiz Quadrada
def sqrt(num):
    global expresao
    try:
        if(float(num) < 0):
            print('Entrada Invalida')
            return
        else:
            raiz = (m.sqrt(float(num)))
            expresao.set(str(raiz))
    except Exception as ValueError:
        print('Entrada Invalida')

# Função Logaritmo Decimal
def log10(num):
    global expresao
    if(num == ''):
        print('Entrada Invalida')
    else:
        resultado = m.log10(float(num))
        expresao.set(resultado)

# Função Radianos
def rad(num):
    global expresao
    if(num == ''):
        print('Entrada Invalida')
    else:
        resultado = m.radians(float(num))
        expresao.set(resultado)

# Função do PI
def pi():
    global expresao
    expresao.set('3.14')

# Função de limpar a tela
def clear():
    global expresao
    expresao.set('')

# Função para deixar o numero negativo/positivo
def negative(num):
    global expresao
    tran = neg(int(num))
    expresao.set(str(tran))

# Cores

cor1 = "#363434"
cor2 = "#feffff"
cor3 = "#37474F"  
cor4 = '#f0ebf1'

# Criando app
app = CTk()
app.title("Calculadora")
app.geometry("366x550")
app.resizable(False, False)
app.configure(bg=cor1)
expresao = StringVar()

# Criando frames
frame_tela = ctk.CTkFrame(app, width=350, height=70, corner_radius=15)
frame_tela.grid(row=0, column=0, sticky='nsew', padx=8, pady=8)

frame_cientifica = ctk.CTkFrame(app, width=365, height=70)
frame_cientifica.grid(row=1, column=0, sticky='nsew', padx=8, pady=3)

frame_calculadora = ctk.CTkFrame(app, width=365, height=70)
frame_calculadora.grid(row=4, column=0, sticky='nsew', padx=8, pady=3)

# Configurando o frame tela
ltela = CTkEntry(frame_tela, width=350, height=20,textvariable=expresao, justify='right', font=('Arial', 18),  text_color=(cor2), fg_color=(cor3))
ltela.grid(row=0, column=1, columnspan=3, ipady=17, sticky='nsew')

# Configurando o frame cientifica
Button(frame_cientifica, text='tan', command= lambda : tan(expresao.get())).grid(row=1, column=0)
Button(frame_cientifica, text='sin', command= lambda : sin(expresao.get())).grid(row=1, column=1)
Button(frame_cientifica, text='cos', command= lambda : cos(expresao.get())).grid(row=1, column=2)
Button(frame_cientifica, text='sqrt', command= lambda : sqrt(expresao.get())).grid(row=1, column=3)

Button(frame_cientifica, text='log', command= lambda : log10(expresao.get())).grid(row=2, column=0)
Button(frame_cientifica, text='pow', command= lambda : adicionar_ao_imput('**')).grid(row=2, column=1)
Button(frame_cientifica, text='rad', command= lambda : rad(expresao.get())).grid(row=2, column=2)
Button(frame_cientifica, text='C', command=clear, hover_color='#f7696e').grid(row=2, column=3)

Button(frame_cientifica, text='pi', command=pi).grid(row=3, column=0)
Button(frame_cientifica, text='(', command= lambda : adicionar_ao_imput('(')).grid(row=3, column=1)
Button(frame_cientifica, text=')', command= lambda : adicionar_ao_imput(')')).grid(row=3, column=2)
Button(frame_cientifica, text='/', command= lambda : adicionar_ao_imput('/')).grid(row=3, column=3)

# Botões em formato padrão
frame_cientifica.grid_columnconfigure(0, weight=1, uniform="col")
frame_cientifica.grid_columnconfigure(1, weight=1, uniform="col")
frame_cientifica.grid_columnconfigure(2, weight=1, uniform="col")
frame_cientifica.grid_columnconfigure(3, weight=1, uniform="col")

# Configurando o frame calculadora
Button(frame_calculadora, text='7', command= lambda : adicionar_ao_imput('7')).grid(row=4, column=0)
Button(frame_calculadora, text='8', command= lambda : adicionar_ao_imput('8')).grid(row=4, column=1)
Button(frame_calculadora, text='9', command= lambda : adicionar_ao_imput('9')).grid(row=4, column=2)
Button(frame_calculadora, text='x', command= lambda : adicionar_ao_imput('*')).grid(row=4, column=3)

Button(frame_calculadora, text='4', command= lambda : adicionar_ao_imput('4')).grid(row=5, column=0)
Button(frame_calculadora, text='5', command= lambda : adicionar_ao_imput('5')).grid(row=5, column=1)
Button(frame_calculadora, text='6', command= lambda : adicionar_ao_imput('6')).grid(row=5, column=2)
Button(frame_calculadora, text='-', command= lambda : adicionar_ao_imput('-')).grid(row=5, column=3)

Button(frame_calculadora, text='1', command= lambda : adicionar_ao_imput('1')).grid(row=6, column=0)
Button(frame_calculadora, text='2', command= lambda : adicionar_ao_imput('2')).grid(row=6, column=1)
Button(frame_calculadora, text='3', command= lambda : adicionar_ao_imput('3')).grid(row=6, column=2)
Button(frame_calculadora, text='+', command= lambda : adicionar_ao_imput('+')).grid(row=6, column=3)

Button(frame_calculadora, text='+/-', command= lambda : negative(expresao.get())).grid(row=7, column=0)
Button(frame_calculadora, text='0', command= lambda : adicionar_ao_imput('0')).grid(row=7, column=1)
Button(frame_calculadora, text='.', command= lambda : adicionar_ao_imput('.')).grid(row=7, column=2)
Button(frame_calculadora, text='=', command=calcular, hover_color='#2699E6', fg_color='#33CCFF').grid(row=7, column=3)

# Botões em formato padrão
frame_calculadora.grid_columnconfigure(0, weight=1, uniform="col")
frame_calculadora.grid_columnconfigure(1, weight=1, uniform="col")
frame_calculadora.grid_columnconfigure(2, weight=1, uniform="col")
frame_calculadora.grid_columnconfigure(3, weight=1, uniform="col")

# Iniciar a aplicação
app.mainloop()