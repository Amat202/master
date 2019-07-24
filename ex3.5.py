try:
	class Dog: 								#OOP- Lap trinh huong doi tuong
		def __init__(self,name,color): 		# method
			self.name = name
			self.color = color

	fido = Dog('Fido','Black + White')
	print(fido.color)
	print(fido.age)
except AttributeError:
	print('Loi game.')
finally:
	print('end')