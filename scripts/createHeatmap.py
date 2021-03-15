import plotly.express as px
import random
import numpy as np

zeroMatrix = np.zeros((10,10))
rowLength = zeroMatrix.shape[0]
columnLength = zeroMatrix.shape[1]
for x in range(0, rowLength):
    for y in range(0, columnLength):
        zeroMatrix[x, y] = random.uniform(0, 1)
data = zeroMatrix
data[9, 9] = None
fig = px.imshow(data,
                labels=dict(x="Day of Week", y="Time of Day", color="Productivity"),
                x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'a', 'b', 'c', 'd', 'e'],
                y=['Morning', 'Afternoon', 'Evening', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'a', 'b']
               )
fig.update_xaxes(side="top")
fig.write_image('/out/heatMap.png')
print(zeroMatrix)




