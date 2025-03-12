from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number

user_nimber = input('Введите номер карты или номер счета: ')
date_string = input('Введите дату: ')


def mask_account_card(user_nimber: str) -> str:
    '''Функция, которая умеет обрабатывать информацию как о картах, так и о счетах'''

    if user_nimber.startswith('Счет ') or user_nimber.startswith('Счёт '):
        section = user_nimber.split(' ', 1)
        account_number = section[1]
        masked_number = get_mask_account(account_number)
        return f"{section[0]} {masked_number}"
    else:
        section = user_nimber.rsplit(" ", 1)
        card_name = section[0]
        card_number = section[1]
        masked_card = get_mask_card_number(card_number)
        return f"{card_name} {masked_card}"


def get_date(date_str: str) -> str:
    '''Функция, которая меняет формат даты'''

    date_obj = datetime.fromisoformat(date_str)
    formatted_date = date_obj.strftime("%d.%m.%Y")
    return formatted_date


print(mask_account_card(user_nimber))
print(get_date(date_string))
