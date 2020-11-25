import time

# Lectura del archivo, se almacena en una matriz de adyacencia de numeros enteros


def leerArchivo(nombreArchivo):
    with open(nombreArchivo, 'r') as archivo:
        matriz = [[int(num) for num in line.split('\t')] for line in archivo]
    return matriz

# Algoritmo de Dijkstra para encontrar el camino de costos mínimos.


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

def bellmanFord(matrix: list) -> list:
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

def floydWarshall(matrix: list) -> list:
    dist = matrix.copy()
    for k in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if (dist[i][k] + dist[k][j] < dist[i][j]):
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

# Función Principal


def main():
    continuar = True
    while continuar:
        print("\n/////////////// Algoritmos de caminos de costos minimos para cualquier par de vertices //////////////")
        print("\nPara probar Dijkstra escriba 1")
        print("\nPara probar Bellman Ford escriba 2")
        print("\nPara probar Floyd-Warshall escriba 3")
        print("\nSi desea salir presione 4")
        opcion = input("\n\nSeleccione el algoritmo a probar: ")
        archivo = input('\nEscoja el archivo que desea probar: ')
        if opcion == '1':
            m = leerArchivo(archivo)
            start_time = time.time()
            mcm = dijkstra(m)
            end_time = time.time()
            print(f'El tiempo del algoritmo es de {end_time-start_time}')
            escribirArchivo(mcm, 'dijkstraOutput.txt')
            print(
                'La matriz de costos minimos para cada par de vertices esta en el archivo dijkstraOutput.txt')
        elif opcion == '2':
            m = leerArchivo(archivo)
            start_time = time.time()
            mcm = bellmanFord(m)
            end_time = time.time()
            print(f'El tiempo del algoritmo es de {end_time-start_time}')
            escribirArchivo(mcm, 'bellmanFordOutput.txt')
            print(
                'La matriz de costos minimos para cada par de vertices esta en el archivo bellmanFordOutput.txt')
        elif opcion == '3':
            m = leerArchivo(archivo)
            start_time = time.time()
            mcm = floydWarshall(m)
            end_time = time.time()
            print(f'El tiempo del algoritmo es de {end_time-start_time}')
            escribirArchivo(mcm, 'floydWarshallOutput.txt')
            print(
                'La matriz de costos minimos para cada par de vertices esta en el archivo floydWarshallOutput.txt')
        elif opcion == '4':
            continuar = False
        else:
            print("Seleccione una opcion valida.")

# Funcion auxiliar para escribir matriz de costos minimos


def escribirArchivo(mcm: list, name: str) -> None:
    out = open(name, 'w')
    for i in range(len(mcm)):
        for j in range(len(mcm[i])):
            out.write(str(mcm[i][j])+'\t')
        out.write('\n')
    out.close()


# Programa principal
main()
