retCode, key = dialog.input_dialog(
    title='key value store',
    message='enter a key',
    width='100')
        
if not retCode and key != '':
    key_value_store = store.get_value('key_value_store')
    if key_value_store is None:
        key_value_store = {}
    
    value = key_value_store.get(key, 'value not set')
    retCode, value = dialog.input_dialog(
        title='key value store',
        message=value,
        width='800')
    if not retCode and value != '':
        key_value_store[key] = value
        store.set_value('key_value_store', key_value_store)