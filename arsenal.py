from graphics import *

class Marca(Polygon):
	def __init__(self, centro):
		r = 15
		ox = centro.getX()
		oy = centro.getY()
		
		p1 = Point(ox, oy)
		p2 = Point(ox+r, oy-r)
		p3 = Point(ox+r, oy)
		p4 = Point(ox, oy+r)
		p5 = Point(ox-r, oy)
		p6 = Point(ox-r, oy-r)
		
		Polygon.__init__(self, p1, p2, p3, p4, p5, p6)
		self.setFill('ForestGreen')
	####
####

class Numero(Text):
	def __init__(self, p, n):
		Text.__init__(self, p, n)
		self.setSize(17)
		if n == 1:
			self.setTextColor('MidnightBlue')
		elif n == 2:
			self.setTextColor('DarkGreen')
		elif n == 3:
			self.setTextColor('DarkOrange')
		elif n == 4:
			self.setTextColor('OrangeRed')
		elif n == 5:
			self.setTextColor('FireBrick')
		else:
			self.setTextColor('FireBrick')
####

class Tapa(Rectangle):
	def __init__(self, tcel, centro):
		p1 = Point(centro.getX() - tcel/2 + 2, centro.getY() - tcel/2 + 2)
		p2 = Point(centro.getX() + tcel/2 - 2, centro.getY() + tcel/2 - 2)
		
		Rectangle.__init__(self, p1, p2)
		self.setFill('Indigo')
		self.setWidth(4)
	
	def pertenece(self, clk):
		pass
####

class Mina(Polygon):
	def __init__(self, centro):
		ox = centro.getX()
		oy = centro.getY()
		rmax = 14
		rmin = 7
		p1 = Point(ox, oy-rmax)
		p2 = Point(ox+rmin, oy-rmin)
		p3 = Point(ox+rmax, oy-rmin)
		p4 = Point(ox+rmin, oy)
		p5 = Point(ox+rmax, oy+rmin)
		p6 = Point(ox+rmin, oy+rmin)
		p7 = Point(ox, oy+rmax)
		p8 = Point(ox-rmin, oy+rmin)
		p9 = Point(ox-rmax, oy+rmin)
		p10 = Point(ox-rmin, oy)
		p11 = Point(ox-rmax, oy-rmin)
		p12 = Point(ox-rmin, oy-rmin)

		Polygon.__init__(self, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12)
		self.setFill('Maroon')
####

class Explosion(Polygon):
	def __init__(self, x, y):
		r1 = 3
		r2 = 10

		p1 = Point(x, y-r1)
		p2 = Point(x+r1, y-r2)
		p3 = Point(x+r1, y-r1)
		p4 = Point(x+r2, y-r1)
		p5 = Point(x+r1, y)
		p6 = Point(x+r2, y+r1)
		p7 = Point(x+r1, y+r1)
		p8 = Point(x+r1, y+r2)
		p9 = Point(x, y+r1)
		p10 = Point(x-r1, y+r2)
		p11 = Point(x-r1, y+r1)
		p12 = Point(x-r2, y+r1)
		p13 = Point(x-r1, y)
		p14 = Point(x-r2, y-r1)
		p15 = Point(x-r1, y-r1)
		p16 = Point(x-r1, y-r2)

		Polygon.__init__(self, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16)
		self.setFill('red')
####

if __name__ == '__main__':
	win = GraphWin('', 300, 100)
	ars = [Mina(Point(20, 25)), Explosion(50, 25), Tapa(40, Point(90, 25)), Numero(Point(130, 25), 1), Numero(Point(150, 25), 2), Numero(Point(170, 25), 3), Numero(Point(190, 25), 4), Numero(Point(210, 25), 5), Numero(Point(230, 25), 6), Numero(Point(250, 25), 7), Marca(Point(25, 60))]
	for o in ars:
		o.draw(win)
	win.getKey()
	win.close()