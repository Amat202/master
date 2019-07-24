
def handle(f,x):
	return f(x)
	#Tai day, chi con x la doi so, f tro thanh 1 ham
re1=handle(lambda y:y%2==0,6)  
#lambda khai bao ham trong doi so cua ham khac ,x hay y deu dc
print(re1) 								#[True]
def chanle(x):	
	if x%2==0:
		return "Chan"
	else:
		return "Le"
print(handle(chanle,5)) 				#[Le]
print(handle(lambda x:chanle(x),5))		#[Le]