from utils import active_class_switch, num_click_switch

active_class_switch(window.get_active_class, {
    'terminal': lambda: num_click_switch(
        store.get_value, store.set_value,
        name='new_tab_or_window_terminal',
        functions=[
            lambda: keyboard.send_keys('<shift>+<ctrl>+t'),
            lambda: keyboard.send_keys('<shift>+<ctrl>+n')
        ],
        timeout=0.2
    ),
    'vscode': lambda: num_click_switch(
        store.get_value, store.set_value,
        name='new_tab_or_window_vscode',
        functions=[
            lambda: keyboard.send_keys('<ctrl>+p'),
            lambda: keyboard.send_keys('<shift>+<ctrl>+n')
        ],
        timeout=0.2
    ),
    'default': lambda: num_click_switch(
        store.get_value, store.set_value,
        name='new_tab_or_window_default',
        functions=[
            lambda: keyboard.send_keys('<ctrl>+t'),
            lambda: keyboard.send_keys('<ctrl>+n')
        ],
        timeout=0.15
    )
})

