# The else clause is executed when the loop terminates normally (not by a break statement)
# Using the else clause with a for loop
'''
num=[1,2,3,4,5]
for i in num:
    if i == 10:
        break
    print("Found 3")
else:
    print("Not Found 3")
'''
# Using the else clause with a while loop
'''
num=[1,2,3,4,5]
i=0
while i < len(num):
    if num[i] == 10:
        break
    print("Found 3")
    i += 1
else:
    print("Not Found 3")
'''