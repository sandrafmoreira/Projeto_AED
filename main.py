from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from pathlib import Path #pathlib is a module in the Python standard library that provides an object-oriented interface for working with filesystem paths. The Path class in pathlib represents a filesystem path and comes with various methods for file and directory manipulation.
from users import * #Para importar as classes do ficheiro users.py para poder importar todas as suas funções

# ------------PÁGINA INICIAL--------------------------
class App():
    def __init__(self, window):
        """
        Permite criar uma window que é um objeto da classe App
        """
        self.window = window

#       Criar o Frame da página incial com uma imagem de fundo
        self.main_frame = Frame(self.window, width = 1000, height = 600, bg = '#333')
        self.main_frame.place(x = 0, y = 0)

#       Mensagem de bem-vindo
        self.welcome_message_label = Label(self.window, text = 'myPhotos.', width=16, height=3, bg = '#fff', font = ('Roboto', 80), fg = 'lightblue').place(x = 0, y = 0)

#       Botão para passar para o frame para fazer login!
        self.login_button = Button(self.window, text = 'Login',bg = '#ccc', width=17, height=3, fg = '#333', font = ('Roboto', 16), command = self.go_to_login).place(x = 65, y = 435)

#       Botão para passar para o frame para criar uma conta!
        self.sign_up_button = Button(self.window, text = 'Sign Up',bg = '#ccc', width=17, height=3, fg = '#333', font = ('Roboto', 16), command = self.go_to_sign_up).place(x = 325, y = 435)

#       Botão com um icon para o utilizador sair da app

        icon = Image.open('..\\Projeto_AED\\images\\icons\\logout_icon.png').resize((60,60))

        icon = Image.open(Path('')/ 'Projeto_AED'/ 'images'/ 'icons' / 'logout_icon.png').resize((80,80)) # platfmor independet

        icon = ImageTk.PhotoImage(icon)
        self.leave_app_btn = Button(self.window, image = icon, bd = 0, bg='#333333', command = self.leave_app)
        self.leave_app_btn.image = icon
        self.leave_app_btn.place( x = 800, y = 445)

    def go_to_sign_up(self):
        """
        Esta função leva o utilizador á página para criar uma conta
        """
        Sign_Up(self.window)

    def go_to_login(self):
        """
        Esta função leva o utilizador á página para fazer login e acessar a app
        """
        Login(self.window)

    def leave_app(self):
        """
        Esta função pergunta ao utilizador se deseja sair da app 
        """
        answer = messagebox.askquestion('Leave the App', 'Do you wish to leave the app?')    
        if answer == 'yes':
           exit()

        
#--------CONFIGURAÇÕES DE JANELA------------------------------------
window = Tk() #Chama a função Tkinter e cria uma janela
window.geometry('1000x600+100-100') #Altera largura e altura da janela e posiciona a janela +/- no centro do ecrã
window.title('myPhotos')
window.resizable(0,0) #Para não se poder redimensionar a janela (para os widgets não saírem do sítio)
window.configure(bg = 'lightgrey')

# # --- Criar uma window centrada no screen -----------------------------
# # Obter as dimensões do meu screen (em pixeis)
# screenWidth = window.winfo_screenwidth()
# screenHeight = window.winfo_screenheight()

# appwidth = 1000
# appHeight = 600
# x = (screenWidth/2) - (appwidth/2)
# y= (screenHeight/2) - (appHeight/2)
# window.geometry(f'{appwidth}x{appHeight}+{int(x)}+{int(y)}')



App(window)

window.mainloop()
