import re

text = 'HeLlOo World'

result = re.findall(r'hello', text)
print(result)                                   # []                        No result; case sensitive
result2 = re.findall(r'hello', text, re.I)
print(result2)                                  # ['HeLlO']                 == re.IGNORECASE; Case insensitive
result3 = re.split(r'l', text)
print(result3)                                  # ['HeL', 'Oo Wor', 'd']    Split in a list
result4 = re.sub(r'o', 'Y', text)
print(result4)                                  # HeLlOY WYrld              Replaced 'o' wih 'Y'
result5 = re.subn(r'o', 'Y', text)
print(result5)                                  # ('HeLlOY WYrld', 2)       Replaced 'o' wih 'Y'; 2 times
