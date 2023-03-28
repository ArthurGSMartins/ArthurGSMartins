#Projeto começado dia 20/03/2023
#Projeto Finalizado dia 22/03/2023
#Arthur Gabriel Silva Martins

import tkinter
from tkinter import *
from tkinter import ttk

#cores

cor0 = '#FFFFFF'
cor1 = '#333333'
cor2 = '#FCC058'
cor3 = '#38576B'
cor4 = '#3297A8'
cor5 = '#FFF873'
cor6 = '#FCC058'
cor7 = '#E85151'
cor8 = cor4
cor10 = '#FCFBF7'
fundo = '#3B3B3B'

#Janela principal
janela = Tk()
janela.title('Jogo da Velha')
janela.geometry('260x370')
janela.configure(bg=fundo)
 
###################################################################################### Separando os frames
frame_cima = Frame(janela, width=240, height=100, bg=cor1,pady=0,padx=0,relief=RAISED)
frame_cima.grid(row=1, column = 0, sticky = NW, padx = 10, pady= 10)

frame_baixo = Frame(janela, width=240, height=300, bg=fundo,pady=0,padx=0,relief=FLAT)
frame_baixo.grid(row=2, column = 0, sticky = NW)

########################################################################################### 

app_x = Label(frame_cima, text='X', height=1, relief=FLAT,anchor=CENTER,font=('Ivy 40 bold'),bg = cor1, fg = cor7)
app_x.place(x=25, y =10)

app_x = Label(frame_cima, text='Jogador 1', height=1, relief=FLAT,anchor=CENTER,font=('Ivy 7 bold'),bg = cor1, fg = cor0)
app_x.place(x=17, y =70)

app_x_pontos = Label(frame_cima, text='0', height=1, relief=FLAT,anchor=CENTER,font=('Ivy 30 bold'),bg = cor1, fg = cor0)
app_x_pontos.place(x=80, y =20)

##############################################################

app_separador = Label(frame_cima, text=':', height=1, relief=FLAT,anchor=CENTER,font=('Ivy 30 bold'),bg = cor1, fg = cor0)
app_separador.place(x=110, y =15)

##############################################################
app_o = Label(frame_cima, text='O', height=1, relief=FLAT,anchor=CENTER,font=('Ivy 40 bold'),bg = cor1, fg = cor4)
app_o.place(x=170, y =10)

app_o = Label(frame_cima, text='Jogador 2', height=1, relief=FLAT,anchor=CENTER,font=('Ivy 7 bold'),bg = cor1, fg = cor0)
app_o.place(x=165, y =70)

app_o_pontos = Label(frame_cima, text='0', height=1, relief=FLAT,anchor=CENTER,font=('Ivy 30 bold'),bg = cor1, fg = cor0)
app_o_pontos.place(x=130, y =20)

#############################################################################################

jogador_1 = 'X'
jogador_2 = 'O'

score_1 = 0
score_2 = 0

tabela = [['1','2','3'],['4','5','6'],['7','8','9']]

jogando = 'X'
joga = ''
contador = 0
contador_de_rodadas = 0

