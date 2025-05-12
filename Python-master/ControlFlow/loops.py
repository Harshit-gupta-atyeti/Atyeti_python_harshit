# The for loop is used to iterate over a sequence (list, tuple, dictionary, set, or string).
'''
num=[10,20,30,40,50]
for i in num:
    print(i)
'''
# The nested for loop is used to iterate over a sequence within another sequence.

num=[[10,20,30],[40,50,60],[70,80,90]]
for i in num:
    for j in i:
        print(j)


# The while loop is used to execute a block of code as long as the condition is true.
'''
num=[10,20,30,40,50]
i=0
while i < len(num):
    print(num[i])
    i += 1 
'''