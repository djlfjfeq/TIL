result = []
cnt = 1

i = int(input())

for n in range(0, i):
    h1, m1, h2, m2=map(int,(input().split(' ')))
    a = h1 +h2
    b = m1 + m2
    if a >= 13:
        a -= 12
    if b >=60:
        b -= 60
        a += 1 
    result.append([a,b])
        
for i in result:
    print(f'#{cnt}', end=' ')
    for n in i:
        print(f'{n}', end=" ")
    print('')      
    cnt +=1  
