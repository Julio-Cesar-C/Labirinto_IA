from random import shuffle, randrange
import entry
import tkinter as tk


def make_maze(w, h):
    """ Cria um labirinto aleatório e o desenha na tela em ASCII Art
        Parâmetros:
            w - o número de colunas do labirinto (padrão: 16)
            h - o número de linhas do labirinto (padrão: 8)
    """

    # Matriz de células visitadas (0 = não visitada, 1 = visitada)
    # Delimitada por uma linha/coluna com todos visitados (fronteira)
    # Sofre overflow nos índices negativos
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]

    # Linhas contendo as células e linhas entre-células
    # Inicia-se com todas as células disjuntas (paredes entre todas elas)
    ver = [["| "] * w + ['|'] for _ in range(h)] + [[]]
    hor = [["+-"] * w + ['+'] for _ in range(h + 1)]

    # Cria uma matriz com valor padrão 1 para cada coluna(w) e linha(h)
    #matriz = [[1 for _ in range((w*2))] for i in range((h*2)-1)]

    def walk(x, y):
        # Visita uma célula e todas as suas células adjacentes,
        #    em profundidade, unindo-as ao labirinto corrente.

        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        print(d)
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]:
                continue
            # Remove a parede entre células
            if xx == x:
                hor[max(y, yy)][x] = "+ "#"+  "
                #matriz[max(y, yy)][x+1] = 0
                #matriz[max(y, yy)][x+2] = 0


            if yy == y:
                ver[y][max(x, xx)] = "  " #"   "
                #matriz[y+1][(max(x, xx))] = 0
                #matriz[y+2][max(x, xx)] = 0


            walk(xx, yy)

    # Visita a célula de origem
    walk(randrange(w), randrange(h))

    # Função para encontrar um caminho no labirinto
    def find_path(x, y):
        if x < 0 or x >= w or y < 0 or y >= h or vis[y][x] == 1:
            return False  # Fora dos limites ou já visitada
        if x == w - 1:
            return True  # Chegou à coluna final, encontrou o caminho

        vis[y][x] = 1  # Marca a célula como visitada

        # Tenta mover para a esquerda, direita, cima ou baixo
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        shuffle(directions)
        for dx, dy in directions:
            if find_path(x + dx, y + dy):
                return True

        return False

    # Encontra o ponto de partida e inicia a busca pelo caminho
    #print(find_path(0, 10))
    z =-1

    matriz = []
    # Desenha o resultado na tela
    for i, (a, b) in enumerate(zip(hor, ver)):
        z=z+1
        row = ''.join([str(z)]+[" |"]+a + ['\n']+[str(z+1)]+[" |"] + b)
        z=z+1
        matriz.append(a)
        matriz.append(b)
        print(row)

    i =-1
    print('')

    #primeira parte se refere a linha, a segunda se refere a altura
    matrizConvertida=[[0 for _ in range((w*2)+1)] for i in range((h*2)+2)]

    rowCount=0
    for row in matriz:
        charCount=0
        for col in row:
            for char in col:
                if(char!=' '):
                    matrizConvertida[rowCount][charCount]=1
                charCount=charCount+1
        rowCount=rowCount+1

    #Converte matriz

    """
    #(Temporaly) prints matriz formatted
    for y in range((w*2)-1):
        i=i+1
        print(str(i)+" |", end='')
        for x in range((h*2)):
            print(matriz[y][x], end='')
        print("|", end='')
        print('')
        """
    return matrizConvertida

def draw_grid(container, height, width):
    """
    Cria uma celula para cada medida H e W
    """
    for x in range(width):
        row = []
        for y in range(height):
            cell = tk.Entry(container, width=2)
            cell.grid(row=x, column=y)
            row.append(cell)


def paint_outline(matriz, container):
    #Preenche verticalmente
    for h in range((len(matriz)-1)):

        # Pinta toda a primeira linha de preto
        entry.change_entry_color(container, h, 0, "black")
        # Pinta toda a ultima linha de preto
        entry.change_entry_color(container, h, len(matriz)-2, "black")

    #Preenche horizontalmente
    for w in range(len(matriz[0])):
        # Pinta toda a primeira linha de preto
        entry.change_entry_color(container, 0, w, "black")
        # Pinta toda a ultima linha de preto
        entry.change_entry_color(container, len(matriz)-2, w, "black")

def paint_maze(matriz, container):
    rowCount=0
    for row in matriz:
        colCount = 0
        for char in row:
            if(char==1):
                entry.change_entry_color(container, rowCount, colCount, "grey")
            colCount=colCount+1
        rowCount=rowCount+1

