import customtkinter as ctk
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import *

class Home(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("SnapTag")
        self.geometry('600x400')


        self.mainloop()
