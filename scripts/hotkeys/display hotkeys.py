from tabulate import tabulate
from os import walk
import json

mypath = '/home/jared/.config/autokey/data/'

files = []
for (dirpath, dirnames, filenames) in walk(mypath):
    files.extend([dirpath + '/' + f for f in filenames if '.json' in f and f != '.folder.json'])
files = files[1:]

hotkeys = []
for f in files:
    if 'vscode' in f or 'unused' in f:
        continue
    with open(f, 'r') as fin:
        data=fin.read()
        obj = json.loads(data)
        h = obj['hotkey']
        if len(h['modifiers']) > 0 or h['hotKey'] is not None:
            k = '+'.join(h['modifiers'] + [h['hotKey']])
            hotkeys.append((obj['description'], k))
         
hotkey_file = '/home/jared/.config/autokey/hotkey_list.txt'
   
with open(hotkey_file, 'w') as fout:
    fout.write(tabulate(hotkeys, headers=['Description', 'Hotkey']))

try:
    system.exec_command("gedit {}".format(hotkey_file))
except:
    pass