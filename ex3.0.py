
def done_twice(func,x):
	return func(func(x))
def add5(x):
	return x+5
print(done_twice(add5,5))     #[15]

ls=[1,2,3,4]
result=list(map(lambda x:x+5,ls))       #map
print(result)
re2=list(filter(lambda x:x%2==0 ,ls))   #filter
print(re2)