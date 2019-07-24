from math import *
def ptb2(a,b,c):
    """Giai pt bac 2 ax^2+bx+c=0"""
    if a==0:
        if b==0 and c==0:
            return 'Vo so nghiem.'
        elif b==0 and c!=0:
            return 'Vo nghiem.'
        else :
            return 'x={}'.format(round(-c/b,2))
    else:
        delta=pow(b,2)-4*a*c
        if delta==0:
            return 'x(2)={}'.format(round(-b/(2*a),2))
        elif delta<0:
            return 'vo nghiem.'
        else:
            x1=round((-b-sqrt(delta))/(2*a),2)
            x2=round((-b+sqrt(delta))/(2*a),2)
            return 'x1={}, x2={}'.format(x1,x2)

x=int(input('a='))
y=int(input('b='))
z=int(input('c='))
print('pt ax^2+bx+c=0 co nghiem: {}'.format(ptb2(x,y,z)))