import entry
import tkinter as tk

# Variaveis do tamanho da janela do Tkinter
window_height = 350
window_width = 350

# Variaveis do tamanho do grid
width = 10
height = 10

cell_matrix = []

root = tk.Tk()


class Application(tk.Frame):
    def __init__(self, master=None):
        container1 = tk.Frame(master, borderwidth=2, relief="groove")
        container1.pack(fill=tk.X, pady=10, padx=5)

        # Cria uma celula para cada medida H e W
        for x in range(height):
            row = []
            for y in range(height):
                cell = tk.Entry(container1, width=2, text="A")
                cell.grid(row=x, column=y)
                row.append(cell)
            cell_matrix.append(row)

        entry.change_entry_color(container1, 1, 1, "blue")


# Altera o posicionamento da tela para o meio do monitor principal
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.geometry("{}x{}+{}+{}".format(window_width,
              window_height, x_cordinate, y_cordinate))

Application(root)
root.title("Labirinto IA")
root.resizable(False, False) # Impede o redimensionamento horizontal e vertical
root.mainloop()
