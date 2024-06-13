import os,platform
os.system('git pull')

convo=platform.architecture()[0]
if convo=="32bit":
    print('Sorry 32 Bit Not Supported...')
elif convo=="64bit":
    __import__("puti")
