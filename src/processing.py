from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(
        data_dictionary: List[Dict[str, object]],
        state: str = 'EXECUTED',
) -> List[Dict[str, object]]:
    '''Фильтрует список словарей по ключу 'state' и возвращает новый список'''

    filtered_dictionary = []
    for dictionary in data_dictionary:
        if dictionary.get('state') == state:
            filtered_dictionary.append(dictionary)
    return filtered_dictionary


def sort_by_date(
        data: List[Dict[str, Any]],
        reverse: bool = True
) -> List[Dict[str, Any]]:
    '''Функция возвращает новый список, отсортированный по дате'''

    return sorted(data, key=lambda x: datetime.fromisoformat(x['date']), reverse=reverse)
