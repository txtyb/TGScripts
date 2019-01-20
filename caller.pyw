import os
task_list=['QQMusic.exe','EasiNote.exe','GeePlayer.exe',\
           'cmd.exe',\
           'PotPlayerMini64.exe /t',\
           'QQLive.exe /t',\
           ]
for i in task_list:
    a=os.popen('taskkill /f -im %s'%i).read()
