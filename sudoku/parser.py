import re

def parser(filename):
    with open(filename) as f:
        text = f.read()
    text = re.sub('\D', '', text)
    numbers = list(map(int, text))
    return [numbers[i:i+9] for i in range(0, len(numbers), 9)]
