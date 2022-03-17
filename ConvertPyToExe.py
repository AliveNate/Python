'''
You will need PIP installed in Terminal/CMD

Then:       # pip install pyinstaller

Assuming that you have your py file that you want to make executable:

    # pyinstaller --onefile -w main.py

onefile - saves the execuable to one file.
-w      - will execute without bringing up terminal. Some programs do need terminal though.

This can take quite awhile depending on the program you created.

After this is complete, in the folder with all of your original files,
    you will now have a new folder      'dist'

dist will have a single executable file     'main'
Drag that 'main' from 'dist' to the other primary folder.

There should be nothing else in 'dist', you should be able to delete it.


If you have a large program, and a simple computer, it can take a decent amount of time to actaully execute.
'''
