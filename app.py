import interfaces as inter
import translate as tr
import tkinter as tk

def callback(text):
    root = tk.Tk()
    app = inter.TranslateFrame(master=root, text=text)
    app.mainloop()

handler = tr.EventClipboard(callback=callback)
handler.config()
handler.start()
