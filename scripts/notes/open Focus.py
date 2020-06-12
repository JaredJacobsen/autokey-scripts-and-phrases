import time
active_title = window.get_active_title()
if 'Focus To-Do' in active_title:
    try:
        system.exec_command('xdotool getactivewindow windowminimize')
    except:
        pass
else:
    window.activate('Focus To-Do')
    time.sleep(0.1)
    active_title = window.get_active_title()
    if 'Focus To-Do' not in active_title:
        try:
            system.exec_command('google-chrome --app-id=crx_ngceodoilcgpmkijopinlkmohnfifjfb')
        except:
            pass
