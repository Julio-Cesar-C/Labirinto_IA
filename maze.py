class No(object):
    def __init__(self, pai=None, coordenada=None, nivel=None, anterior=None,
                 proximo=None):
        self.pai = pai
        self.coordenada = coordenada
        self.nivel = nivel
        self.anterior = anterior
        self.proximo = proximo


class lista(object):
    head = None
    tail = None

    # INSERE NO INÍCIO DA LISTA
    def inserePrimeiro(self, v1, v2, p):
        novo_no = No(p, v1, v2, None, None)
        if self.head == None:
            self.tail = novo_no
            self.head = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
            self.head = novo_no

    # INSERE NO FIM DA LISTA
    def insereUltimo(self, v1, v2, p):

        novo_no = No(p, v1, v2, None, None)

        if self.head is None:
            self.head = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior = self.tail
        self.tail = novo_no

    # REMOVE NO INÍCIO DA LISTA
    def deletaPrimeiro(self):
        if self.head is None:
            return None
        else:
            no = self.head
            self.head = self.head.proximo
            if self.head is None:
                self.tail = None
            else:
                self.head.anterior = None
            return no

    # REMOVE NO FIM DA LISTA
    def deletaUltimo(self):
        if self.tail is None:
            return None
        else:
            no = self.tail
            self.tail = self.tail.anterior
            if self.tail is None:
                self.head = None
            else:
                self.tail.proximo = None

            return no

    def vazio(self):
        if self.head is None:
            return True
        else:
            return False

    def exibeLista(self):

        aux = self.head
        str = []
        while aux != None:
            temp = []
            temp.append(aux.coordenada)
            temp.append(aux.nivel)
            str.append(temp)
            aux = aux.proximo

        return str

    def exibeCaminho(self):

        atual = self.tail
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.coordenada)
            atual = atual.pai
        caminho.append(atual.coordenada)
        caminho = caminho[::-1]
        return caminho

    def exibeCaminho1(self, valor):

        atual = self.head
        while atual.coordenada != valor:
            atual = atual.proximo

        caminho = []
        atual = atual.pai
        while atual.pai is not None:
            caminho.append(atual.coordenada)
            atual = atual.pai
        caminho.append(atual.coordenada)
        return caminho

    def primeiro(self):
        return self.head

    def ultimo(self):
        return self.tail


def sucessor(x, y, mapa):
    filhos = []
    if mapa[x-1][y] != 1:
        aux = []
        aux.append(x-1)
        aux.append(y)
        filhos.append(aux)
    if mapa[x+1][y] != 1:
        aux = []
        aux.append(x+1)
        aux.append(y)
        filhos.append(aux)
    if mapa[x][y-1] != 1:
        aux = []
        aux.append(x)
        aux.append(y-1)
        filhos.append(aux)
    if mapa[x][y+1] != 1:
        aux = []
        aux.append(x)
        aux.append(y+1)
        filhos.append(aux)
    return filhos


def amplitude(mapa, inicio, fim):
    mapaNovo=mapa
    # caminho = [[1,1],[1,2]]

    caminho = []
    # manipular a FILA para a busca
    l1 = lista()

    # cópia para apresentar o caminho (somente inserção)
    l2 = lista()

    # insere ponto inicial como nó raiz da árvore
    l1.insereUltimo(inicio, 0, None)
    l2.insereUltimo(inicio, 0, None)

    # controle de nós visitados
    visitado = []
    linha = []
    linha.append(inicio)
    linha.append(0)
    visitado.append(linha)

    while not l1.vazio():
        # remove o primeiro da fila
        atual = l1.deletaPrimeiro()
        x = atual.coordenada[0]
        y = atual.coordenada[1]

        filhos = []
        filhos = sucessor(x, y, mapaNovo)

        # varre todos as conexões dentro do grafo a partir de atual
        for novo in filhos:
            flag = True  # pressuponho que não foi visitado

            # para cada conexão verifica se já foi visitado
            for j in range(len(visitado)):
                if visitado[j][0] == novo:
                    if visitado[j][1] <= (atual.nivel+1):
                        flag = False
                    else:
                        visitado[j][1] = atual.nivel+1
                    break

            # se não foi visitado inclui na fila
            if flag:
                l1.insereUltimo(novo, atual.nivel + 1, atual)
                l2.insereUltimo(novo, atual.nivel + 1, atual)

                # marca como visitado
                linha = []
                linha.append(novo)
                linha.append(atual.nivel+1)
                visitado.append(linha)

                # verifica se é o objetivo
                if novo == fim:

                    caminho += l2.exibeCaminho()
                    for t in caminho:
                        mapaNovo[t[0]][t[1]] = 2
                    return mapaNovo
    return mapaNovo


