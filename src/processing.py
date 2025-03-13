from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(data_dictionary: List[Dict[str, object]], state: str = 'EXECUTED') -> List[Dict[str, object]]:
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
    print("Выход функции filter_by_state со статусом по умолчанию 'EXECUTED':")
    print(result_default)

    result_canceled = filter_by_state(input_dictionary, 'CANCELED')
    print("\nВыход функции filter_by_state, если статус 'CANCELED':")
    print(result_canceled)


def sort_by_date(data: List[Dict[str, Any]], reverse=True) -> List[Dict[str, Any]]:
    '''Функция возвращает новый список, отсортированный по дате'''

    return sorted(data, key=lambda x: datetime.fromisoformat(x['date']), reverse=reverse)


data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}
]

sorted_data_desc = sort_by_date(data)
print("\nВыход функции sort_by_date:")
for sorted_data in sorted_data_desc:
    print(sorted_data)
