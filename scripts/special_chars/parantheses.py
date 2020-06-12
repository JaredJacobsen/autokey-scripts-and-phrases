from utils import triple_click, quadruple_click

language_context = store.get_global_value('language_context')
    
if language_context == 'python':
    quadruple_click(store.get_value, store.set_value, keyboard.send_keys,
        first_contents='j',
        second_contents='<backspace>()<left>',
        third_contents='<right><backspace><backspace>()',
        fourth_contents='<backspace><backspace>():<enter>',
        timeout=0.2)

elif language_context == 'javascript':
    quadruple_click(store.get_value, store.set_value, keyboard.send_keys,
        first_contents='j',
        second_contents='<backspace>()<left>',
        third_contents='<right><backspace><backspace>()',
        fourth_contents='<backspace><backspace>() => {<enter>',
        timeout=0.2)


else:
    triple_click(store.get_value, store.set_value, keyboard.send_keys,
        first_contents='j',
        second_contents='<backspace>()<left>',
        third_contents='<right><backspace><backspace>()', timeout=0.2)

