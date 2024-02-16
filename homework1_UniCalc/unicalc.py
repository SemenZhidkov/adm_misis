# Жидков Семён, Ковалёва Мария, Зебелян Артем - БПМ-22-3

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Calculator(App):
    def build(self):
        self.current_mode = 'decimal'  # Изначально выбрана десятичная система счисления
        self.operations = ['+', '-', '*', '/']
        self.numbers = [str(i) for i in range(10)]
        self.hex_numbers = ['A', 'B', 'C', 'D', 'E', 'F']

        self.input_text = TextInput(multiline=False, readonly=True, font_size=50)
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+'],  # Изменили кнопку "." на "C" для сброса
            ['A', 'B', 'C', ''],   # Добавили кнопки для шестнадцатеричных чисел
            ['D', 'E', 'F', '']
        ]

        mode_button = Button(text='Decimal', on_press=self.change_mode)
        mode_button.size_hint = (None, None)
        mode_button.width = 100
        mode_button.height = 100

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(mode_button)
        layout.add_widget(self.input_text)

        for row in buttons:
            button_box = BoxLayout()
            for label in row:
                button = Button(text=label, on_press=self.on_button_press)
                button_box.add_widget(button)
            layout.add_widget(button_box)

        return layout

    def change_mode(self, instance):
        if self.current_mode == 'decimal':
            self.current_mode = 'binary'
            instance.text = 'Binary'
        elif self.current_mode == 'binary':
            self.current_mode = 'octal'
            instance.text = 'Octal'
        elif self.current_mode == 'octal':
            self.current_mode = 'hexadecimal'
            instance.text = 'Hexadecimal'
        else:
            self.current_mode = 'decimal'
            instance.text = 'Decimal'

    def to_decimal(self, number):
        try:
            if self.current_mode == 'binary':
                return str(int(number, 2))
            elif self.current_mode == 'octal':
                return str(int(number, 8))
            elif self.current_mode == 'hexadecimal':
                decimal_value = 0
                for char in number:
                    if char.isdigit():
                        decimal_value = 16 * decimal_value + int(char)
                    elif char.upper() in self.hex_numbers:
                        decimal_value = 16 * decimal_value + self.hex_numbers.index(char.upper()) + 10
                    else:
                        raise ValueError("Invalid hexadecimal character: {}".format(char))
                return str(decimal_value)
            else:
                return str(float(number))
        except ValueError as e:
            return 'Error: {}'.format(e)

    def from_decimal(self, number):
        if self.current_mode == 'binary':
            return bin(int(number))[2:]
        elif self.current_mode == 'octal':
            return oct(int(number))[2:]
        elif self.current_mode == 'hexadecimal':
            return hex(int(number))[2:].upper()
        else:
            return str(number)

    def on_button_press(self, instance):
        current = self.input_text.text

        if instance.text == '=':
            try:
                result = self.from_decimal(eval(current))
                self.input_text.text = result
            except Exception as e:
                self.input_text.text = 'Error'
        elif instance.text == 'C':  # Обрабатываем сброс текущего значения
            self.input_text.text = ''
        else:
            if (self.current_mode == 'decimal' and instance.text in self.numbers) or \
                    (self.current_mode == 'binary' and instance.text in ['0', '1']) or \
                    (self.current_mode == 'octal' and instance.text in [str(i) for i in range(8)]) or \
                    (self.current_mode == 'hexadecimal' and (
                            instance.text.isdigit() or instance.text.upper() in self.hex_numbers)) or \
                    instance.text in ['+', '-', '*', '/']:
                if self.current_mode == 'hexadecimal' and instance.text.upper() in self.hex_numbers:
                    self.input_text.text += str(self.hex_numbers.index(instance.text.upper()) + 10)
                else:
                    self.input_text.text += instance.text


if __name__ == '__main__':
    Calculator().run()






































