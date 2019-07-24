while True:
    x=int(input('Nhap x:'))
    print(x,"chan" if x%2==0 else 'le')
    y=input('Nhap tiep ko bro?(y/n) -> ')
    if y=='n':
        break
print('Bye bro.')
