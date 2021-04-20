n=int(input())
for i in range(n):
    ox=input()
    cnt=0
    ans=0
    for j in range(len(ox)):
        if ox[j]=='O' :
           cnt+=1
        else :
            cnt=0
        ans+=cnt
    print(ans)
