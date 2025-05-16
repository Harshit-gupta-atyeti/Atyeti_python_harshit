#local and global
x=10 #global variable
def func():
    y=5 #local variable
    print("inside function x is",x) #accessing global
    print("inside function y is",y)

func()
print("outside function x is",x)
#print("outside function y is",y) #this will cause an error