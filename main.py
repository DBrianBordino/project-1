from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculatorApp(App):
    def build(self):
        self.operators = ['+', '-', '*', '/']
        self.last_was_operator = None
        self.last_button = None
        self.result = TextInput(font_size=32, readonly=True, halign='right', multiline=False)
        layout = GridLayout(cols=4, spacing=2)
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        for button in buttons:
            layout.add_widget(Button(text=button, on_press=self.on_button_press))
        layout.add_widget(self.result)
        return layout

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text

        if button_text == '=':
            try:
                # Perform the calculation
                result = str(eval(current))
                self.result.text = result
            except:
                self.result.text = 'Error'
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                # Don't allow consecutive operators
                return
            elif current == '' and button_text in self.operators:
                # First character can't be an operator
                return
            else:
                new_text = current + button_text
                self.result.text = new_text

        self.last_button = instance
        self.last_was_operator = button_text in self.operators


if __name__ == '__main__':
    app = CalculatorApp()
    app.run()
