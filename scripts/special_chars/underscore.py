from utils import triple_click
    
triple_click(store.get_value, store.set_value, keyboard.send_keys,
    first_contents='u',
    second_contents='<backspace>_',
    third_contents='_',
    timeout=0.2)