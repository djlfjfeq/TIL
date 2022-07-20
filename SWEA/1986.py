result = []

cnt = 1

i = int(input())

for n in range(0, i):
    sum = 0
    a= int(input())
    for i in range(1, a+1):
        if i % 2 == 1:
            sum += i
        else:
            sum -= i
    result.append(sum)    
            
for i in result:
    print(f'#{cnt} {i}')  
    cnt +=1  
