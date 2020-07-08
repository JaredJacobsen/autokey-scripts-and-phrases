active_class = window.get_active_class()
if 'crx_pjkljhegncpnkpknbcohdijeoejaedia.Google-chrome' in active_class:
    try:
        system.exec_command('xdotool getactivewindow windowminimize')
    except:
        pass
else:
    window.activate('crx_pjkljhegncpnkpknbcohdijeoejaedia.Google-chrome', matchClass=True)
