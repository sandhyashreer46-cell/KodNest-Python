# Inbuilt String Methods - Single Program

s = " KodNest Technologies 123 "

print("Original String:", s)

# Case conversion methods
print("upper():", s.upper())          # KODNEST TECHNOLOGIES 123
print("lower():", s.lower())          # kodnest technologies 123
print("capitalize():", s.capitalize()) # Kodnest technologies 123
print("title():", s.title())          # Kodnest Technologies 123
print("swapcase():", s.swapcase())    # kODnEST tECHNOLOGIES 123

# Searching & counting
print("find('Tech'):", s.find("Tech")) # 10
print("count('o'):", s.count("o"))     # 3

# Replace
print("replace('123', '2025'):", s.replace("123", "2025"))

# Start & End check
print("startswith(' Kod'):", s.startswith(" Kod"))   # True
print("endswith('123 '):", s.endswith("123 "))        # True

# Split & Join
words = s.split()

print("split():", words)
print("join():", "--".join(words))
#Replace
print("replace('123','2025')", s.replace("kodnest","2025"))
#start & End check
print("startswith(' kod'):",s.startswith(" kod"))
print("endswith('123 '):",s.endswith("123 "))
# split & Join
words = s.split()
print("split():",words)
print("join():"," ".join(words))
#strip spaces
print("strip():",s.strip())
print("lstrip():",s.lstrip())
print("rstrip():",s.rstrip())

s = "  "
#checking methods
print("isalpha():",s.isalpha())
print("isdigit():",s.isdigit())
print("isspace():",s.isspace())
print("isalnum():",s.isalnum()) #true

#length
print("length of string:",len(s))