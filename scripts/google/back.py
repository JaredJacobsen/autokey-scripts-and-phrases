from utils import active_class_switch, num_click_switch
      
num_click_switch(
    store.get_value, store.set_value,
    name='chrome_back',
    functions=[
        lambda: keyboard.send_keys('<alt>+<left>'),
        lambda: keyboard.send_keys('<alt>+<right>')
    ],
    timeout=0.15
)