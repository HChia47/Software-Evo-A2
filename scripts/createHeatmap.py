import plotly.graph_objects as go
import random
import numpy as np
import pandas as pd

def createFigRectVert(listDifLengths, listDifLengths2):
    i = -5.5
    j = -0.5
    for x, y in zip(listDifLengths, listDifLengths2):
        i = i+x
        j = j+y
        fig.add_shape(type="rect",
                x0=i, y0=-0.5, x1=j, y1=82.5,
                line=dict(color="black", width = 2),
                )

def createFigRectHorz(listDifLengths, listDifLengths2):
    i = -2.5
    j = -0.5
    for x, y in zip(listDifLengths, listDifLengths2):
        i = i+x
        j = j+y
        fig.add_shape(type="rect",
                x0=-0.5, y0=i, x1=82.5, y1=j,
                line=dict(color="black", width = 2),
                )

dfLine = pd.read_csv("/out/lineData.csv")
dfSim = pd.read_csv("/out/simScoreList.csv")
dfDup = pd.read_csv("/out/linesOfDuplicatedCodeList.csv")
npSim = dfSim.to_numpy()
versionList = dfLine['version'].tolist()
dictVList = {}
i = 0
for x in versionList:
    dictVList[x] = i
    i += 1
zeroMatrix = np.zeros((len(versionList),len(versionList)))
for x in range(0, len(versionList)):
    for y in range(0, len(versionList)):
        zeroMatrix[x, y] = None
for x in npSim:
    zeroMatrix[dictVList[x[1]], dictVList[x[0]]] = x[2]
print(npSim)
dat = np.flip(zeroMatrix, axis=0)
print(dat)
reverseVersionList = versionList.copy()
reverseVersionList.reverse()
print(reverseVersionList)
heatmap = go.Heatmap(x=versionList,
                y=reverseVersionList,
                z = dat,
                xgap = 1,
                ygap = 1)
layout = go.Layout(height=1500, width=1500)
fig = go.Figure(data=heatmap, layout=layout)
difLengths = [5, 5, 6, 7, 4, 6, 4, 6, 4, 4, 2, 3, 4, 5, 4, 5, 5, 1, 2, 2, 2]
difLengths2 = [5, 6, 7, 4, 6, 4, 6, 4, 4, 2, 3, 4, 5, 4, 5, 5, 1, 2, 2, 2, 2]
difLengthsReverse2 = difLengths2.copy()
difLengthsReverse2.reverse()
difLengthsReverse = difLengthsReverse2.copy()
difLengthsReverse.pop()
difLengthsReverse.insert(0, 2)
print(difLengthsReverse)
print(difLengthsReverse2)
createFigRectVert(difLengths, difLengths2)
createFigRectHorz(difLengthsReverse, difLengthsReverse2)
fig.update_xaxes(type='category')
fig.update_xaxes(type='category')
fig.write_image('/out/heatMap.png')
print(zeroMatrix)




