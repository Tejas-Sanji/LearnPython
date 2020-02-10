class Area:
	b=0
	h=0
	def __init__(self,b1,h1):
		print('constructing object')
		self.b=b1
		self.h=h1
	def calc(self):
		print('Area: ',self.b*self.h)
class Square(Area):
	def __init__(self,x):
		self.b=x
		self.h=x
rectang=Area(10,5)
rectang.calc()
sq=Square(10)
sq.calc()