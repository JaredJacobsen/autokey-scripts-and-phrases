try:
    desktops_num = int(system.exec_command('xdotool get_desktop', getOutput=True))
except:
    pass
    
try:
    system.exec_command('xdotool set_desktop {0}'.format(desktops_num + 1))
except:
    pass