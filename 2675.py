n=int(input())
while n>0:
    a,b=input().split(' ')
    for i in b:
        print(i*int(a), end='')
    print()
    n-=1