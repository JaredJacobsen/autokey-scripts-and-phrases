#import time
active_class = window.get_active_class()
if 'crx_dpbhdojchflfefifdehlgddpoaanhgnf.Google-chrome' in active_class:
    try:
        system.exec_command('xdotool getactivewindow windowminimize')
    except:
        pass
else:
    window.activate('crx_dpbhdojchflfefifdehlgddpoaanhgnf.Google-chrome', matchClass=True)
#    time.sleep(0.05)
#    active_class = window.get_active_class()
#    if 'crx_dpbhdojchflfefifdehlgddpoaanhgnf.Google-chrome' not in active_class:
#        try:
#            system.exec_command('google-chrome --app-id=crx_dpbhdojchflfefifdehlgddpoaanhgnf')
#        except:
#            pass