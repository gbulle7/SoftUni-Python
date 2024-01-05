# string = input()
# string_lower = string.lower()
# count = string_lower.count('sand') + string_lower.count('water') + string_lower.count('fish') + string_lower.count('sun')
# print(count)

# string = input()
# lower_str = string.lower()
# counter = 0
# beach_words = ["sand", "water", "fish", "sun"]
# for word in beach_words:
#     counter += lower_str.count(word)
# print(counter)

string = input()
lower_str = string.lower()
counter = 0
for item in ["sand", "water", "fish", "sun"]:
    if item in lower_str:
        word_count = lower_str.count(item)
        counter += word_count
print(counter)