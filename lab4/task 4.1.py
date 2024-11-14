# TODO решите задачу
import json


def total(json_file):
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Файл не найден.")
        return None

    total_score = 0
    for item in data:
        if "score" in item and "weight" in item:
            total_score += item["score"] * item["weight"]
    return round(total_score, 3)


json_file = 'input.json'  # Замените 'data.json' на ваш файл
result = total(json_file)

if result is not None:
    print(result)
