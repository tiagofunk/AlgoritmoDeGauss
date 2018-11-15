def ler(arquivo):
	ordem = -1
	matriz = []

	arq = open(arquivo)

	texto = arq.readlines()

	ordem = int( texto[0] )

	for i in range( 0, len( texto ) ) :
		if i != 0:
			numeros = texto[i].split(" ")
			tamanho = len( numeros )
			matriz.append( [] )
			for j in range( 0, tamanho ):
				matriz[i-1].append( int( numeros[j] ) )

	arq.close()
	
	return matriz

def calcular( sistema ):
	n = len( sistema ) - 1
	m = 0
	soma = 0
	aux = 0
	
	for i in range( 0, n ):
		if sistema[i][i] == 0 and i != n :
			for j in range( i, n+1 ):
				if sistem[j][i] != 0 and j != i:
					for k in range( 0, n+2 ):
						aux = sistema[i][k]
						sistema[i][k] = sistema[j][k]
						sistema[j][k] = aux
					break
		
		for j in range( i+1, n+1 ):
			m = -1.0 * (sistema[j][i] / sistema[i][i])
			for k in range( 0, n+2 ):
				sistema[j][k] = sistema[j][k] + m * sistema[i][k]
	
	respostas = []
	for i in range( 0, n+1 ):
		respostas.append( 0 )
	
	respostas[ n ] = sistema[n][n+1] / sistema[n][n]
	for i in range( n-1, -1, -1 ):
		soma = 0
		for j in range( i+1, n+1 ):
			soma += sistema[i][j] * respostas[j]
			respostas[i] = (sistema[i][j + 1] - soma) / sistema[i][i]
	
	return respostas

import sys
import time

tempoInicialLeitura = time.time()
matriz = ler( sys.argv[1] )
tempoFinalLeitura = time.time()

print(tempoInicialLeitura)
print(tempoFinalLeitura)
print( (tempoFinalLeitura-tempoInicialLeitura) * 1000.0 )

respostas = calcular( matriz )

for n in respostas:
	print( "{}  ".format(round(n,4)), end="" )

print()
