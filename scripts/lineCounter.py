import os
import csv
import pandas as pd
import subprocess

def countLineOfRelease(directory):
    output = subprocess.check_output(["cloc", "--include-lang=JavaScript", '--not-match-f="Test.js$|intro.js$|outro.js$"' '--not-match-d="sizzle"', "--quiet", "--csv", "{}/src".format(directory)])
    print(output)
    splitOutput = output.splitlines()
    lastLine = splitOutput[-1]
    lastLineDec = lastLine.decode('utf-8')
    print(lastLineDec)
    splitLastLine = lastLineDec.split(",")
    print(splitLastLine)
    splitLastLine.remove("SUM")
    print(splitLastLine)
    splitLastLine.insert(0, directory)
    print(splitLastLine)
    print(type(splitLastLine[0]))
    return splitLastLine
    #cmd = 'cloc --quiet --csv {}/src'.format(directory)
    #print(cmd)
    #os.popen(cmd)

with os.scandir("/usr/jquery-data") as dirs:
    listData = []
    for curdir in dirs:
        if curdir.is_dir():
            print(curdir.name)
            data = countLineOfRelease(curdir.name)
            listData.append(data)
    print(listData)
    listData.sort(key=lambda s: list(map(int, s[0].split('.'))))
    print(listData)
    dataFrame = pd.DataFrame(listData, columns = ["version", "files", "blank", "comment", "code"])
    dataFrame.to_csv("/out/lineData.csv", index = False)


