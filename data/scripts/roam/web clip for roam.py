import time
from utils import open_roam

title = window.get_active_title()

clipboard.fill_clipboard("")
time.sleep(0.1)

keyboard.send_keys('<ctrl>+l')
time.sleep(0.1)

keyboard.send_keys('<ctrl>+c<ctrl>+c<ctrl>+c<ctrl>+c<ctrl>+c<ctrl>+c<ctrl>+c')
time.sleep(0.1)

fromClip = clipboard.get_clipboard()

time.sleep(0.1)

toClip = '[{}]({})'.format(title[:-16], fromClip)

clipboard.fill_clipboard(toClip)

#dialog.info_dialog(clipboard.get_clipboard())

open_roam(window.get_active_class(), system.exec_command, window.activate)

time.sleep(0.1)
keyboard.send_keys('<ctrl>+u')