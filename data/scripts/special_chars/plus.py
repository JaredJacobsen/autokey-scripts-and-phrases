from utils import double_click

double_click(store.get_value, store.set_value, keyboard.send_keys,
    first_contents='h',
    second_contents='<backspace><shift>+=',
    timeout=0.15)