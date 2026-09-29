s1 = "hello"
print(id(s1),s1)

s1 = "hello"+"world"
print(id(s1),s1)

s1 = "hello"
s2 = s1 + "world"
print(id(s1),s1)
print(id(s2),s2)

s1 = "Python"
s2 = "python"
print(id(s1),s1)
print(id(s2),s2)
print(s1==s2)
print(s1 is s2)
#slicing
s1 = "Python"
print(s1) #python
print(s1[0]) #p
print(s1[-1]) #n
print(s1[0:6]) #python
print(s1[0:7]) #python
print(s1[0:10]) #python
print(s1[1:3]) #yt
s1 = "python"
print(s1)
print(s1[2])
print(s1[5])
print(s1[0:3])
print(s1[1:4])
print(s1[2:6])
print(s1[4:8])
print(s1[2:5:2])
print(s1[2:3:1])
print(s1[2:4:1])
print(s1[2:5:2])
print(s1[2:6:1])
print(s1[2:7:2])
