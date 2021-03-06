from utils import num_click_switch, get_win_title_from_id, active_class_switch
    

def chrome_function():
    num_click_switch(
        store.get_value, store.set_value,
        name='double_omnibox',
        functions=[
            lambda: keyboard.send_keys('<ctrl>+l<ctrl>+c<ctrl>+c<ctrl>+c<ctrl>+c<ctrl>+c<ctrl>+c<ctrl>+c'),
            lambda: keyboard.send_keys('<ctrl>+l<ctrl>+l<ctrl>+l<ctrl>+c<ctrl>+c<ctrl>+c<ctrl>+c<ctrl>+chttps://via.hypothes.is/<backspace><ctrl>+v<enter>')
        ],
        timeout=0.18
    )
    
def vscode_function():
    num_click_switch(
        store.get_value, store.set_value,
        name='double_code_fold',
        functions=[
            lambda: keyboard.send_keys('<ctrl>+k<ctrl>+l'),
            lambda: keyboard.send_keys('<ctrl>+k<ctrl>+]'),
            lambda: keyboard.send_keys('<ctrl>+k<ctrl>+[')
        ],
        timeout=0.18
    )
    
active_class_switch(window.get_active_class, {
    'chrome': chrome_function,
    'vscode': vscode_function
})