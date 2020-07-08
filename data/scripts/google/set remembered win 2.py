winTitle = window.get_active_title()

win_info = system.exec_command("wmctrl -l | grep '{}'".format(winTitle), getOutput=True)
win_id = win_info.split('pop-os')[0].split()[0]
store.set_global_value('remembered_win_2_id', win_id)