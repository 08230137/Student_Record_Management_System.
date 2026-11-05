
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window


class HelloWorldApp(App):

    def build(self):
        # Main window
        self.title = "Kivy - Karma Yangchen"
        Window.size = (550, 400)

        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=15
        )

        # Main heading
        heading = Label(
            text="Hello World!",
            font_size=30,
            color=(0.25, 0.41, 0.88, 1)
        )

        # Welcome message
        message = Label(
            text="My First Kivy GUI Application",
            font_size=18
        )

        # Interactive button
        button = Button(
            text="Click Me",
            font_size=18,
            background_normal="",
            background_color=(0.25, 0.41, 0.88, 1),
            size_hint=(1, 0.3)
        )

        button.bind(on_press=self.show_message)

        # Student information
        student_info = Label(
            text=(
                "Karma Yangchen | Student ID: 08230137\n"
                "IT A | Roll No: 6"
            ),
            font_size=15,
            halign="center",
            valign="middle",
            color=(0.25, 0.41, 0.88, 1)
        )

        student_info.bind(
            size=lambda instance, value:
            setattr(instance, "text_size", value)
        )

        # Add widgets to layout
        layout.add_widget(heading)
        layout.add_widget(message)
        layout.add_widget(button)
        layout.add_widget(student_info)

        return layout

    # Function to handle button click
    def show_message(self, instance):
        instance.text = "Welcome to Kivy!"


if __name__ == "__main__":
    HelloWorldApp().run()
