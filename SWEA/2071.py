result = []
cnt = 1

i = int(input())

for n in range(0, i):
        a,b,c,d,e,f,g,h,i,j=map(int,(input().split(' ')))
        temp = [a,b,c,d,e,f,g,h,i,j] 
        result.append(temp)
         
for i in result:
    sum = 0
    for n in i:
        sum += int(n)
    print(f'#{cnt} {sum}')  
    cnt +=1  

