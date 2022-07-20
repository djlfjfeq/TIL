result = []

i = int(input())
cnt = 1
a=0
b=0
for n in range(0, i):
        p,q,r,s,w=map(int,(input().split(' ')))
        a= p*w
        if r>w:
            b=q
        else:
            b=q + ((w-r)*s)
        if a<b:
            result.append(a)
        else:
            result.append(b)
                     
for i in result:
        print(f'#{cnt} {i}')  
        cnt +=1  
        
    