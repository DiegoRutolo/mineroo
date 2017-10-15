import graphics
import random
from arsenal import *
from time import sleep

tcel = 40	 #tamano de celda
width = tcel*20	 #ancho
height = tcel*20 #alto
ncols = 0	 #numero de columnas
nfils = 0	 #numero de filas
nminas = 0	 #numero de minas colocadas
nmarcas = 0		
densidad = 0.13	 #densidad de minas
muerte = False
vict = False

win = graphics.GraphWin('BarreMinas', width, height)
win.setBackground('Thistle')

#Encuenta el centro
def buscaCentro(a):
	return int(tcel/2)+tcel*a
####

#Inicializacion y mapeado
def setup():
	#Dibuja la cuadricula
	def cuadricula():
		global ncels, nfils, ncols
		for i in range(width):
			if i%tcel == 0:
				lin = graphics.Line(graphics.Point(i, 0), graphics.Point(i, height))
				lin.setFill('black')
				lin.draw(win)
				ncols += 1
			####
		####
		for i in range(height):
			if i%tcel == 0:
				lin = graphics.Line(graphics.Point(0, i), graphics.Point(width, i))
				lin.setFill('black')
				lin.draw(win)
				nfils += 1
			####
		####
		ncels = nfils*ncols
	####

	def marcas():
		global mapaMarca
		mapaMarca = [[None for y in range(nfils)] for x in range(ncols)]
	####

	#Decide si hay mina o no
	def minaOno(p, x, y):
		global nminas
		if random.random() < p:
			return Mina(graphics.Point(buscaCentro(x), buscaCentro(y)))
			nminas += 1
		else:
			return None
	####

	#Generar mapa de minas
	def mapeo(p):
		global mapaMinas
		mapaMinas = [[minaOno(p, x, y) for y in range(nfils)] for x in range(ncols)]
		marcas()
	####

	#Dibuja las minas (o numeros?) en su sitio
	def dibujaMinas():
		for x in range(ncols):
			for y in range(nfils):
				try:
					mapaMinas[x][y].draw(win)
				except:
					pass
	####

	#Coloca las tapas
	def cubrir():
		global mapaTapa
		mapaTapa = [[Tapa(tcel, graphics.Point(buscaCentro(x), buscaCentro(y))) for y in range(nfils)] for x in range(ncols)]
		for x in range(ncols):
				for y in range(nfils):
					mapaTapa[x][y].draw(win)
	####

	#Calcula el numero segun las minas que rodean la casilla
	def queNumero(x, y):
		cont = 0
		for i in range(-1, 2):
			for j in range(-1, 2):
				if((x+i >= 0 and x+i < ncols) and (y+j >= 0 and y+j < nfils)):
					if type(mapaMinas[x+i][y+j]) == Mina:
						cont += 1
		####
		if cont != 0:
			return cont
		else:
			return None
	####

	#Anade el numero a mapaMinas
	def numerar():
		for x in range(ncols):
			for y in range(nfils):
				if not mapaMinas[x][y]:
					mapaMinas[x][y] = Numero(graphics.Point(buscaCentro(x), buscaCentro(y)), queNumero(x, y))
					if not queNumero(x, y):
						mapaMinas[x][y] = None
	####

	cuadricula()
	mapeo(densidad)
	numerar()
	dibujaMinas()
	cubrir()
####

#Encuentra la casilla correspondiente a la coordenada
def cas(p):
	if ncols > nfils:
		fin = ncols
	else:
		fin = nfils
	####
	
	for i in range(fin):
		if i*tcel - p < 0 and (i+1)*tcel - p >= 0:
			return i
	return 0
####

#Destapa las casillas vacias y sus 8 adyacentes
def destapaCosas(x, y):
	sleep(0.003)
	for i in range(-1, 2):
		for j in range(-1, 2):
			if x+i >= 0 and x+i < ncols and y+j >= 0 and y+j < nfils and not mapaMarca[x+i][y+j]:
				try:
					mapaTapa[x+i][y+j].undraw()
					mapaTapa[x+i][y+j] = None
				except:
					pass
	mapaMinas[x][y] = -1
	for i in range(-1, 2):
		for j in range(-1, 2):
			if (x+i >= 0 and x+i < ncols and y+j >= 0 and y+j < nfils) and (not mapaMinas[x+i][y+j]):
				destapaCosas(x+i, y+j)
####

#Abre las casillas dominadas por el numero
def abreNum(x, y):
	n = int(mapaMinas[x][y].getText())
	listaMinas = []
	print(n)
	
	for i in range(n):
		pass
####

def mainLoop():
	global muerte, mapaMarca, vict
	nmarcas = 0
	while not muerte:
		clk = win.getMouse()
		ky = win.checkKey()
		x = cas(clk.getX())
		y = cas(clk.getY())
		print('')
		print(x, y)
		
		#Logica
		if ky:				#al pulsar una tecla
			if ky == 'c':		#la tecla 'c' es para comprobar el campo
				for i, j in range(nfils), range(ncols):
					if not (mapaMarca[i][j] and type(mapaMinas[i][j]) == Mina):
						muerte = True
					else:
						vict = True
			else:				#si se pulsa una tecla que no sea 'c'
				if mapaTapa[x][y]:
					if not mapaMarca[x][y]:
						mapaMarca[x][y] = Marca(graphics.Point(buscaCentro(x), buscaCentro(y)))
						mapaMarca[x][y].draw(win)
					else:
						mapaMarca[x][y].undraw()
						mapaMarca[x][y] = None
		else:
			if mapaMarca[x][y]:
				pass			#no hacer nada al hacer click sobre una marca sin haber pulsado una tecla
			else:
				if mapaTapa[x][y]:
					mapaTapa[x][y].undraw()
					mapaTapa[x][y] = None
					if type(mapaMinas[x][y]) == Mina:
						muerte = True
						print('Muerte')
					elif  mapaMinas[x][y] == None:
						destapaCosas(x, y)
				else:
					if type(mapaMinas[x][y]) == Numero:
						abreNum(x, y)
		vict = True
		for x in range(ncols):
			for y in range(nfils):
				if mapaTapa[x][y]:
					if type(mapaMinas[x][y]) != Mina:
						vict = False
		if vict:
			break
####

setup()
mainLoop()

if muerte:
	win2 = graphics.GraphWin('PERDISTE', 200, 100)
	win2.setBackground('black')
	moriste = graphics.Text(graphics.Point(100, 25), 'PERDISTE')
	moriste.setTextColor('PaleTurquoise')
	moriste.setSize(30)
	txt = graphics.Text(graphics.Point(100, 80), 'Cualquier tecla: Salir')
	txt.setTextColor('PaleTurquoise')
	moriste.draw(win2)
	txt.draw(win2)
	k = win2.getKey()
elif vict:
	win3 = graphics.GraphWin('GANASTE', 200, 100)
	win3.setBackground('black')
	moriste = graphics.Text(graphics.Point(100, 25), 'GANSTE')
	moriste.setTextColor('LawnGreen')
	moriste.setSize(30)
	txt = graphics.Text(graphics.Point(100, 80), 'Cualquier tecla: Salir')
	txt.setTextColor('LawnGreen')
	moriste.draw(win3)
	txt.draw(win3)
	k = win3.getKey()
####
win.close()
stats.close()
