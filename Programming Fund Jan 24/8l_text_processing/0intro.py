a = 'aSd'
b = a.swapcase()
print(b)                         # AsD
c = a.capitalize()
print(c)                         # Asd
d = a.upper()
print(d)                         # ASD
e = a.lower()
print(e)                         # asd
f = a.find('S')
print(f)                         # 1

txt1 = "I like bananas"
print(txt1.replace("bananas", "apples"))      # I like apples

print(id(txt1))      # Object identity/memory address


# center string with padding
txt2 = "banana"
x = txt2.center(20, "O")
print(x)                           # OOOOOOObananaOOOOOOO
x = txt2.rjust(20, 'O')     # OOOOOOOOOOOOOObanana
print(x)
x = txt2.ljust(20, 'O')     # bananaOOOOOOOOOOOOOO
print(x)

# mapping table for translation
txt3 = "Good night Sam!"
x1 = "mSa"
y1 = "eJo"
z1 = "odnght"
mytable = str.maketrans(x1, y1, z1)
print(txt3.translate(mytable))      # G i Joe!

# same as dictionary
txt4 = "Good night Sam!"
mydict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
print(txt4.translate(mydict))        # G i Joe!
