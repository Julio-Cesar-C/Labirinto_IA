from random import shuffle, randrange
from colorama import Fore, Back, Style, init

def make_maze(w = 10, h = 10):
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
    ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
    hor = [["+--"] * w + ['+'] for _ in range(h + 1)]


    def walk(x, y):
        # Visita uma célula e todas as suas células adjacentes,
        #    em profundidade, unindo-as ao labirinto corrente.
        
        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            # Remove a parede entre células
            if xx == x: hor[max(y, yy)][x] = "+  "
            if yy == y: ver[y][max(x, xx)] = "   "
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
    print(find_path(0, 10))
        

    # Desenha o resultado na tela
    for i, (a, b) in enumerate(zip(hor, ver)):
        row = ''.join(a + ['\n'] + b)

        # Adiciona o caractere '#' azul no caminho encontrado
        if i >= 1 and i < h - 1:
            row = Back.BLUE + Fore.WHITE + row[:3] + '#' + row[4:-2] + row[-2:] + Style.RESET_ALL

        print(row)

make_maze()