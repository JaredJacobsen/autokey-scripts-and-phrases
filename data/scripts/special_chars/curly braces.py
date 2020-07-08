from utils import triple_click
    
triple_click(store.get_value, store.set_value, keyboard.send_keys,
    first_contents='i',
    second_contents='<backspace>{}<left>',
    third_contents='<right><backspace><backspace>{<enter>',
    timeout=0.2)