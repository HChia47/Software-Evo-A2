import os
import csv
import json
import pandas as pd
import subprocess as sp

# get JsInspect command on only the src to retrieve json file
def getJsInspectBetween2Versions(version1, version2):
  output = sp.getoutput(f'jsinspect ' + str(version1) +"/src "+str(version2) +"/src" + f' -I -L -r json --ignore "intro.js$|outro.js$|Test.js$|sizzle"')
  #print(f'jsinspect ' + str(versionList[0]) +"/src "+str(versionList[1]) +"/src" + f' -I -L -r json --ignore "intro.js$|outro.js$|Test.js$|sizzle"')
  duplicateJson = json.loads(output)
  #print(duplicateJson)
  return duplicateJson

# #count the amount of duplicate code lines by reading the JsInspect json file between two version
# # DOES NOT WORK SINCE THIS WILL GIVE MORE DUPLICATES THAN AMOUNT OF CODE OF 2 VERSION COMBINED
# def duplicateCodeLinesBetween2Versions(version1, version2):
#   duplicateJsonFile = getJsInspectBetween2Versions(version1, version2)
#   totalLinesOfCode = 0
#   for match in duplicateJsonFile:
#     for instance in match["instances"]:
#       totalLinesOfCode = totalLinesOfCode + (instance["lines"][1] - instance["lines"][0] + 1)
#       print(totalLinesOfCode)
#   return totalLinesOfCode


#count the amount of duplicate code lines by reading the JsInspect json file between two version using range such that
def duplicateCodeLinesBetween2Versions(version1, version2):
  duplicateJsonFile = getJsInspectBetween2Versions(version1, version2)
  totalLinesOfCode = 0
  dictionaryRange = {}
  for match in duplicateJsonFile:
    for instance in match["instances"]:
      if instance["path"] in dictionaryRange:
        dictionaryRange[instance["path"]].update(range(instance["lines"][0], instance["lines"][1] + 1))
      else:
        dictionaryRange[instance["path"]] = set(range(instance["lines"][0], instance["lines"][1] + 1))
  #print(dictionaryRange)
  for keys in dictionaryRange.values():
    #print(keys) 
    for value in keys:
      totalLinesOfCode = totalLinesOfCode + 1
  return totalLinesOfCode

# get all data list needed
dataFrame = pd.read_csv("/out/lineData.csv")
versionList = dataFrame['version'].tolist()
blankList = dataFrame['blank'].tolist()
commentList = dataFrame['comment'].tolist()
codeList = dataFrame['code'].tolist()
allCodeAddedList = []
for x, y, z in zip(blankList, commentList, codeList):
    xyz = x + y + z
    allCodeAddedList.append(xyz)


#makes pair of all versions and calculates similirity metric and total amount of codes.
i = 0
j = 0
completeVersionListDuplicates = []
completeSimList = []
while i < len(versionList):
  while j < len(versionList):
    if i < j:
      versionListDuplicates = []
      simListDuplicate = []
      versionListDuplicates.append(versionList[i])
      versionListDuplicates.append(versionList[j])
      simListDuplicate.append(versionList[i])
      simListDuplicate.append(versionList[j])
      totalDuplicatelines = duplicateCodeLinesBetween2Versions(versionList[i], versionList[j])
      simScore = totalDuplicatelines / (allCodeAddedList[i]+allCodeAddedList[j])
      versionListDuplicates.append(totalDuplicatelines)
      simListDuplicate.append(simScore)
      completeVersionListDuplicates.append(versionListDuplicates)
      completeSimList.append(simListDuplicate)
      print(versionListDuplicates)
      print(simListDuplicate)
      #print(completeVersionListDuplicates)
      #print(completeSimList)
    j += 1
  i += 1
  j = 0
print(completeVersionListDuplicates)

#create 2 csv list with one having the pair of versions and total amount of duplicate  and the other the pair and ssimilarity metric score.
dataFrame = pd.DataFrame(completeVersionListDuplicates, columns = ["version", "versionCompare", "DuplicatedCodeTotal"])
dataFrame.to_csv("/out/linesOfDuplicatedCodeList.csv", index = False)
dataFrame = pd.DataFrame(completeSimList, columns = ["version", "versionCompare", "SimScore"])
dataFrame.to_csv("/out/simScoreList.csv", index = False)

