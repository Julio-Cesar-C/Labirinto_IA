from random import shuffle, randrange

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

    # Imprime o resultado na tela
    print(ver)
    print("\n")
    print(hor)
    
    for (a, b) in zip(hor, ver):
        print(''.join(a + ['\n'] + b))
    
    # result = zip(hor, ver)
    
    # result1 = (list(result))
    # print((result1[0][0][0]))
    # print((result1[0][1][0]))
    
    # n_col = (len(result1)-1)*3+1
    # n_lin = (len(result1)-1)*2+1
    # print(n_lin,n_col)
    
    # mat = []
    
    # for lista in result1:
    #     l1 = lista[0]
    #     l2 = lista[1]
    #     aux = []
    #     for str1 in l1:
    #         for s in str1:
    #             if s!=" ":
    #                 aux.append(1)
    #             else:
    #                 aux.append(0)
    #         mat.append(aux)
        
    #     aux = []
    #     for str1 in l2:
    #         for s in str1:
    #             if s!=" ":
    #                 aux.append(1)
    #             else:
    #                 aux.append(0)
    #         mat.append(aux)
    
    # print(mat)
            
    
  
    
make_maze()