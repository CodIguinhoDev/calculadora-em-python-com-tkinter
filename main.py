import tkinter as tk


def input_user(value):
    inputUser.insert(tk.END, value)


def calculate():
    try:
        # Pega o texto do Entry, avalia como expressão matemática
        result = eval(inputUser.get())

        # Limpa o campo e insere o resultado
        inputUser.delete(0, tk.END)
        inputUser.insert(tk.END, str(result))

    except:
        # Em caso de erro, limpa e mostra "ERROR"
        inputUser.delete(0, tk.END)
        inputUser.insert(tk.END, "ERROR")


def clear():
    inputUser.delete(0, tk.END)


window = tk.Tk()
window.title("CALCULADORA")
window.geometry("400x500")


# CAMPO DE ENTRADA (DISPLAY)
inputUser = tk.Entry(
    window, width=20, font=("Arial", 24), borderwidth=2, relief="solid"
)
# Ocupa as 4 colunas da grade
inputUser.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# BOTÕES NUMÉRICOS
# (texto, linha, coluna)
numbers = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("0", 4, 1),
]

# Criação dinâmica dos botões numéricos
for text, line, column in numbers:
    button = tk.Button(
        window,
        text=text,
        width=5,
        height=2,
        font=("Arial", 18),
        command=lambda t=text: input_user(t),
    )
    button.grid(row=line, column=column, padx=5, pady=5)


# BOTÕES DE OPERAÇÃO
# (+, -, *, /)
operations = [("+", 1, 3), ("-", 2, 3), ("*", 3, 3), ("/", 4, 3)]

for op, line, column in operations:
    button = tk.Button(
        window,
        text=op,
        width=5,
        height=2,
        font=("Arial", 18),
        command=lambda o=op: input_user(o),
    )
    button.grid(row=line, column=column, padx=5, pady=5)


# BOTÃO CLEAR (C)
clear_btn = tk.Button(
    window, text="C", width=5, height=2, font=("Arial", 18), command=clear
)
clear_btn.grid(row=4, column=0, padx=5, pady=5)


# BOTÃO DE IGUAL (=)
equal_btn = tk.Button(
    window, text="=", width=5, height=2, font=("Arial", 18), command=calculate
)
equal_btn.grid(row=4, column=2, padx=5, pady=5)


window.mainloop()
