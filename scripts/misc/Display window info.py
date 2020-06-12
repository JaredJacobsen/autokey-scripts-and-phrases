winTitle = window.get_active_title()
winClass = window.get_active_class()

win_info = system.exec_command("wmctrl -l | grep '{}'".format(winTitle), getOutput=True)
win_id = win_info.split('pop-os')[0].split()[0]


dialog.info_dialog("Window information", 
          "Active window information:\nTitle: '%s'\nClass: '%s'\nid: '%s'" % (winTitle, winClass, win_id))