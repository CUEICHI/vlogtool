#
# File mover 
#
'''
ファイルを日付に従ったディレクトリに移動します．
移動先がない場合は自動的に生成します
'''

import glob
import datetime
import os
import sys
import shutil
from time import ctime, strftime


if len(sys.argv) < 2:
    print("Usage: filemover directory")
    exit(0)

DIR = sys.argv[1]
print ("[",DIR,"]")
for file in glob.iglob(DIR):
    print(file)
    ftime = datetime.datetime.fromtimestamp(os.stat(file).st_mtime)
    dirname = ftime.strftime("%m-%d")
    if os.path.isdir(dirname) == False:
        os.mkdir(dirname)
    print('move', dirname,'/',file)
    dstname = f"{dirname}/{file}"
    if os.path.exists(dstname) == False:
        shutil.move(file,dstname)
    else:
        print("File exists?!!")








