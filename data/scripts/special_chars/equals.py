from utils import double_click

double_click(store.get_value, store.set_value, keyboard.send_keys,
    first_contents='k',
    second_contents='<backspace>=',
    timeout=0.15)