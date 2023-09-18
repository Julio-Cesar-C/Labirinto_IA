import tkinter as tk
import Grid
import maze

# Variaveis do tamanho da janela do Tkinter
window_height = 600
window_width = 450

root = tk.Tk()


class Application(tk.Frame):
    MATRIZ_GLOBAL=[]
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


        #Find path container
        container_find_path = tk.Frame(
            master, height=200, borderwidth=2, relief="groove")
        container_find_path.pack(fill=tk.X, padx=5, pady=5)
        # End
        container_end = tk.Frame(
            container_find_path, height=200, borderwidth=2)
        container_end.pack(fill=tk.X, padx=5, pady=5)

        text_end = tk.Label(container_end, text="End coordinate",)
        text_end.pack(side=tk.LEFT)

        self.entry_end = tk.Entry(container_end)
        self.entry_end.pack(side=tk.RIGHT)

        container_maze = tk.Frame(master, borderwidth=2, relief="groove")
        # Button Make Maze
        button_make = tk.Button(
            text="Make Maze", command=lambda: self.generate_maze(container_maze))
        button_make.pack()
        button_find_path = tk.Button(
            text="Find Path", command=lambda: self.activate_find_path())
        button_find_path.pack()

        container_maze.pack(fill=tk.X, pady=10, padx=5)



    def generate_maze(self, container):
        self.clean_maze_container(container) # Limpa o container container_maze se já houver widgets

        # Obtem matriz com cordenadas do grid 
        self.MATRIZ_GLOBAL = Grid.make_maze(
            int(self.entry_height.get()), int(self.entry_width.get()))

        Grid.draw_grid(container, len(self.MATRIZ_GLOBAL), len(self.MATRIZ_GLOBAL))
        Grid.paint_maze(self.MATRIZ_GLOBAL, container)
        Grid.paint_outline(self.MATRIZ_GLOBAL, container)

    def activate_find_path(self):
        maze.find_path(self.MATRIZ_GLOBAL,inicio = (1, 1),fim = (len(self.MATRIZ_GLOBAL) - 3, int(self.entry_end.get())))



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
