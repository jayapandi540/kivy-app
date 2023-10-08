from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle

class CombinedChatApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        # Create the first screen
        first_screen = Screen(name='first_screen')
        first_screen.add_widget(self.create_combined_layout(first_screen))
        self.screen_manager.add_widget(first_screen)

        # Create the second screen
        second_screen = Screen(name='second_screen')
        second_screen.add_widget(self.create_combined_layout(second_screen))
        self.screen_manager.add_widget(second_screen)

        # Create the third screen
        third_screen = Screen(name='third_screen')
        third_screen.add_widget(self.create_combined_layout(third_screen))
        self.screen_manager.add_widget(third_screen)

        # Create the fourth screen
        fourth_screen = Screen(name='fourth_screen')
        fourth_screen.add_widget(self.create_combined_layout(fourth_screen))
        self.screen_manager.add_widget(fourth_screen)

        # Create the fifth screen
        fifth_screen = Screen(name='fifth_screen')
        fifth_screen.add_widget(self.create_combined_layout(fifth_screen))
        self.screen_manager.add_widget(fifth_screen)

        return self.screen_manager

    def create_combined_layout(self, current_screen):
        layout = BoxLayout(orientation='vertical', spacing=10)

        # Create a button to trigger the dropdown menu
        button = Button(text='Menu', size_hint=(None, None), size=(500, 50), halign='right')
        button.bind(on_release=self.show_dropdown)

        # Create a dropdown menu
        self.dropdown = DropDown()

        # Add buttons to the dropdown menu
        for option in ['Option 1', 'Option 2', 'Option 3', 'Option 4']:
            btn = Button(text=option, size_hint_y=None, height=30)
            btn.bind(on_release=lambda btn_option: self.select_option(btn_option.text, self.dropdown, current_screen))
            self.dropdown.add_widget(btn)

        layout.add_widget(button)

        # UI components for chat
        self.messages = []
        scroll_view = ScrollView()
        self.message_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.message_layout.bind(minimum_height=self.message_layout.setter('height'))
        scroll_view.add_widget(self.message_layout)

        input_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        self.input_field = TextInput(multiline=False, size_hint=(0.7, 1))
        send_button = Button(text='Send', size_hint=(0.3, 1), on_press=self.send_message)

        input_layout.add_widget(self.input_field)
        input_layout.add_widget(send_button)

        layout.add_widget(scroll_view)
        layout.add_widget(input_layout)

        # Create a back button
        back_button = Button(text='Back', size_hint=(None, None), size=(500, 50), halign="right", valign='middle')
        back_button.bind(on_press=lambda instance: self.go_back(current_screen))
        layout.add_widget(back_button)

        return layout

    def go_back(self, current_screen):
        # Switch to the previous screen
        if current_screen.name == 'first_screen':
            return
        previous_screen_index = self.screen_manager.screens.index(current_screen) - 1
        self.screen_manager.current = self.screen_manager.screens[previous_screen_index].name

    def show_dropdown(self, instance):
        # Open the dropdown when the button is clicked
        self.dropdown.open(instance)

    def select_option(self, option, dropdown, current_screen):
        # Handle the selected option
        print(f"Selected option: {option}")
        dropdown.dismiss()

        # Switch screens based on the selected option
        if option == 'Option 1':
            self.screen_manager.current = 'second_screen'
        elif option == 'Option 2':
            self.screen_manager.current = 'third_screen'
        elif option == 'Option 3':
            self.screen_manager.current = 'fourth_screen'
        elif option == 'Option 4':
            self.screen_manager.current = 'fifth_screen'

    def send_message(self, instance):
        message = self.input_field.text
        if message:
            self.messages.append(message)
            self.add_message(message, sender='You')  # Assuming all messages are from 'You'
            self.input_field.text = ''  # Clear the input field

    def add_message(self, message, sender='You'):
        # Create a message box with an orange or sky-blue background
        message_box = BoxLayout(orientation='vertical', size_hint_y=None, height=50)

        if sender == 'You':
            color = (0.529, 0.808, 0.922, 1)  # Sky-blue color
        else:
            color = (1, 0.647, 0, 1)  # Orange color

        with message_box.canvas.before:
            Color(*color)
            Rectangle(pos=message_box.pos, size=message_box.size)

        # Add a label for the message
        message_label = Label(text=f"{sender}: {message}", size_hint_y=None, height=50)
        message_box.add_widget(message_label)

        # Add the message box to the message layout
        self.message_layout.add_widget(message_box)

        # Scroll to the latest message
        self.message_layout.parent.scroll_y = 0

# Only run the CombinedChatApp
if __name__ == '__main__':
    CombinedChatApp().run()
