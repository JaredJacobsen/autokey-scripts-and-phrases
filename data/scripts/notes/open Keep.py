import time
active_title = window.get_active_title()
if 'Google Keep' in active_title:
    try:
        system.exec_command('xdotool getactivewindow windowminimize')
    except:
        pass
else:
    window.activate('Google Keep')
    time.sleep(0.02)
    active_title = window.get_active_title()
    if 'Google Keep' not in active_title:
        try:
            system.exec_command('google-chrome --app-id=hmjkmjkepdijhoojdojkdfohbdgmmhki')
        except:
            pass