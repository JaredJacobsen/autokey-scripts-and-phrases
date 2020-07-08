import time

selection = clipboard.get_selection()
time.sleep(0.1)
clipboard.fill_clipboard(selection)
time.sleep(0.1)
active_class = window.get_active_class()

if 'oogle-chrome' in active_class:
    keyboard.send_keys('<ctrl>+t')
    time.sleep(0.01)
else:
    win_id = store.get_global_value('chrome_win_id_for_new_tabs')
    win_info = system.exec_command("wmctrl -l | grep '{}'".format(win_id), getOutput=True)
    #dialog.info_dialog(str(win_id), str(win_info))
    if win_info:
        win_title = win_info.split('pop-os')[1].strip()
        window.activate(win_title)
        keyboard.send_keys('<ctrl>+t')
        time.sleep(0.01)
    else:
        system.exec_command('google-chrome')
        retCode = window.wait_for_focus('New Tab', timeOut=0.1)
        #keyboard.send_keys('<ctrl>+t')
        #time.sleep(0.01)
        #retCode = window.wait_for_focus('New Tab', timeOut=0.5)

keyboard.send_keys('<ctrl>+v')
time.sleep(0.1)
keyboard.send_keys('<enter>')
#keyboard.send_keys(text + "<enter>")
