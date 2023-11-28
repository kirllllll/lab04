import json # Импортировали необходимый модуль

finp = 'input.json' # Импортировали необходимый файл

def task() -> float:
    with open(finp) as dct: # Читаем данные из файла
        jdct = json.load(dct) # Сериализуем в python объект

        summ = sum([value["score"] * value["weight"] for value in jdct]) # Через list comprehension считаю значения и упускаю ключи

    return round(summ, 3) # Возвращаем округленный ответ

print(task())
