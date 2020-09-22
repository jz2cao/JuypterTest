import locale
import json
import os

full_path = os.path.realpath(__file__)
full_path = os.path.dirname(full_path)
folderName= full_path.split("/")[-1]
print(folderName)

rootDir = '.'
totalCount = 0
for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        if ".json" in fname:
            with open(os.path.join(dirName, fname)) as json_file:
                if ("de.json" not in fname) and ("eo.json" not in fname) and ("zh-Hant.json" not in fname) and ("zh-Hans.json" not in fname) and ("es.json" not in fname) and ("fr.json" not in fname) and ("it.json" not in fname) and ("ja.json" not in fname) and ("pt-br.json" not in fname) and ("ru.json" not in fname) and ("zh-cn.json" not in fname) and ("zh-tw.json" not in fname) and ("gpconfig" not in fname) and ("pt.json" not in fname) and ("pt-BR.json" not in fname) and ("pt-TW.json" not in fname) and ("zh.json" not in fname) and ("zh-CN.json" not in fname) and ("zh-TW.json" not in fname) and ("zh-CH.json" not in fname):
                    removeString1 = '-en.json'
                    removeString2 = '.en.json'
                    removeString3 = '_en.json'
                    removeString4 = '.json'
                    pathName = os.path.join(dirName, fname)
                    pathName = pathName.replace(removeString1, '')
                    pathName = pathName.replace(removeString2, '')
                    pathName = pathName.replace(removeString3, '')
                    pathName = pathName.replace(removeString4, '')
                    print(pathName)
                    languages = ['fr','es','zh-Hans', 'zh-Hant', 'ja', 'de', 'it', 'pt-BR', 'ru']
                    languages2 = ['fr','es','zhHans', 'zhHant', 'ja', 'de', 'it', 'ptBR', 'ru']
                    if fname != "en.json":
                        # i.e en file is called "strings_en.json"
                        translatedName = fname
                        translatedName = translatedName.replace(removeString1, '')
                        translatedName = translatedName.replace(removeString2, '')
                        translatedName = translatedName.replace(removeString3, '')
                        translatedName = translatedName.replace(removeString4, '')
                        for i in range(9):
                            langName = translatedName + "-" + languages[i] + ".json"
                            print("const "+languages2[i]+" = require(\"./"+langName+"\");")

                    else:
                        # i.e en file is called "en.json"
                        for i in range(9):
                            langName = languages[i] + ".json"
                            print("const "+languages2[i]+" = require(\"./"+langName+"\");")
                    totalCount += 1
                    print
                    print("// Public Methods ------------------------------------------------------------->")
                    print("""
module.exports = {
\t"en": en,
\t"eo": eo,
\t"de": de,
\t"es": es,
\t"fr": fr,
\t"it": it,
\t"ja": ja,
\t"pt-BR": ptBR,
\t"ru": ru,
\t"zh-CN": zhHans,
\t"zh-TW": zhHant
};
                    """)
                    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print(totalCount)



