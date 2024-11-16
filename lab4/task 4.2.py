# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = 'input.csv'
OUTPUT_FILENAME = 'output.json'


def csv_to_json(csv_file, delimiter=",", row_delimiter="\n"):
    with open(csv_file, 'r') as file:
       reader = csv.DictReader(file)
       f = [row for row in reader]

    with open(OUTPUT_FILENAME, 'c') as file2:
        json.dump(f, file2, indent = 4)


if __name__ == '__main__':
    # Нужно для проверки
    csv_file = 'input.csv'
    csv_to_json(csv_file, delimiter=",", row_delimiter="\n")

    with open(OUTPUT_FILENAME, 'r') as output_json:
        for line in output_json:
            print(line, end="")
