from kivy.app import App
from  kivy.uix.label import Label

class Basic(App):
    def build(self):
        label = Label(text="hello World")
        return  label
app = Basic()
app.run()