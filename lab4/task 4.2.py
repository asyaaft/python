# TODO импортировать необходимые молули
INPUT_FILENAME = 'input.csv'
OUTPUT_FILENAME = 'output.json'

import csv
import json


def csv_to_json(csv_file, delimiter=",", row_delimiter="\n"):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file, delimiter=delimiter)
        data = []
        for row in reader:
            data.append(row)

    json_string = json.dumps(data, indent=4)
    return json_string


csv_file = "input.csv"
json_data = csv_to_json(csv_file)
print(json_data)

if __name__ == '__main__':
    # Нужно для проверки
    csv_to_json(csv_file, delimiter=",", row_delimiter="\n")
    with open(OUTPUT_FILENAME) as output_json:
        for line in output_json:
            print(line, end="")
