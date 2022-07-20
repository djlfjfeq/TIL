number = int(input())

a = []
while(number > 0):
    a.append(number)
    number //= 2
a.sort()
for i in a:
    print(i, end=' ')
 