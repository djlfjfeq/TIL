result = []

i = int(input())
cnt = 1
for n in range(0, i):
    a,b  = map(int,(input().split(' ')))
    result.append([a,b])
    #print(result)
 
for i in result:
    print(f'#{cnt} {(int(i[0]) // int(i[1]))} {int(i[0]) % int(i[1])}')  
    cnt +=1  



 