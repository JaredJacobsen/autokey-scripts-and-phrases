from utils import active_class_switch 
    
active_class_switch(window.get_active_class, {
    'roam': lambda: keyboard.send_keys('<ctrl>+u'),
    'keep': lambda: keyboard.send_keys('/'),
    'default': lambda: keyboard.send_keys('<ctrl>+f')
})