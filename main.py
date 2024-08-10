from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserIconView

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # App name and slogan
        header = BoxLayout(orientation='vertical', size_hint_y=None, height=100)
        app_name = Label(text='Cryptify', font_size='32sp', bold=True, size_hint_y=None, height=50)
        slogan = Label(text='Encrypt. Decrypt. Keep It Safe.', font_size='16sp', size_hint_y=None, height=50)
        header.add_widget(app_name)
        header.add_widget(slogan)
        
        # File chooser button
        file_button = Button(text='Select File', size_hint_y=None, height=50)
        file_button.bind(on_press=self.select_file)

        layout.add_widget(header)
        layout.add_widget(file_button)
        
        return layout

    def select_file(self, instance):
        file_chooser = FileChooserIconView()
        popup = Popup(title='Select a file', content=file_chooser, size_hint=(0.9, 0.9))
        popup.open()

if __name__ == '__main__':
    app = MainApp()
    app.run()
