from src.masks import get_mask_card_number, get_mask_account
# импорт функций из модуля masks.py


user_nimber = input()

def mask_account_card (user_nimber: str) -> str:
    '''Функция, которая умеет обрабатывать информацию как о картах, так и о счетах'''

    if user_nimber.startswith('Счёт '):
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

print(mask_account_card(user_nimber))


