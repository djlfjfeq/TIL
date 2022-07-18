numbers = [0, 20, 100, 40]

max = numbers[0]
second_num = numbers[0]

for n in numbers:
    if(max<n):
        second_num = max
        max = n
        
    elif second_num < n and n < max:
        second_num = n 
print(second_num)

