from utils import num_click_switch

num_click_switch(
    store.get_value, store.set_value,
    name='show_notifications',
    functions=[
        lambda: keyboard.send_keys('<ctrl>+<shift>+<super>+2'),
        lambda: keyboard.send_keys('<ctrl>+<shift>+<super>+1')
    ],
    timeout=0.18
)