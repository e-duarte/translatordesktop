from tkinter import scrolledtext
import tkinter as tk
import translate as tr
import time

class TranslateFrame(tk.Frame):
    def __init__(self, master=None, text=''):
        super().__init__(master)
        self.master = master
        self.master.geometry('200x50-1-1')
        self.master.title("Translate")
        self.gtranslator = tr.GoogleTranslator('pt')
        self.pack()
        self.create_widgets()
        self.text = text
        # self.master.wm_overrideredirect(True)
        
    def create_widgets(self):
        self.trans_bnt = tk.Button(self)
        self.trans_bnt["text"] = "Translate"
        self.trans_bnt["bg"] = "blue"
        self.trans_bnt["fg"] = "white"
        self.trans_bnt["width"] = "200"
        self.trans_bnt["height"] = "50"
        self.trans_bnt["command"] = self.translate
        self.trans_bnt.pack(side="top")

    def translate(self):
        text = self.gtranslator.translate(self.text)
        self.translateFrame = TranslatedFrame(master=tk.Tk())
        self.translateFrame.insert_text(text.lower())
        self.master.destroy()
    
    def show(self):
        self.master.deiconify()

    def hide(self):
        self.master.withdraw()

class TranslatedFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Translated")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.text_area = scrolledtext.ScrolledText(self)
        self.text_area.pack()

    def insert_text(self, text):
        self.text_area.insert("end", text)
        self.text_area.config(state=tk.DISABLED)
