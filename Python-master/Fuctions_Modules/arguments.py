#positional arguments
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet("john cena",45) # john cena goes to name and 45 goes to age

#keyword arguments
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")
greet(age=45, name="john cena") # order does not matter in keyword arguments

#default arguments
def greet(name,age=30):
    print(f"Hello {name}, you are {age} years old.")

greet("john cena")  #uses default age=30
greet("john cena",45) #overrides default

# *args
def print_num(*single):
    for num in single:
        print(num)
print_num(1,2,3,4,5) #allows any number of arguments

#**kwargs
def print_info(**two):
    for key,value in two.items():
        print(f"{key}:{value}")
print_info(name='john cena',age=45) #allow any number of keyword argument