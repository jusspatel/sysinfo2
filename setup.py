try:
    import pyfiglet
    import subprocess
    import os
    import re
    import sys
    from colorama import * 
    import platform
    from subprocess import Popen
except ImportError:
    os.system("pip3 install pyfiglet", shell=True)


os.system("cls")

ascii_banner = pyfiglet.figlet_format("SysInfoV2")
print(ascii_banner)
init()

input('\n [=] Press Enter to download modules')
print("Please wait")
os.system('pip install psutil')
os.system('pip install matplotlib')
os.system('pip install hurry.filesize')
print('Modules Installed , opening Programme !')
Popen('SysInfoV2.py' , shell = True)
