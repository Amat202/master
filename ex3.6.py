
class Wolf:
	legs = 4
	def __init__(self,name,color):
		self.nm = name
		self.cl = color
	def bark(self):
		print("Gau!")

fido = Wolf("Fido", "brown")
print(fido.nm) 		#[Fido]
fido.bark() 		#[Gau!]

print(fido.legs) 	#[4]
fido.legs = 7
print(fido.legs) 	#[7]
print(Wolf.legs) 	#[4]
Wolf.legs = 6
print(Wolf.legs) 	#[6]