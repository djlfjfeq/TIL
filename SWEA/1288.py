result = []
cnt = 1

i = int(input())
for n in range(0, i):
    a = int(input())
    t =[]
    s = 1
    while 1: 
        c = a*s
        while c!=0:
            b = c%10
            if b not in t:
                t.append(b)
            c = c//10
           
        if len(t) == 10:
            result.append(a*s)
            break
        else:
            s +=1 
    
for i in result:
    print(f'#{cnt} {i}')  
    cnt +=1  

