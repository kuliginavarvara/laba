# TODO Напишите функцию для поиска индекса товара
def find_index(listitems, item_to_find):
    if item_to_find in listitems:
        return listitems.index(item_to_find)
    else:
        None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")


