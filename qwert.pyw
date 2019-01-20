import sys,time,os,datetime#,shutil
from os import popen
from win32com.shell import shell, shellcon
a=sys.argv
def get_date():
    a=time.localtime()
    d=datetime.datetime(a.tm_year,a.tm_mon,a.tm_mday)
    d+=datetime.timedelta( -a.tm_wday,0, 0)
    sm='0'+str(d.month)if d.month<10 else str(d.month)
    sd='0'+str(d.day)if d.day<10 else str(d.day)
    s=str(d.year)+sm+sd
    return s
dirs='D:\\Desktop\\%s\\'%get_date()
if not os.path.isdir(dirs):
    os.mkdir(dirs)
os.chdir(dirs)
if len(a)>1:
    b=filter(lambda i: os.path.isdir(i) or os.path.isfile(i),a[1:])
    shell.SHFileOperation ((0, shellcon.FO_MOVE, '\0'.join(b), '',
                            shellcon.FOF_ALLOWUNDO, None, None))
else:
    popen('explorer %s'%dirs)
time.sleep(1)
