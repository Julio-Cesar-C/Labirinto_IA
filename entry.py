import tkinter as tk


def change_entry_color(container, row, col, new_color):
    entry = None
    for widget in container.winfo_children():  # Lista todos os widgets que estão dentro do container
        if isinstance(widget, tk.Entry):  # Verificar se o widget é um objeto Entry
            # Verifica se a posicao do widget é a desejada
            if int(widget.grid_info()["row"]) == row and int(widget.grid_info()["column"]) == col:
                entry = widget
                break
    if entry:  # Se o Entry desejado foi encontrado, altera a cor
        entry.config(bg=new_color)

def change_entry_text(container, row, col, texto):
    entry = None
    for widget in container.winfo_children():  # Lista todos os widgets que estão dentro do container
        if isinstance(widget, tk.Entry):  # Verificar se o widget é um objeto Entry
            # Verifica se a posicao do widget é a desejada
            if int(widget.grid_info()["row"]) == row and int(widget.grid_info()["column"]) == col:
                entry = widget
                break
    if entry:  # Se o Entry desejado foi encontrado, altera a cor
        entry.insert(0, texto)  # Insere o novo texto na Entry