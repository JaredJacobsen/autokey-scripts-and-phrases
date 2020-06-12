try:
    desktops_num = int(system.exec_command('xdotool get_desktop', getOutput=True))
except:
    pass

try:
    system.exec_command('xdotool set_desktop {0}'.format(
        desktops_num - 1 if desktops_num > 0 else desktops_num
    ))
except:
    pass