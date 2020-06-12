from utils import quadruple_click, active_class_switch
    
active_class_switch(window.get_active_class, {
    'terminal': lambda: keyboard.send_keys('<shift>+<ctrl>+c'),
    'default': lambda: quadruple_click(
        store.get_value, store.set_value, keyboard.send_keys,
        first_contents='<ctrl>+c',
        second_contents='<ctrl>+<right><ctrl>+<shift>+<left>',
        third_contents='<end><shift>+<home><ctrl>+c',
        fourth_contents='<end><shift>+<home><shift>+<home><ctrl>+c',
        timeout=0.2
    )
})