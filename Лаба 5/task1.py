# TODO решите задачу
import json


def task(input_file: str) -> float:
    file = open(input_file, 'r')
    data = json.load(file)

    total = 0
    for item in data:
        total += item.get('score', 0) * item.get('weight', 1)
    return round(total, 3)

input_file = 'input.json'
print(task(input_file))
