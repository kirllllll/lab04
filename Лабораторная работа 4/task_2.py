import json
import csv
# Импортировали необходимые молули

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
# Импортировали необходимые файлы


def task() -> None:
    with open(INPUT_FILENAME) as finp: # Читаем данные из файла
            cdct = [line for line in csv.DictReader(finp)] # Считываем строки и перерабатываем в OrderedDict

    jdct = json.dumps(cdct, indent=4) # Сериализуем данные в json с отступами

    with open(OUTPUT_FILENAME, "w") as fout: # Открываем файл на запись
        fout.write(jdct)

if __name__ == '__main__':
    # Конвертируем с помощью функции
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
