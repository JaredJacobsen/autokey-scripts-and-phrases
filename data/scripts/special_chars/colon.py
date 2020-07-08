from utils import triple_click
    
triple_click(store.get_value, store.set_value, keyboard.send_keys,
    first_contents=';',
    second_contents='<backspace>:',
    third_contents='<backspace>:<enter>',
    timeout=0.2)