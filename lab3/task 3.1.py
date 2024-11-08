# TODO Напишите функцию для поиска индекса товара
def find_item_index(item_list, find_item):
    for index, item_list in enumerate(item_list):
        if item_list == find_item:
            return index
    return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
find_item = 'груша'
for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
