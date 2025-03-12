def filter_by_state(data_dictionary, state='EXECUTED'):
    '''Фильтрует список словарей по ключу 'state' и возвращает новый список'''

    filtered_dictionary = []
    for dictionary in data_dictionary:
        if dictionary.get('state') == state:
            filtered_dictionary.append(dictionary)
    return filtered_dictionary

if __name__ == "__main__":
    input_dictionary = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    ]

    result_default = filter_by_state(input_dictionary)
    print("Выход функции со статусом по умолчанию 'EXECUTED':")
    print(result_default)

    result_canceled = filter_by_state(input_dictionary, 'CANCELED')
    print("\nВыход функции, если вторым аргументом передано 'CANCELED':")
    print(result_canceled)