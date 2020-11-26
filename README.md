# Tarea6Dalgo

## Autores:
	Sergio David Sierra Sanmiguel	201914519
	Santiago Tangarife Rincón	201815439
	
Para resolver los tres problemas se crearon archivos con el nombre
parteX.py donde X corresponde al número de cada problema. Los archivos
pueden ser ejecutados en cualquier IDE para python, ya que no están 
dentro de una carpeta de un proyecto de python.

## Parte1.py :
	Al ejecutar el programa se pediran 2 entradas, un número del 1 al 4,
	el cual indica el tipo de algoritmo que se va aprobar; y un archivo 
	a probar, este archivo es el que contiene la matriz que representa el
	grafo (se usa el mismo formato que los archivos adjuntos en el 
	enunciado).
	La salida del programa es un archivo de texto con el mismo formato de
	los archivos de entrada, sin embargo, este contiene el costo minimo 
	para ir de un vertice a otro. Adicionalmente, se imprime en consola el
	timpo que tomo en completarse la ejecución del algoritmo, y el nombre 
	del archivo en el que se encuentra la respuesta.
	El proceso se puede repetir las veces que desee para probar con 
	diferentes matrices.
	
	Tiempos (segundos):
		distances5.txt
			Dijkstra		0.0
			Bellman Ford	0.004
			Floyd Warshall	0.001
		distances100.txt:
			Dijkstra		0.345
			Bellman Ford	48.462
			Floyd Warshall	0.745
		distances1000.txt:
			Dijkstra		346.219
			Bellman Ford	N/A
			Floyd Warshall	797.235
			
## Parte2.py :
	El programa necesita una entrada, una matriz que indica con 1 si un vertice 
	está conectado a otro (se usa el mismo formato que en el enunciado).
	La salida es un archivo de texto llamado BFS en el que se muestra una cadena
	de texto igual a la del enunciado, por ejemplo {{0,2,3},{1,5},{4,6}} para la 
	matriz de ejemplo.
	Al finalizar se puede indicar con Y o N (no es case sensitive) si se desea 
	continuar, para probar otra matriz.
	Para este problema se incluyen 2 archivos de texto para probar el programa. 
	El primero, prueba_p2.txt, en donde está la misma matriz del enunciado. El 
	segundo, prueba_p2_3x3.txt, el cual representa un grafo de 3 vertices, en 
	donde ningún verticeestá conectado con otro, por lo que se espera una respuesta
	de la forma {{0},{1},{2}}.
	
## Parte3.py :
	El programa necesita una entrada, un archivo de texto que contiene una matriz,
	que representa un grafo (El archivo debe tener el mismo formato que el descrito
	en la parte 1 del enunciado). 
	La salida es una respuesta en consola. Se muestra "El grafo tiene ciclos" si el
	grafo contiene al menos un ciclo. De lo contrario se muestra el orden topologico
	de la matriz de la forma [a,b,c].
	Se incluye el archivo prueba_p3_sinCiclos.txt para ver el funcionamiento con un
	grafo que no tiene ciclos. Para ver el funcionamiento con ciclos se puede probar
	con cualquiera de los archivos distances que estaban en el enunciado.
