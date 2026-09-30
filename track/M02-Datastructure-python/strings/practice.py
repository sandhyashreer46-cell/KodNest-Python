#1. Extract first 5 characters

text = "Programming"
print(text[0:5])  # Output: Progr

#2. Extract characters from index 2 to 7

text = "PythonProgramming"
print(text[2:8])  # Output: thonPr

#3. Extract from index 4 to the end

text = "DataScience"
print(text[4:])  # Output: Science

#4. Extract from beginning to index 5

text = "Artificial"
print(text[:5])  # Output: Artif

#5. Extract every second character

text = "ABCDEFGHIJ"
print(text[ :: 2])  # Output: ACEGI

text = "Developer"
print(text[-4:])  # Output: oper

#7. Extract everything except the last 3 characters

text = "Programming"
print(text[ :- 3])  # Output: Programm

#8. Extract characters using two negative indexes

text = "Python"
print(text[-5 :- 2])  # Output: yth

#9. Extract the last 6 characters

text = "FullStackDeveloper"
print(text[-6:])  # Output: eloper

#10. Remove the first 2 and last 2 characters

text = "Welcome"
print(text[2 :- 2])  # Output: lco

text = "DataScience"
print(text[2 :- 2])  # Output: taScien

#12.

text = "PythonProgramming"
print(text[6 :- 3])  # Output: Programm

#13.

text = "FullStackDeveloper"
print(text[4 :- 8])  # Output: StackD

#14.

text = "ABCDEFGHIJKLM"
print(text[2 :- 3:2])  # Output: CEGI

#15.

text = "Programming"
print(text[-8:8])  # Output: gramm

text = "Python"
print(text[ ::- 1])  # Output: nohtyP

#17. Reverse only part of the string

text = "Programming"
print(text[7:2 :- 1])  # Output: mmarg

#18. Reverse using negative indexes

text = "ABCDEFGHIJ"
print(text[-1 :- 6 :- 1])  # Output: JIHGF

#19. Take every second character in reverse

text = "ABCDEFGHIJ"
print(text[ ::- 2])  # Output: JHFDB

#20. Challenge - predict carefully

text = "PythonProgramming"

print(text[12:4 :- 2])  # Output: mroP

#21. What will be printed?

word = "Developer"
print(word[-2 :- 7 :- 1])  # Output: epole

#22. What will be printed?

word = "ABCDEFGHIJK"
print(word[8:2 :- 2])  # Output: IGE

#23. What will be printed?

word = "PythonProgramming"
print(word[-2 :- 12 :- 2])  # Output: nmagr

#24. What will be printed?

word = "ABCDEFGHIJ"
print(word[7 :- 8 :- 1])  # Output: HGFED

#25. What will be printed?

word = "DataScience"
print(word[-1:1 :- 2])  # Output: eniSt