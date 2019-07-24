
num_set={1,2,3,4,5}
word_set=set(['eggs','haha','yolo'])
print(3 in num_set)		#[True]
print('jo' not in word_set)   #[True]

oh_set=set()		#empty set
print(oh_set)
print(word_set)

set1={1,3,5,2,1,4,2,-1}
print(set1)
set1.add(7)
set1.remove(-1)
print(set1)
print(len(set1))

set2={1,2,3,4,5,6}
set3={4,5,6,7,8,9}
print(set2 | set3)
print(set2 & set3)
print(set2 - set3)
print(set2 ^ set3)