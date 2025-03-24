import sys
import os
import customtkinter as ctk
from PIL import Image
import db
from tkinter import messagebox

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import *
from App import app


class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
        self.title('SnapTag')
        self.resizable(False, False)

        self.user_var = ctk.StringVar()
        self.password_var = ctk.StringVar()
        self.bind('<Return>', self.confirm_login)

        self.image = ctk.CTkImage(light_image=Image.open(BACKGROUND_IMAGE), size=(WINDOW_WIDTH + 60, WINDOW_HEIGHT + 60))
        self.label = ctk.CTkLabel(self, image=self.image, text='')
        self.label.place(x=0, y=0, relwidth=1, relheight=1)

        User(self, self.user_var, self.confirm_login)
        Password(self, self.password_var)
        Button(self, self.confirm_login)

        self.mainloop()


    def confirm_login(self, event=None):
        users = db.get_usuarios()

        for user in users:
            if self.user_var.get() in user and self.password_var.get() in user:
                self.user_var.set('')
                self.password_var.set('')
                self.destroy()
                return app.Home()
            else:
                self.user_var.set('')
                self.password_var.set('')
                return messagebox.showerror(title='Erro', message='Usuário ou senha incorreto!')

class User(ctk.CTkEntry):

    def __init__(self, parent, user_var, command):
        super().__init__(master=parent,
                         textvariable=user_var,
                         fg_color=ENTRY_COLOR,
                         bg_color=ENTRY_COLOR,
                         border_color=ENTRY_COLOR,
                         text_color=BLACK
                         )

        user_label = ctk.CTkLabel(parent,
                                  text='Usuário',
                                  fg_color=WHITE,
                                  bg_color=WHITE,
                                  text_color=BLACK)
        user_label.place(relx=0.05, rely=0.35)

    
        self.place(relx=0.05, rely=0.43)


class Password(ctk.CTkEntry):

    def __init__(self, parent, password_var):
        super().__init__(master=parent,
                         fg_color=ENTRY_COLOR,
                         bg_color=ENTRY_COLOR,
                         border_color=ENTRY_COLOR,
                         text_color=BLACK,
                         textvariable=password_var,
                         show='*')

        password_label = ctk.CTkLabel(parent,
                                      text='Senha',
                                      fg_color=WHITE,
                                      bg_color=WHITE,
                                      text_color=BLACK
                                      )
        password_label.place(relx=0.05, rely=0.55)

        self.place(relx=0.05, rely=0.63)


class Button(ctk.CTkButton):

    def __init__(self, parent, command):
        super().__init__(master=parent,
                         bg_color=WHITE,
                         fg_color=WHITE,
                         text='',
                         width=75,
                         height=35,
                         hover=False,
                         image=ctk.CTkImage(Image.open((BACKGROUND_BUTTON_IMAGE)), size=(80, 35)),
                         command=command
                         )
        self.bind('<Enter>',  self.hover_image)
        self.bind('<Leave>', self.leave_image)
        self.place(relx=0.2, rely=0.75)
    
    def hover_image(self, event):
        self.configure(image=ctk.CTkImage(Image.open(BACKGROUND_BUTTON_HOLD_IMAGE), size=(80, 35)))
    
    def leave_image(self, event):
        self.configure(image=ctk.CTkImage(Image.open(BACKGROUND_BUTTON_IMAGE), size=(80, 35)))


if __name__ == '__main__':
    App()