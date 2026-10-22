c = 30
def add():
    global a
    a = 10
    b = 20
    print(a + b)
    print(c)
add()
print(c)

# print (f "The value of a is {a}")
#print(a + b)

x = 100 # global variable
def display():
    x = 50 
    print("Local x",x)
display()
print("Global x",x)

x  = 10 #global variable
def display():
    print(x)
display()
x = 20
print(x)