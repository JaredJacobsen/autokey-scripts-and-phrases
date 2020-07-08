#clipboard.fill_selection('testing')
#dialog.info_dialog(clipboard.get_selection())
import time

if not store.get_value('test_double'):
    store.set_value('test_double', True)
    time.sleep(0.2)
    store.set_value('test_double', False)
else:
    keyboard.send_keys('success')
    