def profundidade(mapa, inicio, fim):

    caminho = []
    # manipular a FILA para a busca
    l1 = lista()

    # cópia para apresentar o caminho (somente inserção)
    l2 = lista()

    # insere ponto inicial como nó raiz da árvore
    l1.insereUltimo(inicio, 0, None)
    l2.insereUltimo(inicio, 0, None)

    # controle de nós visitados
    visitado = []
    linha = []
    linha.append(inicio)
    linha.append(0)
    visitado.append(linha)

    while not l1.vazio():
        # remove o primeiro da fila
        atual = l1.deletaUltimo()
        x = atual.coordenada[0]
        y = atual.coordenada[1]

        filhos = []
        filhos = sucessor(x, y, mapa)

        # varre todos as conexões dentro do grafo a partir de atual
        for novo in filhos:

            flag = True  # pressuponho que não foi visitado

            # para cada conexão verifica se já foi visitado
            for j in range(len(visitado)):
                if visitado[j][0] == novo:
                    if visitado[j][1] <= (atual.nivel+1):
                        flag = False
                    else:
                        visitado[j][1] = atual.nivel+1
                    break

            # se não foi visitado inclui na fila
            if flag:
                l1.insereUltimo(novo, atual.nivel + 1, atual)
                l2.insereUltimo(novo, atual.nivel + 1, atual)

                # marca como visitado
                linha = []
                linha.append(novo)
                linha.append(atual.nivel+1)
                visitado.append(linha)

                # verifica se é o objetivo
                if novo == fim:
                    caminho += l2.exibeCaminho()
                    # print("Árvore de busca:\n",l2.exibeLista())
                    for t in caminho:
                        mapa[t[0]][t[1]] = 2
                    return mapa
    return mapa


def prof_limitada(mapa, inicio, fim, limite):

    caminho = []
    # manipular a FILA para a busca
    l1 = lista()

    # cópia para apresentar o caminho (somente inserção)
    l2 = lista()

    # insere ponto inicial como nó raiz da árvore
    l1.insereUltimo(inicio, 0, None)
    l2.insereUltimo(inicio, 0, None)

    # controle de nós visitados
    visitado = []
    linha = []
    linha.append(inicio)
    linha.append(0)
    visitado.append(linha)

    while not l1.vazio():
        # remove o primeiro da fila
        atual = l1.deletaUltimo()
        x = atual.coordenada[0]
        y = atual.coordenada[1]

        if atual.nivel < limite:

            filhos = []
            filhos = sucessor(x, y, mapa)

            # varre todos as conexões dentro do grafo a partir de atual
            for novo in filhos:

                flag = True  # pressuponho que não foi visitado

                # para cada conexão verifica se já foi visitado
                for j in range(len(visitado)):
                    if visitado[j][0] == novo:
                        if visitado[j][1] <= (atual.nivel+1):
                            flag = False
                        else:
                            visitado[j][1] = atual.nivel+1
                        break

                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo, atual.nivel + 1, atual)
                    l2.insereUltimo(novo, atual.nivel + 1, atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.nivel+1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo == fim:
                        caminho += l2.exibeCaminho()
                        for t in caminho:
                            mapa[t[0]][t[1]] = 2
                    return mapa
    return mapa


def aprof_iterativo(mapa, inicio, fim, lim_max):

    for limite in range(1, lim_max):

        caminho = []
        # manipular a FILA para a busca
        l1 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio, 0, None)
        l2.insereUltimo(inicio, 0, None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while not l1.vazio():
            # remove o primeiro da fila
            atual = l1.deletaUltimo()
            x = atual.coordenada[0]
            y = atual.coordenada[1]

            if atual.nivel < limite:

                filhos = []
                filhos = sucessor(x, y, mapa)

                # varre todos as conexões dentro do grafo a partir de atual
                for novo in filhos:

                    flag = True  # pressuponho que não foi visitado

                    # para cada conexão verifica se já foi visitado
                    for j in range(len(visitado)):
                        if visitado[j][0] == novo:
                            if visitado[j][1] <= (atual.nivel+1):
                                flag = False
                            else:
                                visitado[j][1] = atual.nivel+1
                            break

                    # se não foi visitado inclui na fila
                    if flag:
                        l1.insereUltimo(novo, atual.nivel + 1, atual)
                        l2.insereUltimo(novo, atual.nivel + 1, atual)

                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.nivel+1)
                        visitado.append(linha)

                        # verifica se é o objetivo
                        if novo == fim:
                            caminho += l2.exibeCaminho()
                            # print("Árvore de busca:\n",l2.exibeLista())
                            for t in caminho:
                                mapa[t[0]][t[1]] = 2
                    return mapa
    return mapa
