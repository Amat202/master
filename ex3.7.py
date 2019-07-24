
class Animal: 							#superclass
	def __init__(self,name,color):
		self.nm=name
		self.cl=color

class Cat(Animal): 						#subclass
	def purr(self):
		print('Meoooo~~')

class Dog(Animal): 						#subclass
	def bark(self):
		print('Gauuu!')

fido=Dog('Fido','Black')
print(fido.cl)
fido.bark()

class newdog(Dog):
	def bark(self): 					#overwriten
		print('Woof') 	

rito=newdog('rito','Brown')
rito.bark()