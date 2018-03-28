import os

class readHoudiniEnv:

    def read(self):
        pathArr =[]
        path = os.environ
        path = path['USERPROFILE'] + r"\Documents"

        CurrentPath = os.getcwd()
        CurrentPathNew1 = CurrentPath.split("\\")
        CurrentPathNewj = "/"
        CurrentPathNew = CurrentPathNewj.join(CurrentPathNew1)

        for filename in os.listdir(path):
            try:
                if filename.split("dini")[0] == "hou":
                    pathHoudini = path + "\\" + filename
                    for env in os.listdir(pathHoudini):
                        if env == "houdini.env":
                            envPath = pathHoudini  + "\\" + env
                            f1= open(envPath,"r")
                            a = list(f1.readlines())

                            for i in a:

                                if i[0:len("SMILE_HOT_BOXPATH")] == "SMILE_HOT_BOXPATH":
                                    pathArr.append(i)
                            f1.close()
            except:
                pass

        return pathArr

