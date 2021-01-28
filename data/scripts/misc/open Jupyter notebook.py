import time

try:
    system.exec_command('gnome-terminal')
except:
    pass

time.sleep(1)
keyboard.send_keys('jupyter notebook --ip=0.0.0.0 --port=8080 ~/code/do_not_delete<enter>')
