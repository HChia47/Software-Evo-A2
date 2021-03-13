import os
import csv
import pandas

def countLineOfRelease(directory):
    cmd = 'cloc --quiet --csv {}/src'.format(directory)
    print(cmd)
    os.popen(cmd)

with os.scandir("/usr/jquery-data") as dirs:
    for curdir in dirs:
        print(curdir.name)
        countLineOfRelease(curdir.name)