def iniciar():
    buttonjogar.place(x=800, y =1900)
    def controle(i):
        global jogando
        global contador
        global jogar

        if i == str(1):
            
            if button0['text'] == '':

                if jogando == 'X':
                    cor = cor7
                if jogando == 'O':
                    cor = cor8

                
                button0['fg'] = cor
                button0['text'] = jogando
                tabela[0][0] = jogando

                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                
                contador+=1
        
        if i == str(2):
            if button1['text'] == '':

                if jogando == 'X':
                    cor = cor7
                if jogando == 'O':
                    cor = cor8

                
                button1['fg'] = cor
                button1['text'] = jogando
                tabela[0][1] = jogando

                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                
                contador+=1

        if i == str(3):
            if button2['text'] == '':

                if jogando == 'X':
                    cor = cor7
                if jogando == 'O':
                    cor = cor8

                
                button2['fg'] = cor
                button2['text'] = jogando
                tabela[0][2] = jogando

                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                
                contador+=1

        if i == str(4):
            if button3['text'] == '':

                if jogando == 'X':
                    cor = cor7
                if jogando == 'O':
                    cor = cor8

                
                button3['fg'] = cor
                button3['text'] = jogando
                tabela[1][0] = jogando

                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                
                contador+=1

        if i == str(5):
            if button4['text'] == '':

                if jogando == 'X':
                    cor = cor7
                if jogando == 'O':
                    cor = cor8

                
                button4['fg'] = cor
                button4['text'] = jogando
                tabela[1][1] = jogando

                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                
                contador+=1

        if i == str(6):
            if button5['text'] == '':

                if jogando == 'X':
                    cor = cor7
                if jogando == 'O':
                    cor = cor8

                
                button5['fg'] = cor
                button5['text'] = jogando
                tabela[1][2] = jogando

                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                
                contador+=1

        if i == str(7):
            if button6['text'] == '':

                if jogando == 'X':
                    cor = cor7
                if jogando == 'O':
                    cor = cor8

                
                button6['fg'] = cor
                button6['text'] = jogando
                tabela[2][0] = jogando

                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                
                contador+=1

        if i == str(8):
            if button7['text'] == '':

                if jogando == 'X':
                    cor = cor7
                if jogando == 'O':
                    cor = cor8

                
                button7['fg'] = cor
                button7['text'] = jogando
                tabela[2][1] = jogando

                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                
                contador+=1

        if i == str(9):
            if button8['text'] == '':

                if jogando == 'X':
                    cor = cor7
                if jogando == 'O':
                    cor = cor8

                
                button8['fg'] = cor
                button8['text'] = jogando
                tabela[2][2] = jogando

                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                
                contador+=1

        if contador >= 5: 
            if tabela[0][0] == tabela[0][1] == tabela [0][2]!="":
                vencedor(jogando)
            elif tabela[1][0] == tabela[1][1] == tabela [1][2]!="":
                vencedor(jogando)
            elif tabela[2][0] == tabela[2][1] == tabela [2][2]!="":
                vencedor(jogando)

            if tabela[0][0] == tabela[1][0] == tabela [2][0]!="":
                vencedor(jogando)
            elif tabela[0][1] == tabela[1][1] == tabela [2][1]!="":
                vencedor(jogando)
            elif tabela[0][2] == tabela[1][2] == tabela [2][2]!="":
                vencedor(jogando)

            if tabela[0][0] == tabela[1][1] == tabela [2][2]!="":
                vencedor(jogando)
            elif tabela[0][2] == tabela[1][1] == tabela [2][0]!="":
                vencedor(jogando)
                    
            if contador >= 9:
                vencedor('Velha')

    def vencedor(i):
        global tabela
        global score_1
        global score_2
        global contador_de_rodadas
        global contador

        button0['state'] = 'disable'
        button1['state'] = 'disable'
        button2['state'] = 'disable'
        button3['state'] = 'disable'
        button4['state'] = 'disable'
        button5['state'] = 'disable'
        button6['state'] = 'disable'
        button7['state'] = 'disable'
        button8['state'] = 'disable'

        app_vencedor = Label(frame_baixo, text='', width=17, relief=FLAT,anchor=CENTER,font=('Ivy 13 bold'),bg = cor1, fg = cor2)
        app_vencedor.place(x=40, y =220)

        if i == 'X':
            score_2 +=1
            app_vencedor['text'] = 'Jogador 2 venceu'
            app_o_pontos['text'] = score_2
        
        if i == 'O':
            score_1 +=1
            app_vencedor['text'] = 'Jogador 1 venceu'
            app_x_pontos['text'] = score_1
        
        if i == 'Velha':
            app_vencedor['text'] = 'Velha'

        def start():
            button0['text'] = ''
            button1['text'] = ''
            button2['text'] = ''
            button3['text'] = ''
            button4['text'] = ''
            button5['text'] = ''
            button6['text'] = ''
            button7['text'] = ''
            button8['text'] = ''

            button0['state'] = 'normal'
            button1['state'] = 'normal'
            button2['state'] = 'normal'
            button3['state'] = 'normal'
            button4['state'] = 'normal'
            button5['state'] = 'normal'
            button6['state'] = 'normal'
            button7['state'] = 'normal'
            button8['state'] = 'normal'

            app_vencedor.destroy()
            buttonjogar.destroy()

        buttonjogar = Button(frame_baixo,command=start, text='Próxima Rodada', width=13,font=('Ivy 10 bold'),overrelief=RIDGE,relief=RAISED,bg = fundo, fg = cor0)
        buttonjogar.place(x=73, y =190)

        def game_over():
            buttonjogar.destroy()
            app_vencedor.destroy()
            terminar()
        
        if contador_de_rodadas >= 5:
            game_over()
        else:
            contador_de_rodadas +=1
            #Reiniciando a Tabela
            tabela = [['1','2','3'],['4','5','6'],['7','8','9']]
            contador = 0

    def terminar():
        global tabela
        global contador_de_rodadas
        global score_1
        global score_2
        global contador

        tabela = [['1','2','3'],['4','5','6'],['7','8','9']]
        contador_de_rodadas = 0
        score_1 = 0
        score_2 = 0
        contador = 0

        button0['state'] = 'disable'
        button1['state'] = 'disable'
        button2['state'] = 'disable'
        button3['state'] = 'disable'
        button4['state'] = 'disable'
        button5['state'] = 'disable'
        button6['state'] = 'disable'
        button7['state'] = 'disable'
        button8['state'] = 'disable'

        app_fim = Label(frame_baixo, text='Jogo Acabou', width=17, relief=FLAT,anchor=CENTER,font=('Ivy 13 bold'),bg = cor1, fg = cor2)
        app_fim.place(x=25, y =90)

        def jogar_de_novo():
            app_x_pontos ['text'] = '0'
            app_o_pontos ['text'] = '0'
            app_fim.destroy()
            buttonjogar.destroy()

            iniciar()

        buttonjogar = Button(frame_baixo,command=jogar_de_novo, text='Jogar De Novo',font=('Ivy 10 bold'),overrelief=RIDGE,relief=RAISED,bg = fundo, fg = cor0)
        buttonjogar.place(x=85, y =190)

    app_ = Label(frame_baixo, text='', height=21, relief=FLAT,pady=5,anchor=CENTER,font=('Ivy 5 bold'),bg = cor0, fg = cor7)
    app_.place(x=90, y =15)

    app_ = Label(frame_baixo, text='', height=21, relief=FLAT,pady=5,anchor=CENTER,font=('Ivy 5 bold'),bg = cor0, fg = cor7)
    app_.place(x=160, y =15)

    ############################################################################################

    app_ = Label(frame_baixo, text='', width=190, relief=FLAT,padx=2,pady=1,anchor=CENTER,font=('Ivy 1 bold'),bg = cor0, fg = cor7)
    app_.place(x=30, y =63)

    app_ = Label(frame_baixo, text='', width=190, relief=FLAT,padx=2, pady=1,anchor=CENTER,font=('Ivy 1 bold'),bg = cor0, fg = cor7)
    app_.place(x=30, y =123)
    ##############################################################

    button0 = Button(frame_baixo,command=lambda: controle('1'), text='', width=4,font=('Ivy 15 bold'),overrelief=RIDGE,relief=FLAT,bg = fundo, fg = cor7)
    button0.place(x=30, y = 15)

    button1 = Button(frame_baixo,command=lambda: controle('2'), text='', width=4,font=('Ivy 15 bold '),overrelief=RIDGE,relief=FLAT,bg = fundo, fg = cor7)
    button1.place(x=100, y = 15)

    button2 = Button(frame_baixo,command=lambda: controle('3'), text='', width=4,font=('Ivy 15 bold'),overrelief=RIDGE,relief=FLAT,bg = fundo, fg = cor7)
    button2.place(x=170, y = 15)

    button3 = Button(frame_baixo,command=lambda: controle('4'), text='', width=4,font=('Ivy 15 bold'),overrelief=RIDGE,relief=FLAT,bg = fundo, fg = cor7)
    button3.place(x=30, y = 75)

    button4 = Button(frame_baixo,command=lambda: controle('5'), text='', width=4,font=('Ivy 15 bold'),overrelief=RIDGE,relief=FLAT,bg = fundo, fg = cor7)
    button4.place(x=100, y = 75)

    button5 = Button(frame_baixo,command=lambda: controle('6'), text='', width=4,font=('Ivy 15 bold'),overrelief=RIDGE,relief=FLAT,bg = fundo, fg = cor7)
    button5.place(x=170, y =75)

    button6 = Button(frame_baixo,command=lambda: controle('7'), text='', width=4,font=('Ivy 15 bold'),overrelief=RIDGE,relief=FLAT,bg = fundo, fg = cor7)
    button6.place(x=30, y =135)

    button7 = Button(frame_baixo,command=lambda: controle('8'), text='', width=4,font=('Ivy 15 bold'),overrelief=RIDGE,relief=FLAT,bg = fundo, fg = cor7)
    button7.place(x=100, y =135)

    button8 = Button(frame_baixo,command=lambda: controle('9'), text='', width=4,font=('Ivy 15 bold'),overrelief=RIDGE,relief=FLAT,bg = fundo, fg = cor7)
    button8.place(x=170, y =135)

#########################################################################
buttonjogar = Button(frame_baixo,command=iniciar, text='Jogar', width=10,font=('Ivy 10 bold'),overrelief=RIDGE,relief=RAISED,bg = fundo, fg = cor0)
buttonjogar.place(x=85, y =190)

janela.mainloop()

#Arthur Gabriel Silva Martins
