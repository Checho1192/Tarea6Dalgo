import time

# Lectura del archivo, se almacena en una matriz de adyacencia de numeros enteros
# -1: No hay arco que conecte los vertices, 0: No hay costo.
def leerArchivo(nombreArchivo):
    with open(nombreArchivo, 'r') as archivo:
        matriz = [[int(num) for num in line.split('\t')] for line in archivo]
    return matriz


# Algoritmo de Dijkstra para encontrar el camino de costos mínimos.
"""
    Retorna una lista de listas. La primera lista son los costos mínimos desde el vertice de origen con respecto a todos los demás 
    vertices en orden, la segunda lista son los predecesores a cada vertice.
"""


def dijkstra(matrix: list) -> list:
    rta = []
    for x in range(len(matrix)):
        distances = []
        seen = []
        for i in range(len(matrix)):
            distances.append(float('inf'))
            seen.append(False)
            if matrix[x][i] != -1:
                distances[i] = matrix[x][i]
        distances[x] = 0
        seen[0] = True
        while not not_seen_all(seen):
            v = min_not_seen(distances, seen)
            seen[v] = True
            if v != -1:
                for i in range(len(distances)):
                    if i != v and matrix[v][i] != -1:
                        if distances[i] > distances[v] + matrix[v][i]:
                            distances[i] = distances[v] + matrix[v][i]
        rta.append(distances)
    return rta


def not_seen_all(seen: list) -> bool:
    for item in seen:
        if item == False:
            return False
    return True


def min_not_seen(distance, seen):
    index = -1
    minimum = float('inf')
    for i in range(len(distance)):
        if not seen[i]:
            if distance[i] < minimum:
                minimum = distance[i]
                index = i
    return index


# Algoritmo de Bellman Ford para encontrar el camino de costos mínimos.
"""
    Retorna una lista con el costo mínimo para llegar a cada vértice desde un vértice de inicio.
"""


def bellmanFord(matrix: list)->list:
    rta = []
    for s in range(len(matrix)):
        df = [float('inf')]*len(matrix)
        df[s] = 0
        for i in range(len(matrix)):
            for u in range(len(matrix)):
                for v in range(len(matrix)):
                    if matrix[u][v] != -1:
                        if df[u] != float('inf') and df[u] + matrix[u][v] < df[v]:
                            df[v] = df[u] + matrix[u][v]
        rta.append(df)
    return rta


# Algoritmo de Floyd-Warshall para encontrar el camino de costos mínimos.

def floydWarshall(matrix: list):
    dist = matrix.copy()
    for k in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if (dist[i][k] + dist[k][j] < dist[i][j]):
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

# Función Principal


def main():
    while True:
        alg = input(
            '\nEscoja el Algoritmo que desea probar (Dijkstra, BellmanFord, FloydWarshall): ')
        archivo = input(
            '\nEscoja el archivo que desea probar: (distances5.txt, distances100.txt, distances1000.txt): ')
        if alg == 'Dijkstra' or alg == 'BellmanFord' or alg == 'FloydWarshall':
            m = leerArchivo(archivo)
            if alg == 'Dijkstra':
                start_time = time.time()
                mcm = dijkstra(m)
                end_time = time.time()
                outD = open("dijkstraOutput.txt",'w')
                for i in range(len(mcm)):
                    for j in range(len(mcm[i])):
                        outD.write(f'{mcm[i][j]}+\t')
                    outD.write('\n')
                print('La matriz de costos minimos para cada par de vertices esta en el archivo dijkstraOutput.txt')
                print(f'El tiempo del algoritmo es de {end_time-start_time}')
            elif alg == 'BellmanFord':
                mcm = bellmanFord(m)
                for i in range(len(mcm)):
                    print(f'{mcm[i]}\n')
            else:
                mcm = floydWarshall(m)
                for i in range(len(mcm)):
                    print(f'{mcm[i]}\n')

        else:
            print(f'El algoritmo {alg} no existe')


# Programa principal
main()
