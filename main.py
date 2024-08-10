from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.image import Image
import os  # To handle file paths

class MainApp(App):
    def build(self):
        self.file_path_label = Label(text='', size_hint=(None, None), size=(400, 50),
                                     pos_hint={'center_x': .5, 'center_y': .3})

        layout = FloatLayout()

        # Logo image
        logo = Image(source='logo.png', size_hint=(None, None), size=(200, 200),
                     pos_hint={'center_x': .5, 'center_y': .8})
        
        # Slogan with Unicode emoji
        slogan = Label(text='Encrypt 🔒 ⇔ Decrypt 🔓. Keep It Safe 🔥', font_size='16sp',
                       size_hint=(None, None), size=(400, 50),
                       pos_hint={'center_x': .5, 'center_y': .6}, font_name="seguiemj")
        
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
        
        # Bind the file chooser's on_submit event to update the file path label
        file_chooser.bind(on_submit=self.show_selected_file_path)

        # Create a popup with file chooser
        self.popup = Popup(title='Select a file', content=file_chooser, size_hint=(0.9, 0.9))
        self.popup.open()

    def show_selected_file_path(self, file_chooser, selected_files, *args):
        if selected_files:
            selected_file_path = selected_files[0]
            self.file_path_label.text = f'Selected File: {selected_file_path}'
            
            # Get the directory of the selected file and create a 'cipher' subfolder
            file_directory = os.path.dirname(selected_file_path)
            output_directory = os.path.join(file_directory, 'cipher')
            os.makedirs(output_directory, exist_ok=True)

            # Generate output file name inside the 'cipher' directory
            input_file_name = os.path.basename(selected_file_path)
            output_file_name = 'res_' + input_file_name
            output_file_path = os.path.join(output_directory, output_file_name)

            # Call the cipher function
            from utils import cipher
            cipher.toggle_bits(selected_file_path, output_file_path)

            # Show success popup with output file path
            self.show_success_popup(output_file_path)
            
            # Close the file chooser popup
            self.popup.dismiss()

    def show_success_popup(self, output_file_path):
        # Create a Label to show the output file path
        success_label = Label(
            text=f'Success! File saved at:\n{output_file_path}', 
            size_hint_y=None, 
            height=80,  # Adjusted height to look better
            text_size=(400, None),  # Make text wrap within the given width
            # halign='center',  # Center align the text
            valign='middle',  # Center align vertically
        )

        # Create a Popup to display the success message
        success_popup = Popup(
            title='Success',
            title_align='center',  # Center the title
            content=success_label,
            size_hint=(0.7, 0.2),  # Adjust the size of the popup
            auto_dismiss=True
        )
        
        # Open the success popup
        success_popup.open()

if __name__ == '__main__':
    app = MainApp()
    app.run()
