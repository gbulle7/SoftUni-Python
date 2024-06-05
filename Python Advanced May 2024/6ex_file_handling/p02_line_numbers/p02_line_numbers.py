from string import punctuation

with open('text.txt') as textfile:
    text = textfile.read().split('\n')

with open('output.txt', 'w') as output:
    for i in range(len(text)):
        line = text[i]
        letters_count = len([char for char in line if char.isalpha()])
        punctuation_count = len([char for char in line if char in punctuation])
        output.write(f"Line {i + 1}: {line} ({letters_count})({punctuation_count})\n")


# Method 2
with open('text.txt') as input_file, open('output.txt', 'w') as output_file:
    result = []
    for row, line in enumerate(input_file):
        letters_count = 0
        punct_count = 0

        for ch in line:
            if ch.isalpha():
                letters_count += 1
            elif ch in punctuation:
                punct_count += 1
        result.append(f'{row + 1}: {line.strip()} ({letters_count})({punct_count})')

    output_file.write('\n'.join(result))
