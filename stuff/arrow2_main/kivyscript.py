#colour values
#these are rgba values with a /255 on the first three digits
top_inputs_bg=(63/255,38/255,82/255,1)
buttons_bg=(126/255,125/255,127/255,1)
mainbox_bg=(49/255,0/255,87/255,1)
top_inputs_fg=(98/255,98/255,98/255,0.6)
mainbox_fg=(1,1,1,1)

import goat
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class main(GridLayout):
    def __init__(self, **kwargs):
        super(main, self).__init__(**kwargs)
        self.cols = 1

        self.top_grid = GridLayout()
        self.top_grid.cols = 4
        self.top_grid.size_hint_y=0.06


        self.directory = TextInput(multiline=False, font_size=16)
        self.directory.background_color=top_inputs_bg
        self.directory.foreground_color=top_inputs_fg
        self.top_grid.add_widget(self.directory)

        self.filename = TextInput(multiline=False, font_size=16)
        self.filename.background_color=top_inputs_bg
        self.filename.foreground_color=top_inputs_fg
        self.top_grid.add_widget(self.filename)

        self.savebutton = Button(text="Save", font_size=16, size_hint_x=None, width=80)
        self.savebutton.background_color=buttons_bg
        self.savebutton.bind(on_press=self.save)
        self.top_grid.add_widget(self.savebutton)

        self.openbutton = Button(text="Open", font_size=16, size_hint_x=None, width=80)
        self.openbutton.background_color=buttons_bg
        self.openbutton.bind(on_press=self.open)
        self.top_grid.add_widget(self.openbutton)

        self.add_widget(self.top_grid)

        self.mainbox = TextInput(size_hint_y=0.94, font_size=24, auto_indent=True)
        self.mainbox.background_color=mainbox_bg
        self.mainbox.foreground_color=mainbox_fg
        self.add_widget(self.mainbox)
    def save(self, instance):
        directory = self.directory.text
        filename = self.filename.text
        feed = self.mainbox.text
        location = directory+"/"+filename
        goat.quicksave(feed,location)
    def open(self, instance):
        directory = self.directory.text
        filename = self.filename.text
        feed = self.mainbox.text
        location = directory+"/"+filename
        self.mainbox.insert_text(goat.loadfile(location))

class Arrow2(App):
    def build(self):
        return main()

if __name__ == "__main__":
    Arrow2().run()
