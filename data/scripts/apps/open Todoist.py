active_class = window.get_active_class()
if 'crx_elldfnmogicegdcphgljaoaklkpcnbnn' in active_class:
    try:
        system.exec_command('xdotool getactivewindow set_desktop_for_window 0')
    except:
        pass
else:
    window.activate('crx_elldfnmogicegdcphgljaoaklkpcnbnn.Google-chrome', matchClass=True)