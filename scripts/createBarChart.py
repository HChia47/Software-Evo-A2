import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def createBarChart(vList, dList, title):
    x = np.arange(len(vList))
    plt.bar(x, dList)
    plt.xticks(x, vList, fontsize=4, rotation=90)
    plt.title('Amount of {} in each JQuery version'.format(title))
    #figure = plt.figure()
    #ax = figure.add_axes([0, 0, 1, 1])
    #ax.bar(vList, dList)
    #ax.set_xticks(np.arange(len(vList)), vList)
    plt.savefig('/out/{}Chart.png'.format(title), dpi=1200)

dataFrame = pd.read_csv("/out/lineData.csv")
print(dataFrame)
versionList = dataFrame['version'].tolist()
filesList = dataFrame['files'].tolist()
blankList = dataFrame['blank'].tolist()
commentList = dataFrame['comment'].tolist()
codeList = dataFrame['code'].tolist()
allCodeAddedList = []
for x, y, z in zip(blankList, commentList, codeList):
    xyz = x + y + z
    allCodeAddedList.append(xyz)
createBarChart(versionList, filesList, "files")
createBarChart(versionList, allCodeAddedList, "code")
print(allCodeAddedList)
print(versionList)
print(type(versionList))
print(type(codeList[0]))