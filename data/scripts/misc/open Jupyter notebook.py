import time

try:
    system.exec_command('gnome-terminal')
except:
    pass

time.sleep(1)
keyboard.send_keys('jupyter notebook ~/code/do_not_delete/hotkey.ipynb<enter>')
