import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pyperclip


def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid input")
        return

    operator = combo_operator.get()

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        try:
            result = num1 / num2
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero")
            return
    elif operator == '^':
        result = num1 ** num2

    result_label.config(text="Result: " + str(result))


def change_base():
    try:
        num = int(entry_num1_base.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid input")
        return

    base = int(combo_base.get())
    result = ''

    if base == 2:
        result = bin(num)[2:]
    elif base == 8:
        result = oct(num)[2:]
    elif base == 10:
        result = num
    elif base == 16:
        result = hex(num)[2:].upper()

    base_result_label.config(text="Result: " + str(result))


def copy_result():
    result_text = result_label.cget("text")  # Получение текста из метки
    result_text = result_text.split(":")[1].strip()  # Извлечение результата
    pyperclip.copy(result_text)  # Копирование результата в буфер обмена


# Create main window
root = tk.Tk()
root.title("Calculator")

# Set window to full screen
root.attributes('-fullscreen', False)

# Calculate window size as 0.3 of the screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = int(screen_width * 0.45)
window_height = int(screen_height * 0.45)

# Set window size
root.geometry(f"{window_width}x{window_height}")

# Calculate position to center the calculator
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

# Set window position
root.geometry(f"+{x_position}+{y_position}")

# Create input fields and labels for basic arithmetic operations
entry_num1 = tk.Entry(root, width=9, font=('Arial', 24))
entry_num1.grid(row=0, column=0)

combo_operator = ttk.Combobox(root, values=['+', '-', '*', '/', '^'], font=('Arial', 24))
combo_operator.grid(row=0, column=1)
combo_operator.current(0)

entry_num2 = tk.Entry(root, width=9, font=('Arial', 24))
entry_num2.grid(row=0, column=2)

result_label = tk.Label(root, text="Result: ", font=('Arial', 24))
result_label.grid(row=1, columnspan=3)

# Create button for basic arithmetic operations
calculate_button = tk.Button(root, text="Calculate", command=calculate, width=15, height=3, font=('Arial', 18))
calculate_button.grid(row=2, columnspan=3)

# Create button for copying result
copy_button = tk.Button(root, text="Copy Result", command=copy_result, width=15, height=3, font=('Arial', 18))
copy_button.grid(row=2, columnspan=1)

# Create input fields and labels for changing base
entry_num1_base = tk.Entry(root, width=9, font=('Arial', 24))
entry_num1_base.grid(row=3, column=0)

combo_base = ttk.Combobox(root, values=[i for i in range(2, 65)], font=('Arial', 24))
combo_base.grid(row=3, column=1)
combo_base.current(2)

base_result_label = tk.Label(root, text="Result: ", font=('Arial', 24))
base_result_label.grid(row=4, columnspan=3)

# Create button for changing base
change_base_button = tk.Button(root, text="Change Base", command=change_base, width=15, height=3, font=('Arial', 18))
change_base_button.grid(row=5, columnspan=3)

root.mainloop()
