#Calculadora - Começo dia 16/03/2023
#Pausa dia 19/03/2023
#Arthur Gabriel Silva Martins
from tkinter import ttk
from tkinter import *
import Funcoes
#Funcoes.menu.menu()

#Cores
cor1 = "#1e1f1e"
cor2 = "#feffff"
cor3 = "#38576b" 
cor4 = "#eceff1" #Números
cor5 = "#ffab40" #Expressões

#Configurações da Tela(Frames)

janela = Tk()
janela.title("Calculadora")
janela.geometry("322x555")
janela.config(bg = cor1)

frame_tela = Frame(janela, width=322,height=70,bg= cor3)
frame_tela.grid(row = 0, column=0)

frame_corpo = Frame(janela, width=322,height=505)
frame_corpo.grid(row = 1, column=0)

############################################

todos_valores = ''

#####################################
def entrar_valores(event):

    global todos_valores

    todos_valores = todos_valores + str( event)
    

    #passando valor pra tela
    valor_texto.set(todos_valores)

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado))

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("0") 


#Criando Label
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto,width=19,height=3,padx=8,relief=FLAT,anchor="e",justify=RIGHT,font=('Ivy 21 '),bg=cor3)
app_label.place(x=0, y =0)



#Criando Botões

b1 = Button(frame_corpo,command= lambda: entrar_valores('3,1415926535897932384626433832795'), text="π", width = 7, height = 3, bg = cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
b1.place(x=80, y=0)

b2 = Button(frame_corpo,command= limpar_tela, text="C", width = 7, height = 3, bg = cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
b2.place(x=0, y=0)

b3 = Button(frame_corpo, command= lambda: entrar_valores('**2'), text="x²", width = 7, height = 3, bg = cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE  )
b3.place(x=161, y=0)

b4 = Button(frame_corpo,command= lambda: entrar_valores ('1/x'), text="1/x", width = 7, height = 3, bg = cor5,fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE  ) ####
b4.place(x=242, y=0)
##############################################
b5 = Button(frame_corpo,command= lambda: entrar_valores('**0.5'), text="√", width = 7, height = 3, bg = cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE  )
b5.place(x=0, y=70)

b6 = Button(frame_corpo,command= lambda: entrar_valores('!'), text="n!", width = 7, height = 3, bg = cor5, fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE  ) ###
b6.place(x=80, y=70)

b7 = Button(frame_corpo,command= lambda: entrar_valores('10**'), text="10^x", width = 7, height = 3, bg = cor5, fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE  )
b7.place(x=161, y=70)

b8 = Button(frame_corpo,command= lambda: entrar_valores('x^n'), text="x^n", width = 7, height = 3, bg = cor5,fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE  ) ####
b8.place(x=242, y=70)
###############################################
b9 = Button(frame_corpo,command= lambda: entrar_valores('7'), text="7", width = 7, height = 3, bg = cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE  )
b9.place(x=0, y=140)

b10 = Button(frame_corpo,command= lambda: entrar_valores('8'), text="8", width = 7, height = 3, bg = cor4,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE  )
b10.place(x=80, y=140)

b11 = Button(frame_corpo,command= lambda: entrar_valores('9'), text="9", width = 7, height = 3, bg = cor4,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE  )
b11.place(x=161, y=140)

b12 = Button(frame_corpo,command= lambda: entrar_valores('+'), text="+", width = 7, height = 3, bg = cor5,fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE  )
b12.place(x=242, y=140)
##############################################
b13 = Button(frame_corpo,command= lambda: entrar_valores('4'), text="4", width = 7, height = 3, bg = cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE  )
b13.place(x=0, y=210)

b14 = Button(frame_corpo,command= lambda: entrar_valores('5'), text="5", width = 7, height = 3, bg = cor4,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE  )
b14.place(x=80, y=210)

b15 = Button(frame_corpo,command= lambda: entrar_valores('6'), text="6", width = 7, height = 3, bg = cor4,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE  )
b15.place(x=161, y=210)

b16 = Button(frame_corpo,command= lambda: entrar_valores('-'), text="-", width = 7, height = 3, bg = cor5,fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE  )
b16.place(x=242, y=210)
###################################################
b17 = Button(frame_corpo,command= lambda: entrar_valores('1'), text="1", width = 7, height = 3, bg = cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
b17.place(x=0, y=280)

b18 = Button(frame_corpo,command= lambda: entrar_valores('2'), text="2", width = 7, height = 3, bg = cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE  )
b18.place(x=80, y=280)

b19 = Button(frame_corpo,command= lambda: entrar_valores('3'), text="3", width = 7, height = 3, bg = cor4,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE  )
b19.place(x=161, y=280)

b20 = Button(frame_corpo,command= lambda: entrar_valores('*'), text="x", width = 7, height = 3, bg = cor5,fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE  )
b20.place(x=242, y=280)

#####################################################
b19 = Button(frame_corpo,command= lambda: entrar_valores('ln'), text="ln", width = 7, height = 3, bg = cor5,fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE  ) ######
b19.place(x=0, y=350)

b20 = Button(frame_corpo,command= lambda: entrar_valores('0'), text="0", width = 7, height = 3, bg = cor4,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE  )
b20.place(x=80, y=350)

b21 = Button(frame_corpo,command= lambda: entrar_valores('+/-'), text="+/-", width = 7, height = 3, bg = cor5,fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE  ) ######
b21.place(x=161, y=350)

b22 = Button(frame_corpo,command= lambda: entrar_valores('/'), text="÷", width = 7, height = 3, bg = cor5,fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE  )
b22.place(x=242, y=350)
#########################################################

b19 = Button(frame_corpo,command= lambda: entrar_valores('log'), text="log", width = 7, height = 3, bg = cor5,fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE  ) #########
b19.place(x=0, y=420)

b20 = Button(frame_corpo,command= lambda: entrar_valores('.'), text=",", width = 7, height = 3, bg = cor5,fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE  )
b20.place(x=80, y=420)

b21 = Button(frame_corpo,command= calcular, text="=", width = 15, height = 3, bg = cor5,fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE  )
b21.place(x=161, y=420)


janela.mainloop() #Para manter a janela aberta