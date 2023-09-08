# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def find_indexes(lst, min_val, max_val):
    """
    Функция для поиска индексов элементов списка, значения которых находятся в заданном диапазоне
    """
    indexes = []
    for i in range(len(lst)):
        if min_val <= lst[i] <= max_val:
            indexes.append(i)
    return indexes

# пример использования функции
my_list = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
min_value = 3
max_value = 7
result = find_indexes(my_list, min_value, max_value)
print(result)  # выводит [1, 2, 3, 6] 
 
# пример использования функции с другим списком
new_list = [12, 34, 56, 78, 90, 23, 45, 67, 89, 10]
min_value = 30
max_value = 70
result = find_indexes(new_list, min_value, max_value)
print(result)  # выводит [1, 2, 6, 7]
