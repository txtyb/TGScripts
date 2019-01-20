# TGScripts
Management of  scripts in TG.

## caller.pyw
To call system kill command by `os.popen` to kill programs like `QQMusic.exe` , `GeePlayer` , `cmd.exe` etc.Especially useful when doing something not allowed officially and kill them down immediately when any teachers come into the classroom.To use it else where , just create a link on the desktop and set an shortcut key( in the computer of TG, the key is `<C-F9>`, which is the pen button on the remote control).
## NewFTP.pyw
### General
A pygame powered GUI program to login the FTP system.
It's open source, unlike any other distribution in TG.
Feel free to edit its looking.
### Controlling
#### Touch control
- tap the square block to login
- slide up and down to turn the pages
- slide towards left to minimize
- tap the minimized floating window to maximize
- drag the minimized window to put it any where
- right click to quit
#### Remote control
- press F3 to start (depend on the hotkey you set)
- press the number corresponding to the block to login
- PgUp and PgDown to turn the pages
- press F3 again to maximize or show window
- left arrow to minimize (have not done yet)
- press Esc, namely Back to quit
#### Keyboard and mouse
- I think you know it 

### Why minimized floating window
As you know, python is a language for the 21st century,
and easy to write, read and mantain. However, it takes ages to start.
To cut down the waiting time, the minimized window is the best option.
### Why pywin32
The smoother, the more win32API should be used. (please do not complain my abusing win32API)
### TO DO
#### Black Magic
Dragging out the files newly uploaded from main window to the desktop. (this might be quite hard)
#### Good-looking Themes
It is obvious that we are using Microsoft Windows7 theme. What if Linux theme or other awesome software, organizations?
#### Advertising
Good things should be shared.
## qwert.pyw
A useful tool to manage the desktop files. when you select the file and drag them onto the link on the desktop (that is, `pythonw.exe qwert.pyw` ,and we named the link `BlackHole` as a joke) it will automaticly move them into the desktop directory and in the directory named after date of the Monday of the week. What's more, it uses the `SHFileOperation` which makes it looks just like what you use in the `explorer.exe`. And for historical reasons, its name was pretty confusing as `qwert.pyw`.
## JupyterLaucher.pyw
Lauch the `jupyter notebook` and hide the console using `win32gui` if it is not running, or show the console window if running.
## website.txt
Store some useful websites ever encountered.
## net.py
A simple script made by sjl to switch the net mode in the command line.
## JupyterNotes/
Contains several jupyter notebooks which involves tests of `matplotlib`, `sympy`, etc.
## PygameStuff/
#### derection.py
A wrapper of direction control in pygame.
#### EventSpyer.py
To see what event happend using pygame's event system.
## Tests/
Contains several python language tests , tests of `PyQt5` ,and `pyplot`.
## WebTests/
Some tests with HTML , JS and CSS.
## tyb/
Several tests made by tyb.
