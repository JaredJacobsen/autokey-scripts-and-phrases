from utils import get_win_title_from_id

win_id = store.get_global_value('remembered_win_3_id')

if win_id is not None:
    win_info = system.exec_command("wmctrl -l | grep '{}'".format(win_id), getOutput=True)
    if win_info:
        win_title = win_info.split('pop-os')[1].strip()
        window.activate(win_title)

win_title = get_win_title_from_id(win_id, system.exec_command)
if win_title:
    window.activate(win_title)