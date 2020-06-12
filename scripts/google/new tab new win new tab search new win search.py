#open new window, search highlighted text in new tab, search highlighted text in new win

import time
from utils import num_click_switch, get_win_title_from_id

def new_tab():
    active_class = window.get_active_class()

    if 'oogle-chrome' in active_class:
        keyboard.send_keys('<ctrl>+t')
        time.sleep(0.01)
    else:
        win_id = store.get_global_value('chrome_win_id_for_new_tabs')
        win_title = get_win_title_from_id(win_id, system.exec_command)
        if win_title:
            window.activate(win_title)
            keyboard.send_keys('<ctrl>+t')
            time.sleep(0.01)
        else:
            system.exec_command('google-chrome')
            retCode = window.wait_for_focus('New Tab', timeOut=0.1)


def search_selection_in_new_tab():
    selection = clipboard.get_selection()
    time.sleep(0.1)
    clipboard.fill_clipboard(selection)
    time.sleep(0.1)
    active_class = window.get_active_class()

    new_tab()
    time.sleep(0.1)
    keyboard.send_keys('<ctrl>+v')
    time.sleep(0.2)
    keyboard.send_keys('<enter>')


def search_selection_in_new_win():
    selection = clipboard.get_selection()
    time.sleep(0.1)
    clipboard.fill_clipboard(selection)
    time.sleep(0.1)

    system.exec_command('google-chrome')
    retCode = window.wait_for_focus('New Tab', timeOut=0.1)

    keyboard.send_keys('<ctrl>+v')
    time.sleep(0.2)
    keyboard.send_keys('<enter>')


num_click_switch(
    store.get_value, store.set_value,
    name='quad_chrome',
    functions=[
        new_tab,
        lambda: system.exec_command('google-chrome'),
        search_selection_in_new_tab,
        search_selection_in_new_win
    ],
    timeout=0.18
)