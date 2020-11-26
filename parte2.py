import time


# Lectura del archivo, se almacena en una matriz de adyacencia de numeros enteros
def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        matriz = [[int(num) for num in line.split('\t')] for line in archivo]
    return matriz


# Copia una matriz en una nueva reemplazando los -1 por infinito

def copy_matrix(matrix: list) -> list:
    dist = []
    for i in range(len(matrix)):
        r = []
        for j in range(len(matrix)):
            if matrix[i][j] == -1:
                r.append(float('inf'))
            else:
                r.append(matrix[i][j])
        dist.append(r)
    return dist


# busca los vertices conectados

def bfs(matrix: list) -> list:
    copied = copy_matrix(matrix)
    response = []

    for i in range(len(copied)):
        actual = connected_vertices(copied, i)
        for n in range(len(actual)):
            merge_non_repeated(actual, connected_vertices(copied, actual[n]))
        actual.sort()
        if not(actual in response):
            response.append(actual)
    return response


# da una lista con los vertices conectados al vertice initial, solo devuelve el inicial si no hay ninguno

def connected_vertices(matrix: list, initial: int) -> list:
    row = copy_matrix(matrix)
    response = [initial]
    for j in range(len(row)):
        if row[initial][j] == 1:
            response.append(j)
    return response


# Pone los elementos de b en a si no se encuentran en a
def merge_non_repeated(a: list, b: list):
    for i in range(len(b)):
        if not(b[i] in a):
            a.append(b[i])


# Función Principal

def main():
    print("\n================== Encontrar componentes conectados en un grafo no dirigido (BFS) ==================")
    continuar = True
    opcion = 'y'
    i = 0
    while continuar:
        if i > 0:
            opcion = input("\n\n¿Continuar? [Y/N]")
        if opcion.lower() == 'y':
            archivo = input('\nEscoja el archivo que desea probar: ')
            m = leer_archivo(archivo)
            start_time = time.time()
            mcm = bfs(m)
            end_time = time.time()
            print(f'El tiempo del algoritmo es de {end_time-start_time}')
            escribir_archivo(mcm, 'BFSOuput.txt')
            print(
                'La lista de vertices que conforman componentes conectados esta en el archivo BFSOuput.txt')
            i += 1
        elif opcion.lower() == 'n':
            continuar = False
        else:
            print("Seleccione una opcion valida.")

# Funcion auxiliar para escribir matriz de costos minimos


def escribir_archivo(mcm: list, name: str) -> None:
    out = open(name, 'w')
    out.write('{ ')
    for i in range(len(mcm)):
        out.write('{')
        for j in range(len(mcm[i])):
            if j < len(mcm[i])-1:
                out.write(str(mcm[i][j])+',')
            elif j == len(mcm[i])-1:
                out.write(str(mcm[i][j]))
        if i < len(mcm)-1:
            out.write('} , ')
        elif i == len(mcm)-1:
            out.write('}')
    out.write(' }')
    out.close()


# Programa principal
main()
