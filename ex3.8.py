
class Human:
	def __init__(self,name,size):
		self.name=name
		self.size=size
	def present(self):
		print('{}: {} cm'.format(self.name,self.size))

class Worker(Human):
	def __init__(self,name,size,job):
		super().__init__(name,size)
		self.job=job
	def present(self):
		super().present()
		print(self.job)

w=Worker('John',35,'trader')
w.present()