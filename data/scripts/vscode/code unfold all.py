from utils import num_click_switch

num_click_switch(
    store.get_value, store.set_value,
    name='double_code_fold',
    functions=[
        lambda: keyboard.send_keys('<ctrl>+k<ctrl>+0'),
        lambda: keyboard.send_keys('<ctrl>+k<ctrl>+j')
    ],
    timeout=0.18
)