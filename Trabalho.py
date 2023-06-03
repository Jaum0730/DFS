class Grafo:
    def __init__(self):
        self.vertices = {}
        self.d = {}
        self.f = {}
        self.tempo = 0

    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def adicionar_aresta(self, origem, destino):
        if origem in self.vertices and destino in self.vertices:
            self.vertices[origem].append(destino)

    def dfs(self):
        graus_saida = {vertice: len(vizinhos) for vertice, vizinhos in self.vertices.items()}
        ordenados = sorted(self.vertices.keys(), key=lambda x: graus_saida[x], reverse=True)

        for vertice in ordenados:
            if vertice not in self.d:
                self.dfs_visit(vertice)

    def dfs_visit(self, vertice):
        self.tempo += 1
        self.d[vertice] = self.tempo

        for vizinho in self.vertices[vertice]:
            if vizinho not in self.d:
                print(f"Aresta de Árvore: ({vertice}, {vizinho})")
                self.dfs_visit(vizinho)
            elif vizinho in self.f:
                if self.d[vertice] < self.d[vizinho]:
                    print(f"Aresta de Avanço: ({vertice}, {vizinho})")
                else:
                    print(f"Aresta de Cruzamento: ({vertice}, {vizinho})")
            else:
                print(f"Aresta de Retorno: ({vertice}, {vizinho})")

        self.tempo += 1
        self.f[vertice] = self.tempo

    def imprimir_d_f(self):
        print("Valores de d:")
        for vertice, valor in self.d.items():
            print(f"{vertice}: {valor}")

        print("\nValores de f:")
        for vertice, valor in self.f.items():
            print(f"{vertice}: {valor}")


def ler_grafo_de_arquivo(nome_arquivo):
    grafo = Grafo()

    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            vertices = linha.strip().split()
            origem = vertices[0]
            for destino in vertices[1:]:
                grafo.adicionar_vertice(origem)
                grafo.adicionar_vertice(destino)
                grafo.adicionar_aresta(origem, destino)

    return grafo


# Exemplo de uso:
nome_arquivo = "Grafo.txt"
grafo = ler_grafo_de_arquivo(nome_arquivo)

print("Executando o DFS:")
grafo.dfs()

print("\nResultados:")
grafo.imprimir_d_f()
