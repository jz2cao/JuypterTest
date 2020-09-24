# Import the os module, for the os.walk function
import os
import json

# Set the directory you want to start from
rootDir = '.'
totalCount = 0
for dirName, subdirList, fileList in os.walk(rootDir):
    #print('Found directory: %s' % dirName)
    for fname in fileList:
        #print('\t%s' % fname)
        if "en.json" not in fname:
            if ("-de.json" in fname) or ("zh-Hant.json" in fname) or ("zh-Hans.json" in fname) or ("-es.json" in fname) or ("-fr.json" in fname) or ("-it.json" in fname) or ("-ja.json" in fname) or ("-pt-br.json" in fname) or ("-ru.json" in fname) or ("-zh-cn.json" in fname) or ("-zh-tw.json" in fname) or ("gpconfig" in fname) or ("-pt.json" in fname) or ("-pt-BR.json" in fname) or ("-pt-TW.json" in fname) or ("-zh.json" in fname) or ("-zh-CN.json" in fname) or ("-zh-TW.json" in fname) or ("-zh-CH.json" in fname):
                pName = os.path.join(dirName, fname)[2:]

                print(pName)

print("The total # of words is: " + str(totalCount))
