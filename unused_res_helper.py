# -*- coding: UTF-8 -*-
import os
import time

def search(dir, res, resType):    
    for folder, dirs, files in os.walk(dir):
        for file in files:
            fullpath = os.path.join(folder, file)
            if fullpath.endswith(".java"):
                with open(fullpath, 'r') as f:
                    for line in f:
                        if ("R."+resType+"." + res) in line:
                            return True
            if fullpath.endswith(".xml"):
                with open(fullpath, 'r') as f:
                    for line in f:
                        if ("@"+resType+"/" + res) in line:
                            return True
    return False

if __name__ == '__main__':  
    start =time.clock()
    resModules = [
                "ai", 
                "make_course", 
                "practice_partner", 
                "common_framework", 
                "zhiniao_res",
                "zhiniao"
                ]
    findInModules = [
                "ai", 
                "make_course", 
                "practice_partner", 
                "common_framework", 
                "zhiniao_res", 
                "zhiniao"
                ]
    rootPath = "/Users/chendanyang367/Code/zhiniao_a/"

    for resModule in resModules:
        srcMain = rootPath + resModule + "/src/main/"
        for path in os.listdir(srcMain): 
            if path.startswith("res"):
                for resDir in os.listdir(srcMain+path):
                    print resModule + resDir + "------------"
                    if resDir.startswith("anim"):
                        allAnimRes = [i[0:i.index(".")] for i in os.listdir(srcMain+path+"/"+resDir)]
                        for res in allAnimRes:
                            used = False
                            for module in findInModules:
                                root = rootPath + module + "/src/main"
                                if search(root, res, "anim"):
                                    used = True
                                    break
                            if not used:
                                print res

                    if resDir.startswith("drawable"):
                        allDrawableRes = [i[0:i.index(".")] for i in os.listdir(srcMain+path+"/"+resDir)]
                        for res in allDrawableRes:
                            used = False
                            for module in findInModules:
                                root = rootPath + module + "/src/main"
                                if search(root, res, "drawable"):
                                    used = True
                                    break
                            if not used:
                                print res

                    if resDir.startswith("color"):
                        allColorRes = [i[0:i.index(".")] for i in os.listdir(srcMain+path+"/"+resDir)]
                        for res in allColorRes:
                            used = False
                            for module in findInModules:
                                root = rootPath + module + "/src/main"
                                if search(root, res, "color"):
                                    used = True
                                    break
                            if not used:
                                print res

                    if resDir.startswith("layout"):
                        allLayoutRes = [i[0:i.index(".")] for i in os.listdir(srcMain+path+"/"+resDir)]
                        for res in allLayoutRes:
                            used = False
                            for module in findInModules:
                                root = rootPath + module + "/src/main"
                                if search(root, res, "layout"):
                                    used = True
                                    break
                            if not used:
                                print res



    end = time.clock()
    print('Running time: %s Seconds'%(end-start))


