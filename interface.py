import tkinter as tk
import Grid
import maze

# Variaveis do tamanho da janela do Tkinter
window_height = 600
window_width = 450

root = tk.Tk()


class Application(tk.Frame):
    MATRIZ = []

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

        # Find path container
        container_find_path = tk.Frame(
            master, height=200, borderwidth=2, relief="groove")
        container_find_path.pack(fill=tk.X, padx=5, pady=5)

        # Coordenate X
        container_cordy = tk.Frame(
            container_find_path, height=200, borderwidth=2)
        container_cordy.pack(fill=tk.X, padx=5, pady=5)

        text_end = tk.Label(container_cordy, text="Coordinate X",)
        text_end.pack(side=tk.LEFT)

        self.entry_end = tk.Entry(container_cordy)
        self.entry_end.pack(side=tk.RIGHT)

        # Coordenate Y
        container_cordx = tk.Frame(
            container_find_path, height=200, borderwidth=2)
        container_cordx.pack(fill=tk.X, padx=5, pady=5)

        text_end1 = tk.Label(container_cordx, text="Coordinate Y",)
        text_end1.pack(side=tk.LEFT)

        self.entry_end1 = tk.Entry(container_cordx)
        self.entry_end1.pack(side=tk.RIGHT)

        # Limit field
        container_limit = tk.Frame(
            container_find_path, height=200, borderwidth=2)
        container_limit.pack(fill=tk.X, padx=5, pady=5)

        text_limit = tk.Label(
            container_limit, text="Limit (for prof limited and prof interactive)",)
        text_limit.pack(side=tk.LEFT)

        self.text_limit = tk.Entry(container_limit)
        self.text_limit.pack(side=tk.RIGHT)

        container_maze = tk.Frame(master, borderwidth=2, relief="groove")
        # Button Make Maze
        button_make = tk.Button(
            text="Make Maze", command=lambda: self.generate_maze(container_maze))
        button_make.pack()

        # Amplitude
        button_find_path_amplitude = tk.Button(
            text="Find Path (Amplitude)", command=lambda: self.activate_find_path_amplitude(container_maze))
        button_find_path_amplitude.pack()

        # Profundidade
        button_find_path_profundidade = tk.Button(
            text="Find Path (Profundidade)", command=lambda: self.activate_find_path_profundidade(container_maze))
        button_find_path_profundidade.pack()

        # Profundidade Limitada
        button_find_path_limitada = tk.Button(
            text="Find Path (Profundidade Limitada)", command=lambda: self.activate_find_path_profundidade_limitada(container_maze))
        button_find_path_limitada.pack()

        # AProfundamento interativo
        button_find_path_aprofundamento_interativo = tk.Button(
            text="Find Path (Aprofundamento Interativo)", command=lambda: self.activate_find_path_aprofundamento_interativo(container_maze))
        button_find_path_aprofundamento_interativo.pack()

        container_maze.pack(fill=tk.X, pady=10, padx=5)

    def generate_maze(self, container):
        # Obtem matriz com cordenadas do grid
        self.MATRIZ = Grid.make_maze(
            int(self.entry_height.get()), int(self.entry_width.get()))
        self.reset_maze_container(self.MATRIZ,container)

    def reset_maze_container(self, matriz,container):
        # Limpa o container container_maze se já houver widgets
        self.clean_maze_container(container)
        Grid.draw_grid(container, len(matriz), len(matriz))
        Grid.paint_maze(matriz, container)
        Grid.paint_outline(matriz, container)

    def activate_find_path_amplitude(self, container):
        self.reset_maze_container(self.MATRIZ,container)
        matriz_amplitude = self.MATRIZ
        Grid.paint_path(maze.amplitude(matriz_amplitude, inicio=[1, 1], fim=[
                        int(self.entry_end1.get()), int(self.entry_end.get())]), container)

    def activate_find_path_profundidade(self, container):
        self.reset_maze_container(self.MATRIZ,container)
        matriz_profundidade = self.MATRIZ

        Grid.paint_path(maze.profundidade(matriz_profundidade, inicio=[1, 1], fim=[
                        int(self.entry_end1.get()), int(self.entry_end.get())]), container)

    def activate_find_path_profundidade_limitada(self, container):
        self.reset_maze_container(self.MATRIZ,container)
        MATRIZ_PROFUNDIDADE_LIMITADA = self.MATRIZ

        Grid.paint_path(maze.prof_limitada(MATRIZ_PROFUNDIDADE_LIMITADA, inicio=[1, 1], fim=[int(
            self.entry_end1.get()), int(self.entry_end.get())], limite=int(self.text_limit.get())), container)

    def activate_find_path_aprofundamento_interativo(self, container):
        self.reset_maze_container(self.MATRIZ,container)
        matriz_prof_interativo = self.MATRIZ

        Grid.paint_path(maze.aprof_iterativo(matriz_prof_interativo, inicio=[1, 1], fim=[int(
            self.entry_end1.get()), int(self.entry_end.get())], lim_max=int(self.text_limit.get())), container)

    def clean_maze_container(self, container):
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
# root.resizable(False, False)
root.mainloop()
