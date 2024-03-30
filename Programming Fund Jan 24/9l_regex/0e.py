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


text2 = '@something@ @something# #something#'
pattern1 = r'(([@#$])\w+\2)'        # \2 group backreference uses most recently matched symbol in group 2 (inner group)
match1 = re.findall(pattern1, text2)
print(match1)
pattern2 = r'(([@#$])\w+([@#$]))'
match2 = re.findall(pattern2, text2)
print(match2)
