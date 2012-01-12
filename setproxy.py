#!/usr/bin/env pytho
from ctypes import wintypes, windll
import ctypes
import Tkinter
import os.path
import sys

GetFolderPath = windll.shell32.SHGetFolderPathW
GetFolderPath.argtypes = [wintypes.HWND, ctypes.c_int, wintypes.HANDLE,
                          wintypes.DWORD, wintypes.LPCWSTR]
WinMessageBox = ctypes.windll.user32.MessageBoxA

def MessageBox(msg, title):
   WinMessageBox(None, msg, title, 0)

def emacs_home_folder():
    path_buf = wintypes.create_unicode_buffer(wintypes.MAX_PATH)
    GetFolderPath(0, 26, 0, 0, path_buf)

    return path_buf.value

pwd = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')

try:
    fp = open(pwd + '/dot_emacs_proxy', 'r')    
except:
    MessageBox("Open proxy template file dot_emacs_proxy",
               "Error")
    sys.exit(1)

proxy_script = fp.read().replace('<pwd>', pwd)
fp.close()

dot_emacs_fname = emacs_home_folder() + '/.emacs'
try:
    fp = open(dot_emacs_fname, 'w')
    fp.write(proxy_script)
    fp.close()
except:
    MessageBox("Can't write file %s" % dot_emacs_fname, "Error")
    sys.exit(1)




