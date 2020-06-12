import time
from utils import num_click_switch

contents = clipboard.get_selection()
time.sleep(0.1)

num_click_switch(
    store.get_value, store.set_value,
    name='wrap_content',
    functions=[
        lambda: keyboard.send_keys('<backspace>({0})'.format(contents)),
        lambda: keyboard.send_keys('<backspace>{{{0}}}'.format(contents))
    ],
    timeout=0.14
)