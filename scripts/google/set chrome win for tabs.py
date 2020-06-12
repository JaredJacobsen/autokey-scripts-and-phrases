from utils import get_active_window_id
    
winTitle = window.get_active_title()
if 'Google Chrome' in winTitle:
    win_id = get_active_window_id(winTitle, system.exec_command)
    store.set_global_value('chrome_win_id_for_new_tabs', win_id)
    dialog.info_dialog('hotkey', 'tabs will direct to this window', width='300')