#for i in range(1,11):
#    print(i, end=' ')
    
#for i in range(1,11,2):
#    print(i, end=' ')

#for i in range(1,51):
#    if i%4==0:
#        print(i, end=' ')

#for i in range(1,11):
#    if i%3!=0:
#        print(i, end=' ')
        
#for i in range(1,8):
#    print(i*i, end=' ')

#for i in range(1,8):
#    if i<5:
#        print(i)
#    else:
#        print(8-i)

#for i in range(1,10):
#    if i<6:
#        print(i*2-1)
#    else:
#        print(19-i*2)

#s=0
#for i in range(1,11):
#    s=s+i
#print(s)

#s=0
#for i in range(1,101):
#    s=s+i
#print(s)

#s=0
#for i in range(1,101):
#    if i%2==1:
#        s=s+i
#print(s)

#s=0
#for i in range(1,101):
#    if i%2==0:
#        s=s+i
#print(s)

#s=0
#for i in range(1,11):
#    s=s+1/i
#print(s)

#a=int(input('a='))
#b=int(input('b='))
#c=int(input('c='))
#if a>b and a>c:
#    print(a)
#elif b>a and b>c:
#    print(b)
#else:
#    print(c)

#max1=100
#for i in range(5):
#    a=int(input('number'))
#    if max1>1:
#        max1=a
#print(max1)

#a=5
#b=8
#a,b=b,a
#print(a)
#print(b)

 
#for n in range(1,101):
#    c=str(n).count('3')+str(n).count('6')+str(n).count('9')
#    if c==0:
#        print(n, end=' ')
#    else:
#        print('짝'*c, end=' ')

#li=[50000,10000,5000,1000,500,100,50,10,5]
#n=int(input('amount='))
#for i in li:
#    m=n//i
#    n=n%i
#    print(i,'---',m)



'''
def ex_while():
    i=2
    j=1
    while i<10:
        while j<10:
            print('{} X {} = {}'.format(i, j, i*j))
            j += 1
        j = 1
        i += 1

def ex_for():
    for i in range(2,10):
        for j in range(1,10):
            print('{} X {} = {}'.format(i, j, i*j))

def ex_break():
    n = 2
    loof = True
    while loof :
        for x in range(1,10):
            print('{} X {} = {}'.format(n,x , n*x))
        n +=1 # 이거 위치가 continue랑 다름
        con=input(str(n)+'단을 출력하시겠습니까?(Y/N) : ')
        if con == 'N':
            break
        for x in range(1,10):
            print('{} X {} = {}'.format(n,x , n*x))
        loof = False
    print('구구단이 종료 되었습니다.')

def ex_continue():
    n = 2
    loof = True
    while loof :
        for x in range(1,10):
            print('{} X {} = {}'.format(n,x , n*x))
        con=input(str(n)+'단을 다시 출력하시겠습니까?(Y/N) : ')
        if con == 'Y':
            continue
        n += 1
        for x in range(1,10):
            print('{} X {} = {}'.format(n,x , n*x))
        loof = False
    print('구구단이 종료 되었습니다.')
ex_break()
'''



