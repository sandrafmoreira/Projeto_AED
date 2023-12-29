from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from users import create_sign_up_frame,create_login_frame #Para importar as funções do ficheiro users.py

#--------CONFIGURAÇÕES DE JANELA------------------------------------
window = Tk() #Chama a função Tkinter e cria uma janela
window.geometry('1000x600') #Altera largura e altura da janela
window.title('myPhotos')
window.resizable(0,0) #Paara não se poder redimensionar a janela (para os widgets não saírem do sítio)
window.configure(bg = 'lightgrey')


# ------------PÁGINA INICIAL--------------------------

#Frame da janela inicial
main_frame = Frame(window, width = 1000, height = 600, bg = '#333')
main_frame.place(x = 0, y = 0) #Estao em duas linhas separadas, pois dá erro ao chamar as funções :/


#Mensagem de bem-vinda
welcome_message_label = Label(main_frame, text = 'Welcome to \nmyPhotos!', font = ('Roboto', 55), bg = '#333', fg = 'white').place(x = 300, y = 150)


#Botão para passar para o frame para criar uma conta!
sign_up_button = Button(main_frame, text = 'Sign Up', bg = '#333', border = '0', fg = 'white', font = ('Roboto', 25), command = lambda: create_sign_up_frame(window, main_frame)).place(x = 300, y = 350)


#Botão para passar para o frame para fazer login!
login_button = Button(main_frame, text = 'Login', bg = '#333', border = '0', fg = 'white', font = ('Roboto', 25), command = lambda: create_login_frame(window, main_frame)).place(x = 550, y = 350)


#--------------------

window.mainloop()

#RASCUNHOS!!

#Diretoria da imagem
# image = Image.open('')

# main_background_image = ImageTk.PhotoImage(image, width = 950, height = 550)
# label_image = Label(main_frame, image = main_background_image).place(x = 0, y = 0) #Para inserir a imagem com .place()


# frame_login= Frame(window, width=1000, height=600, bg='#333')
# frame_login.pack()

# lbl_title= Label(frame_login, text='MyFotos', bg='#333', fg='lightblue', font=('Roboto', 70)).pack(padx='40',pady='40')

# list_credentials = [ ['sandra', '123'], ['nuno', '456'], ['ken', '789'] ]

# app_admin_frame = None
# app_user_frame = None

# def login():
#     global app_admin_frame
#     global app_user_frame
#     global admin
#     global user
#     username = username_entry.get()
#     password = password_entry.get()
#     for i in list_credentials:
#         if i[0] == username and i[1] == password:
#             lbl_status['text'] ='Login successful'
#             frame_login.pack_forget() #para esconder a frame login sem a destruir, para ela aparecer outra vez temos que usar .pack()    
#             if (username=='sandra' and password=='123') or (username=='nuno' and password=='456') or (username=='ken' and password=='789'):
#                 admin = True
#                 app_admin_frame = Frame(window, width=400, height=300, bg='pink') #criar uma frame para admins
#                 app_admin_frame.pack()
#             else:
#                 user= True
#                 app_user_frame = Frame(window, width=400, height=300, bg='purple') #criar uma frame para users normais
#                 app_user_frame.pack()
#             return
#         else:
#             lbl_status['text'] ='Invalid credentials'

# def signup():
#     username = username_entry.get()
#     password = password_entry.get()
#     for i in list_credentials:
#         if i[0] == username:
#             lbl_status['text'] = 'Account already exists'
#             return
#     list_credentials.append([username, password])
#     lbl_status['text'] ='Registration successful'

# username_lbl =Label(frame_login, text='Username', bg='#333', fg='white', font=('Roboto', 12)).pack(padx='10',pady='10')
# username_entry =Entry(frame_login, bg='#333', fg='white', font=('Roboto', 12))
# username_entry.pack(padx=10,pady=10)
# password_lbl =Label(frame_login, text='Password', bg='#333', fg='white', font=('Roboto', 12)).pack(padx='10',pady='10')
# password_entry =Entry(frame_login, show='*', bg='#333', fg='white', font=('Roboto', 12))
# password_entry.pack(padx=10,pady=10)

# lbl_status=Label(frame_login, background='#333', fg='#fff', font=('Roboto', 10), text='')
# lbl_status.pack()

# btn_login =Button(frame_login, text='LOGIN', width=15, height=2, bg='lightblue', fg='#333', font=('Roboto', 10), command=login).pack(padx='15',pady='15')
# btn_signup =Button(frame_login, text='SIGNUP', width=15, height=2, bg='lightblue', fg='#333', font=('Roboto', 10), command=signup).pack(padx='10',pady='10')

