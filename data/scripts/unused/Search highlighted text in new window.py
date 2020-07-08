import time

selection = clipboard.get_selection()
time.sleep(0.1)
clipboard.fill_clipboard(selection)
time.sleep(0.1)

active_class = window.get_active_class()

system.exec_command('google-chrome')
retCode = window.wait_for_focus('New Tab', timeOut=0.1)
#time.sleep(0.1)

keyboard.send_keys('<ctrl>+v')
time.sleep(0.1)
keyboard.send_keys('<enter>')
#keyboard.send_keys(text + "<enter>")
