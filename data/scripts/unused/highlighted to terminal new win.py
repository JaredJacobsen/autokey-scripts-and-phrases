import time

try:
    system.exec_command('gnome-terminal')
except:
    pass

time.sleep(1)
keyboard.send_keys(clipboard.get_selection())
time.sleep(0.2)
keyboard.send_keys('<enter>')