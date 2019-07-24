try:
    while True:
        x=int(input('Nhap x:'))
        dem=0
        for i in range(1,x+1):
            if x%i==0:
                dem=dem+1
        print(x,'la so nto.' if dem==2 else 'ko la so nto.')
        t=['y','n']
        h=input('Tiep ko bro?(y/n) -> ')
        while h not in t:
            print('Sai cu phap. Moi nhap lai (Nhap cho dung dm).')
            h=input('Tiep ko bro?(y/n) -> ')
        if h=='n':
            break
    print('Bye!')
except:
    print('sai cu phap. cut ngay')
