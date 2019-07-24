def pr(a):
	print(a) 
	#return tra ve ket qua,ko co return chi thuc hien cau lenh

pr('Hello world.')

g=5 				#global variable
def increment():
	g=2				#local variable
	g+=1
increment()
print(g)			# 5

def increment2():
	global g 		# nhan global variable
	g=2				
	g+=1
increment2()
print(g)            #3