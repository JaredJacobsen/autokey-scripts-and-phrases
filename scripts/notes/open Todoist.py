active_title = window.get_active_title()
if 'todoist' in active_title:
    try:
        system.exec_command('xdotool getactivewindow windowminimize')
    except:
        pass
else:
    window.activate('todoist')
    active_title = window.get_active_title()
    if 'todoist' not in active_title:
        try:
            system.exec_command('google-chrome --app-id=bgjohebimpjdhhocbknplfelpmdhifhd')
        except:
            pass