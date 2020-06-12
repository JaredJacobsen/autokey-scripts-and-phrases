from utils import active_class_switch, num_click_switch, close_window

active_class_switch(window.get_active_class, {
    'terminal': lambda: num_click_switch(
        store.get_value, store.set_value,
        name='close_tab_or_window_terminal',
        functions=[
            lambda: keyboard.send_keys('<shift>+<ctrl>+w'),
            close_window
        ],
        timeout=0.15
    ),
    'default': lambda: num_click_switch(
        store.get_value, store.set_value,
        name='close_tab_or_window',
        functions=[
            lambda: keyboard.send_keys('<ctrl>+w'),
            lambda: close_window(system.exec_command)
        ],
        timeout=0.1
    )
})
