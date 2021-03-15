import os
import csv
import json
import pandas as pd
import subprocess as sp

# get JsInspect command on only the src to retrieve json file
def getJsInspectBetween2Versions(version1, version2):
  output = sp.getoutput(f'jsinspect ' + str(versionList[0]) +"/src "+str(versionList[1]) +"/src" + f' -I -L -r json --ignore "Test.js$|sizzle|intro.js$|outro.js$"')
  print(f'jsinspect ' + str(versionList[0]) +"/src "+str(versionList[1]) +"/src" + f' -I -L -r json --ignore "Test.js$|sizzle|intro.js$|outro.js$"')
  duplicateJson = json.loads(output)
  print(duplicateJson)
  return duplicateJson

#count the amount of duplicate code lines by reading the JsInspect json file between two version
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
  print(dictionaryRange)
  for keys in dictionaryRange.values():
    print(keys) 
    for value in keys:
      totalLinesOfCode = totalLinesOfCode + 1
  print(totalLinesOfCode)


dataFrame = pd.read_csv("/out/lineData.csv")
versionList = dataFrame['version'].tolist()
print(versionList)
codeList = dataFrame['code'].tolist()
print(codeList)
duplicateCodeLinesBetween2Versions(versionList[0], versionList[1])
