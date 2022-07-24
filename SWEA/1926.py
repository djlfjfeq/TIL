number = int(input())
t =[3,6,9]
 
for i in range(1, number+1):
    cnt = 0
    n= i
    while(n != 0):
        a= n%10
        n //=10
        if a in t:
            cnt +=1
    if cnt ==0:
        print(f'{i}', end=' ')
    else:
        print('-'*cnt, end=' ')
        
   
   
   