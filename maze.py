def find_path(labirinto, inicio, fim):
    def dfs(caminho_atual):
        x, y = caminho_atual[-1]

        if (x, y) == fim:
            return caminho_atual

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            novo_x, novo_y = x + dx, y + dy

            if 0 <= novo_x < len(labirinto) and 0 <= novo_y < len(labirinto[0]) and labirinto[novo_x][novo_y] == 0 and (novo_x, novo_y) not in caminho_atual:
                novo_caminho = caminho_atual + [(novo_x, novo_y)]
                resultado = dfs(novo_caminho)

                if resultado:
                    return resultado

    caminho = dfs([inicio])

    if caminho:
        print("Caminho encontrado:")
        for x, y in caminho:
            labirinto[x][y] = 2  # Marque o caminho no labirinto com 2
            print(f"({x}, {y})")
    else:
        print("Não foi possível encontrar um caminho.")

    return labirinto