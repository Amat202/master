def dec(fun):
	def wrap():
		print('yareyareyare')
		fun()
		print('yareyareyare')
	return wrap
@dec
def pr():
	print('"Jotaro"')
def pr2():
	print('ararara')
pr()                        #run de xem ket qua
pr2()                       #run