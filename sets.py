#Sets are unordered,unindexed and mutable,unchangeable
#Don't Support duplicate values

s = {1,2,3,3,4,5}
#print(s,s[1])
#s[2] = 300 #set are immutable 
s.add(7)
s.update({8,9})
#s.remove(10)
s.discard(10)
s.pop()
s.pop()
s.clear()
del s
# print(type(s),s)

s1 ={1,2,3,"Hello",1.2,True,0,1.2324,1,2,False}
print(s1)

#Constructor
s2 =set()
print(s2,type(s2)) #empty set
s3 = set([1,2,3,4])
print(s3,type(s3))
s.clear
del s
# print(type(s),s)
s1 = {1,2,3,"Hello",1.2,True,0,1.2324,1,2,False}
print(s1)

#constructor of set
s2 = set()
print(s2,type(s2))
s3 = set([1,2,3,4])
print(s3,type(s3))

#loop
for n in s3:
    print(n)
    if n==2:
        break

