from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout

class MainApp(App):
    def build(self):
        self.file_path_label = Label(text='', size_hint=(None, None), size=(400, 50),
                                     pos_hint={'center_x': .5, 'center_y': .3})

        layout = FloatLayout()

        # Logo image
        logo = Image(source='logo.png', size_hint=(None, None), size=(200, 200),
                     pos_hint={'center_x': .5, 'center_y': .8})
        
        # Slogan
        slogan = Label(text='Encrypt. Decrypt. Keep It Safe.', font_size='16sp',
                       size_hint=(None, None), size=(400, 50),
                       pos_hint={'center_x': .5, 'center_y': .6})
        
        # File chooser button
        file_button = Button(text='Select File', size_hint=(None, None),
                             size=(200, 50), pos_hint={'center_x': .5, 'center_y': .4})
        file_button.bind(on_press=self.select_file)

        # Adding widgets to layout
        layout.add_widget(logo)
        layout.add_widget(slogan)
        layout.add_widget(file_button)
        layout.add_widget(self.file_path_label)

        return layout

    def select_file(self, instance):
        file_chooser = FileChooserIconView()
        file_chooser.filters = ['*.txt', '*.jpg', '*.png', '*.pdf']  # Customize filters as needed
        
        # Create a popup with file chooser
        self.popup = Popup(title='Select a file', content=file_chooser, size_hint=(0.9, 0.9))
        self.popup.open()

if __name__ == '__main__':
    app = MainApp()
    app.run()
