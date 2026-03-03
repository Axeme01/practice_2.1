with open('text.txt', 'w', encoding='utf-8') as file:

    lines = [
        "First line",
        "Second line",
        "third line",
        "fourth line",
        "fifth line",
    ]
    for line in lines:
        file.write(line + '\n')

with open('text.txt', 'r') as file:
    content = file.readlines()

    num_lines = len(content)
    word_count = sum(len(line.split()) for line in content)
    longest_line = max(content, key=len).strip()

print(f'Количество строк: {num_lines}')
print(f'Количество слов: {word_count}')
print(f'Самая длинная строка:\n"{longest_line}"')