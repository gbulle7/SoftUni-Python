count = int(input())
synonyms = {}

for index in range(count):
    word = input()
    synonym = input()
    if word in synonyms:
        synonyms[word].append(synonym)
    else:
        synonyms[word] = [synonym]
    # if word not in synonyms:
    #     synonyms[word] = []
    # synonyms[word].append(synonym)

for word, synonym in synonyms.items():
    print(f"{word} - {', '.join(synonym)}")

# for word in synonyms:
#     print(f"{word} - {', '.join(synonyms[word])}")

# for word, synonym in word_synonyms.items():
#     print(f"{word} - ", end="")
#     print(*synonym, sep=", ")