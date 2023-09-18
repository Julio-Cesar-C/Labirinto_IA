import tkinter as tk
import Grid

# Variaveis do tamanho da janela do Tkinter
window_height = 350
window_width = 350

root = tk.Tk()


class Application(tk.Frame):
    entry_width = None
    entry_height = None

    def __init__(self, master=None):
        # Container to shelter container_width and container_height
        container_options = tk.Frame(
            master, height=200, borderwidth=2, relief="groove")
        container_options.pack(fill=tk.X, padx=5, pady=5)

        # Width
        container_width = tk.Frame(
            container_options, height=200, borderwidth=2)
        container_width.pack(fill=tk.X, padx=5, pady=5)

        text_width = tk.Label(container_width, text="Width",)
        text_width.pack(side=tk.LEFT)

        self.entry_width = tk.Entry(container_width)
        self.entry_width.pack(side=tk.RIGHT)

        # Height
        container_height = tk.Frame(
            container_options, height=200, borderwidth=2)
        container_height.pack(fill=tk.X, padx=5, pady=5)

        text_height = tk.Label(container_height, text="Height",)
        text_height.pack(side=tk.LEFT)

        self.entry_height = tk.Entry(container_height)
        self.entry_height.pack(side=tk.RIGHT)

        container_maze = tk.Frame(master, borderwidth=2, relief="groove")
        # Button Make Maze
        button_make = tk.Button(
            text="Make Maze", command=lambda: self.generate_maze(container_maze))
        button_make.pack()

        container_maze.pack(fill=tk.X, pady=10, padx=5)

    def generate_maze(self, container):
        self.clean_maze_container(container) # Limpa o container container_maze se já houver widgets

        # Obtem matriz com cordenadas do grid 
        matriz = Grid.make_maze(
            int(self.entry_height.get()), int(self.entry_width.get()))

        Grid.draw_grid(container, len(matriz)+2, len(matriz))
        Grid.paint_maze(matriz, container)
        Grid.paint_outline(matriz, container)



    def clean_maze_container(self,container):
        # Itere sobre os widgets no container e destrua-os
        for widget in container.winfo_children():
            widget.destroy()

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
