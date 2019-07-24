
def cd(): 			#cd() ~ generator
	i=5
	while i>0:
		yield i
		i -=1
for i in cd():
	print(i)

def chan(x):
	for i in range(x):
		if i % 2 == 0 :
			yield i
print(list(chan(11)))
