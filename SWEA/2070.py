result = []

i = int(input())
cnt = 1
for n in range(0, i):
    a,b  = map(int,(input().split(' ')))
    result.append([a,b])
    #print(result)
 
for i in result:
    if i[0] < i[1]:
        print(f'#{cnt} <')  
    if i[0] == i[1]:
        print(f'#{cnt} =')  
    if i[0] > i[1]:
        print(f'#{cnt} >')  
    cnt +=1  



 