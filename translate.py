from googletrans import Translator
import keyboard
import clipboard

class EventClipboard:
    def __init__(self, callback=None):
        self.keyboard = keyboard
        self.clipboard = clipboard
        self.text = ''
        self.callback = callback

    def config(self, key='ctrl + c'):
        self.keyboard.add_hotkey(key, self.clipboard_callback)

    def clipboard_callback(self):
        self.text = self.clipboard.paste()
        self.callback(self.text)
    
    def start(self):
        self.keyboard.wait('esc')
    

class GoogleTranslator:    
    def __init__(self, target):
        self.target = target
        self.translator = Translator()
    def translate(self, text):
        return self.translator.translate(text, dest = self.target).text