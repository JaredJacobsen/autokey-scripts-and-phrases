retCode, userInput = dialog.input_dialog(
    title='Quick Note',
    message='Enter a note',
    width='800')
        
if not retCode and userInput != '':
    delimiter = '\n---------------------------\n'
    with open('~/Documents/quick_notes.txt', 'a+') as fout:
        fout.write(delimiter)
        fout.write(userInput)
    
    