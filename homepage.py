from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import Image, ImageTk

def homepage_window(window):
    """
    Esta função cria a janela da homepage \n
    É constituida pela barra de navegação e pela página principal \n
    A barra de navegação têm o logo da app, uma barra de pesquisa, icones da dashboard, de notifições e do perfil do utilizador
    """
    #Para criar a barra de navegação e a homepage
    nav_bar = Frame(window, width = 1000, height = 60, bg = '#333333').place(x = 0, y = 0)
    homepage = Frame(window, width = 1000, height = 1000, bg = 'lightgrey').place(x = 0, y = 150)

    #----WIDGETS DA BARRA DE NAVEGAÇÃO--------
    myPhotos_logo = Label(nav_bar, text = 'myPhotos', fg = 'white', bg = '#333333', font =('Roboto', 28)).place(x = 0, y = 5)

    #Icone da lupa (FONTE - SITE FLATICON)
    icon = Image.open('..\\Projeto_AED\\images\\icons\\search_icon.png').resize((27,27))
    icon = ImageTk.PhotoImage(icon)
    search_icon = Button(image = icon, bg = '#333333', bd = 0)
    search_icon.image = icon
    search_icon.place( x = 185, y = 15)

    #Barra de pesquisa
    search = Entry(nav_bar, bg = '#E0E0E0', bd = 0, font =('Roboto', 14), width = 15).place(x = 220, y = 15)

    #Icone do perfil (FONTE - SITE FLATICON)
    icon2 = Image.open('..\\Projeto_AED\\images\\icons\\profile_icon.jpg').resize((50,50))
    icon2 = ImageTk.PhotoImage(icon2)
    profile_icon = Button(image = icon2, bd = 0, bg='#333333')
    profile_icon.image = icon2
    profile_icon.place( x = 940, y = 5)

    #Icone do sino da notificação (FONTE - SITE FLATICON)
    icon3 = Image.open('..\\Projeto_AED\\images\\icons\\bell_icon.png').resize((50,50))
    icon3 = ImageTk.PhotoImage(icon3)
    bell_icon = Button(image = icon3, bd = 0, bg='#333333')
    bell_icon.image = icon3
    bell_icon.place(x = 870, y = 5)

    #Icone da dashboard (FONTE - SITE FLATICON)
    #Janela com várias estatísticas do utilizador
    icon4 = Image.open('..\\Projeto_AED\\images\\icons\\dashboard_icon.png').resize((50,50))
    icon4 = ImageTk.PhotoImage(icon4)
    dashboard_icon = Button(image = icon4, bd = 0, bg = '#333333')
    dashboard_icon.image = icon4
    dashboard_icon.place(x = 800, y = 5)

    #----- WIDGETS PARA A HOMEPAGE
    activity_list = ['All Posts','Followers Only','Popular']
    activity_select = Combobox(homepage, values = activity_list, width = 15, font = ('Roboto', 18)).place(x = 30, y = 100)

    #Icone para selecionar um tipo de grid (FONTE - SITE FLATICON)
    icon5 = Image.open('..\\Projeto_AED\\images\\icons\\grid_icon1.png').resize((40,40))
    icon5 = ImageTk.PhotoImage(icon5)
    grid_icon1 = Button(image = icon5, bd = 0, bg = 'lightgrey')
    grid_icon1.image = icon5
    grid_icon1.place(x = 600, y = 100)

    #Icone para selecionar um 2º tipo de grid (FONTE - SITE FLATICON)
    icon6 = Image.open('..\\Projeto_AED\\images\\icons\\grid_icon2.png').resize((40,40))
    icon6 = ImageTk.PhotoImage(icon6)
    grid_icon2 = Button(image = icon6, bd = 0, bg = 'lightgrey')
    grid_icon2.image = icon6
    grid_icon2.place(x = 660, y = 100)

    #Icone para selecionar um 3º tipo de grid (FONTE - SITE FLATICON)
    icon7 = Image.open('..\\Projeto_AED\\images\\icons\\grid_icon3.png').resize((40,40))
    icon7 = ImageTk.PhotoImage(icon7)
    grid_icon3 = Button(image = icon7, bd = 0, bg = 'lightgrey')
    grid_icon3.image = icon7
    grid_icon3.place(x = 720, y = 100)

    #Botão para adicionar um post
    add_post_btn = Button(homepage, text = '+  Add Post', width = 12, height = 1, bg = '#28942a', fg = 'white', font = ('Roboto', 20), bd = 0).place(x = 800, y = 70)