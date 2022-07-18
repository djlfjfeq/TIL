
word = 'banana'

my_dict ={}

for i in word:
    if i not in my_dict:
        my_dict[i] = 1
    
    else:
        my_dict[i] = my_dict[i] + 1
        #my_dict[i] = my_dict.get(i, 0) + 1
        
for i in my_dict:
    print(i, my_dict.get(i))
    