######## LEYENDA ########
#   $Ca = Conjunto A
#	$Cb = Conjunto B
#	$S = Espacio muestral


def union(Ca, Cb):
	return  list(Ca)+(filter(lambda x: x not in Ca, list(Cb)))
	
def intercepcion(Ca,Cb):
	return filter(lambda x: x in Ca, list(Cb))

def espacio(*conjuntos):
	result = []
	for n in conjuntos:
		result = list(union(result,n))
	return result

def complemento(Ca, S):
	return filter(lambda x: x not in Ca, list(S))

def diferencia(Ca,Cb):
	return filter(lambda x: x not in Cb, list(Ca))
