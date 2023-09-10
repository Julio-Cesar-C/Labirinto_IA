import entry
import tkinter as tk
import Grid

# Variaveis do tamanho da janela do Tkinter
window_height = 350
window_width = 350

# Variaveis do tamanho do grid
width = 4
height = 4

root = tk.Tk()


class Application(tk.Frame):
    def __init__(self, master=None):
        container1 = tk.Frame(master, borderwidth=2, relief="groove")
        container1.pack(fill=tk.X, pady=10, padx=5)

        # Obtem matriz com cordenadas do grid
        matriz = Grid.make_maze(height, width)

        Grid.draw_grid(container1, height+2, width+2)
        Grid.paint_outline(matriz, container1)


# Altera o posicionamento da tela para o meio do monitor principal
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.geometry("{}x{}+{}+{}".format(window_width,
              window_height, x_cordinate, y_cordinate))

Application(root)
root.title("Labirinto IA")
# Impede o redimensionamento horizontal e vertical
root.resizable(False, False)
root.mainloop()
