# text = input()
# vowels = 'aouei'
#
# output = ''.join([txt for txt in text if not txt.lower() in vowels])
# print(output)

def remove_vowels(txt):
    vowels = 'aouei'
    output = ''.join([char for char in txt if char.lower() not in vowels])
    return output


text = input()
print(remove_vowels(text))
