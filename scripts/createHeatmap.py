import plotly.graph_objects as go
import random
import numpy as np
import pandas as pd

dfLine = pd.read_csv("/out/lineData.csv")
dfSim = pd.read_csv("/out/simScoreList.csv")
dfDup = pd.read_csv("/out/linesOfDuplicatedCodeList.csv")
npSim = dfSim.to_numpy()
versionList = dfLine['version'].tolist()
dictVList = {}
i = 0
for x in versionList:
    print(type(x))
    dictVList[x] = i
    i += 1
print(dictVList)
zeroMatrix = np.zeros((len(versionList),len(versionList)))
for x in range(0, len(versionList)):
    for y in range(0, len(versionList)):
        zeroMatrix[x, y] = None
for x in npSim:
    zeroMatrix[dictVList[x[0]], dictVList[x[1]]] = x[2]
print(npSim)
dat = zeroMatrix
print(dat)
reverseVersionList = versionList.copy()
reverseVersionList.reverse()
print(reverseVersionList)
fig = go.Figure(data=go.Heatmap(x=versionList,
                y=reverseVersionList,
                z = dat,
                type = 'heatmap'))
#fig = px.imshow(data,
                #labels=dict(x="Day of Week", y="Time of Day", color="Productivity"),
                #x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'a', 'b', 'c', 'd', 'e'],
                #y=['Morning', 'Afternoon', 'Evening', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'a', 'b']
               #)
fig.write_image('/out/heatMap.png')
print(zeroMatrix)




