#winTitle = window.get_active_title()

#win_info = system.exec_command("wmctrl -l | grep '{}'".format(winTitle), getOutput=True)
#win_id = win_info.split('pop-os')[0].split()[0]
#store.set_global_value('remembered_win_2_id', win_id)

from utils import get_active_window_id
    
winTitle = window.get_active_title()

win_id = get_active_window_id(winTitle, system.exec_command)
store.set_global_value('remembered_win_3_id', win_id)
#dialog.info_dialog('hotkey', 'press <super>+1 to come back to this window', width='300')