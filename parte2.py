# Lectura del archivo, se almacena en una matriz de adyacencia de numeros enteros
def leerArchivo(nombreArchivo):
    with open(nombreArchivo, 'r') as archivo:
        matriz = [[int(num) for num in line.split('\t')] for line in archivo]
    return matriz

# Algoritmo de Breadth First Search 
def bfs(matrix: list)->list:
    answer = []
    
    return answer