
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
        self.rim_numbers = ['I', 'V', 'X', 'M']

        self.input_text = TextInput(multiline=False, readonly=True, font_size=50)
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['Clear', '0', '=', '+'],  # "Clear" для сброса
            ['A', 'B', 'C', '.'],  # Добавили кнопки для шестнадцатеричных чисел
            ['D', 'E', 'F', ''],
            ['I', 'V', 'X']
        ]

        mode_button = Button(text='Decimal', on_press=self.change_mode)
        mode_button.size_hint = (None, None)
        mode_button.width = 200
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
        elif self.current_mode == 'hexadecimal':
            self.current_mode = 'roman'
            instance.text = 'Roman'
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
            if self.current_mode == 'roman':
                try:
                    result = self.calculate_roman(current)
                    self.input_text.text = result
                except Exception as e:
                    self.input_text.text = 'Error'
            else:
                try:
                    result = self.from_decimal(eval(current))
                    self.input_text.text = result
                except Exception as e:
                    self.input_text.text = 'Error'
        elif instance.text == 'Clear':  # Обрабатываем сброс текущего значения
            self.input_text.text = ''
        elif instance.text == '.':
            if self.current_mode == 'decimal' and current and current[-1].isdigit():
                    # Разрешаем добавление точки, если режим - десятичный и текущий ввод - число
                self.input_text.text += instance.text
        elif instance.text == '.':
            if self.current_mode == 'decimal' and current and current[-1].isdigit():
                # Разрешаем добавление точки, если режим - десятичный и текущий ввод - число
                self.input_text.text += instance.text
        else:
            if (self.current_mode == 'decimal' and instance.text in self.numbers) or \
                    (self.current_mode == 'binary' and instance.text in ['0', '1']) or \
                    (self.current_mode == 'octal' and instance.text in [str(i) for i in range(8)]) or \
                    (self.current_mode == 'hexadecimal' and (
                            instance.text.isdigit() or instance.text.upper() in self.hex_numbers)) or \
                    instance.text in ['+', '-', '*', '/']:
                if self.current_mode == 'hexadecimal' and instance.text.upper() in self.hex_numbers:
                    value = self.hex_numbers.index(instance.text.upper()) + 10
                    self.input_text.text += str(value)
                else:
                    self.input_text.text += instance.text
            if (self.current_mode == 'roman' and instance.text in self.rim_numbers):
                self.input_text.text += instance.text

    def roman_to_int(self, roman_num):
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_value = 0

        for i in range(len(roman_num) - 1, -1, -1):
            if roman_dict[roman_num[i]] < prev_value:
                result -= roman_dict[roman_num[i]]
            else:
                result += roman_dict[roman_num[i]]
            prev_value = roman_dict[roman_num[i]]
        return result

    def int_to_roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ''
        i = 0

        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

    def calculate_roman(self, expression):
        try:
            operators = ['+', '-', '*', '/']
            operator = None
            for op in operators:
                if op in expression:
                    operator = op
                    break

            parts = expression.split(operator)
            num1 = self.roman_to_int(parts[0].strip())
            num2 = self.roman_to_int(parts[1].strip())

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 // num2

            return self.int_to_roman(result)

        except Exception as e:
            return 'Error: Invalid expression'


if __name__ == '__main__':
    Calculator().run()








































