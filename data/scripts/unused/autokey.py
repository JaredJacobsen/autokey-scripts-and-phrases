import time

output = window.activate('AutoKey')
active_title = window.get_active_title()
if 'AutoKey' not in active_title:
    try:
        system.exec_command('gnome-terminal')
    except:
        pass
    time.sleep(0.8)
    keyboard.send_keys('autokey-gtk --verbose<enter>')
    
    