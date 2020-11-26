from collections import defaultdict


def leerArchivo(nombreArchivo):
    with open(nombreArchivo, 'r') as archivo:
        matriz = [[int(num) for num in line.split('\t')] for line in archivo]
    return matriz


def convert(a):
    adjList = defaultdict(list)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] != 0 and a[i][j] != -1:
                adjList[i].append(j)
    return adjList


def isCylic(adjList) -> bool:
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


def isCylic_util(adjList, visited, curr):
    if visited[curr] == True:
        return True
    visited[curr] = True
    flag = False
    for i in range(len(adjList[curr])):
        flag = isCylic_util(adjList, visited, adjList[curr][i])
        if flag == True:
            return True
    return False


#m = leerArchivo('distances5.txt')

m = [[0, 1,	1, -1, -1],[-1, 0, -1, 1,	-1],[-1, -1, 0, 1,	-1],[-1, -1, -1, 0,	1],[-1, -1, 1, -1, 0]]
adjList = convert(m)
print(isCylic(adjList))