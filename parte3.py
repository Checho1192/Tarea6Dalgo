def leerArchivo(nombreArchivo):
    with open(nombreArchivo, 'r') as archivo:
        matriz = [[int(num) for num in line.split('\t')] for line in archivo]
    return matriz

def dfs(matrix: list, start: int)->list:
    vertices = [i for i in range(len(matrix))]
    answer = []
    stack = []
    visited = [False]*len(matrix)
    stack.append(start)
    visited[start] = True
    while len(stack)>0:
        next = stack.pop()
        answer.append(vertices[next])
        for i in range(len(vertices)):
            if (matrix[next][i] != -1 or matrix[next][i]!=0) and not visited[i]:
                stack.append(i)
                visited[i] = True
    return answer

m = leerArchivo('distances5.txt')
print(dfs(m, 0))