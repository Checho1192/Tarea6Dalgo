import time


def leerArchivo(nombreArchivo: str) -> list:
    archivo = open(nombreArchivo, 'r')
    matrix = []
    for line in archivo:
        r = []
        for num in line.split("\t"):
            if num != '\n':
                r.append(int(num))
        matrix.append(r)
    archivo.close()
    return matrix


def convert(a: list) -> list:
    adjList = []
    for i in range(len(a)):
        r = []
        for j in range(len(a[i])):

            if a[i][j] != 0 and a[i][j] != -1:
                a[i][j] = 1
            else:
                a[i][j] = 0
            if a[i][j] != 0:
                r.append(j)
        adjList.append(r)
    return adjList


def isCylic(adjList: list) -> bool:
    visited = [False]*len(adjList)
    flag = False
    for i in range(len(adjList)):
        visited[i] = True
        for j in range(len(adjList[i])):
            flag = isCylic_util(adjList, visited, adjList[i][j])
            if flag == True:
                return True
        visited[i] = False
    return False


def isCylic_util(adjList: list, visited: list, curr: int) -> bool:
    if visited[curr] == True:
        return True
    visited[curr] = True
    flag = False
    for i in range(len(adjList[curr])):
        flag = isCylic_util(adjList, visited, adjList[curr][i])
        if flag == True:
            return True
    visited[curr] = False
    return False


def topologicalSort(graph: list) -> list:
    visited = [False]*len(graph)
    result = []

    def dfs(node):
        if visited[node]:
            return
        visited[node] = True
        for adj in graph[node]:
            dfs(adj)
        result.append(node)
    for i in range(len(graph)):
        dfs(i)
    return result


def main() -> None:
    print("\n================== Encontrar ciclos en un grafo dirigido (DFS) ==================")
    continuar = True
    opcion = 'y'
    i = 0
    while continuar:
        if i > 0:
            opcion = input("\n\n¿Continuar? [Y/N]")
        if opcion.lower() == 'y':
            archivo = input('\nEscoja el archivo que desea probar: ')
            m = leerArchivo(archivo)
            adj = convert(m)
            start_time = time.time()
            rta = isCylic(adj)
            if rta == False:
                topolo = topologicalSort(adj)
                topolo.reverse()
                print(
                    f'El orden topologico del grafo sin ciclos es de {topolo}')
            else:
                print("El grafo tiene ciclos ")
            end_time = time.time()
            print(f'El tiempo del algoritmo es de {end_time-start_time}')
            i += 1
        elif opcion.lower() == 'n':
            continuar = False
        else:
            print("Seleccione una opcion valida.")


main()
