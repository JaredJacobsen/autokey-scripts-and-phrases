active_title = window.get_active_title()
if 'quick_notes' in active_title:
    window.close('quick_notes')
else:
    try:
        system.exec_command('gedit -s ~/Documents/quick_notes.txt')
    except:
        pass