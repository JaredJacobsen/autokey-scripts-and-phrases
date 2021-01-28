import time

def open_roam(active_class, exec_command, activate):
    if 'crx_dpbhdojchflfefifdehlgddpoaanhgnf.Google-chrome' in active_class:
        try:
            exec_command('xdotool getactivewindow set_desktop_for_window 0')
        except:
            pass
    else:
        activate('crx_dpbhdojchflfefifdehlgddpoaanhgnf.Google-chrome', matchClass=True)


def close_window(exec_command):
    try:
        exec_command('wmctrl -c :ACTIVE:')
    except:
        pass

def get_win_title_from_id(win_id, exec_command):
    try:
        win_info = exec_command("wmctrl -l | grep '{}'".format(win_id), getOutput=True)
    except:
        win_info = None

    return win_info.split('pop-os')[1].strip() if win_info else None

def get_active_window_id(active_win_title, exec_command):
    win_info = exec_command("wmctrl -l | grep '{}'".format(active_win_title), getOutput=True)
    return win_info.split('pop-os')[0].split()[0]

def num_click_switch(get_value, set_value, name, functions, timeout=0.2):
    key = 'num_click_switch' + name
    def f():
        return [i for i in range(len(functions)) if get_value(key+str(i))]
    vals = f()
    num_clicks = max(vals) + 1 if len(vals) > 0 else 0
    
    if not num_clicks + 1 > len(functions):
        set_value(key+str(num_clicks), True)
        time.sleep(timeout)
        vals = f()
        set_value(key+str(num_clicks), False)
        if max(vals) == num_clicks:
            functions[num_clicks]()
        

def double_click(get_value, set_value, send_keys,
    first_contents, second_contents, timeout=0.2):
    store_key = 'double_' + '{0}_{1}'.format(first_contents, second_contents)
    if not get_value(store_key):
        if first_contents:
            send_keys(first_contents)
        set_value(store_key, True)
        time.sleep(timeout)
        set_value(store_key, False)
    else:
        send_keys(second_contents)

def triple_click(get_value, set_value, send_keys,
    first_contents, second_contents, third_contents, timeout=0.2):
    key = '{0}_{1}_{2}'.format(first_contents, second_contents, third_contents)
    double_store_key = 'double_' + key
    triple_store_key = 'triple_' + key
    if not get_value(double_store_key) and not get_value(triple_store_key):
        if first_contents:
            send_keys(first_contents)
        set_value(double_store_key, True)
        time.sleep(timeout)
        set_value(double_store_key, False)
    elif not get_value(triple_store_key):
        if second_contents:
            send_keys(second_contents)
        set_value(triple_store_key, True)
        time.sleep(timeout)
        set_value(triple_store_key, False)
    else:
        send_keys(third_contents)


def quadruple_click(get_value, set_value, send_keys,
    first_contents, second_contents, third_contents, 
    fourth_contents, timeout=0.2):
    key = '{0}_{1}_{2}_{3}'.format(first_contents, second_contents, third_contents, fourth_contents)
    double_store_key = 'double_' + key
    triple_store_key = 'triple_' + key
    quad_store_key = 'quad_' + key
    if not get_value(double_store_key) and not get_value(triple_store_key) and not get_value(quad_store_key):
        if first_contents:
            send_keys(first_contents)
        set_value(double_store_key, True)
        time.sleep(timeout)
        set_value(double_store_key, False)
    elif not get_value(triple_store_key) and not get_value(quad_store_key):
        if second_contents:
            send_keys(second_contents)
        set_value(triple_store_key, True)
        time.sleep(timeout)
        set_value(triple_store_key, False)
    elif not get_value(quad_store_key):
        if third_contents:
            send_keys(third_contents)
        set_value(quad_store_key, True)
        time.sleep(timeout)
        set_value(quad_store_key, False)
    else:
        send_keys(fourth_contents)

def active_class_switch(get_active_class, context_dict):
    simple_name_dict = {
        'terminal': 'gnome-terminal-server.Gnome-terminal',
        'chrome': 'google-chrome.Google-chrome',
        'vscode': 'code.Code',
        'keep': 'crx_hmjkmjkepdijhoojdojkdfohbdgmmhki.Google-chrome',
        'todoist': 'crx_bgjohebimpjdhhocbknplfelpmdhifhd.Google-chrome',
        'autokey': 'autokey-gtk.Autokey-gtk',
        'roam': 'crx_dpbhdojchflfefifdehlgddpoaanhgnf.Google-chrome',
        'default': 'default'
    }
    context_dict = {simple_name_dict[k]: v for k, v in context_dict.items()}
    
    active_class = get_active_class()
    func = context_dict.get(active_class)
    if func is None:
        context_dict['default']()
    else:
        context_dict[active_class]()