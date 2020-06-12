from utils import active_class_switch
    
active_class_switch(window.get_active_class, {
    'terminal': lambda: keyboard.send_keys('<shift>+<ctrl>+v'),
    'default': lambda: keyboard.send_keys('<ctrl>+v')
})