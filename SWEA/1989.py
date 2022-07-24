result = []
cnt = 1

i = int(input())

for n in range(0, i):
    s = input()
    a = ''
    for i in s:
        a = i + a
    if a == s:
        result.append(1)
    else:
        result.append(0)
        
for i in result:
    print(f'#{cnt} {i}')  
    cnt +=1  



 