choices = ["python", "javascript", "other"]

retCode, choice = dialog.list_menu(choices)
if retCode == 0:
    dialog.info_dialog("Context", "Setting language context to " + choice, width='300')
    store.set_global_value('language_context', choice)