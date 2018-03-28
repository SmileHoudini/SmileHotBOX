import os
import hou
class readHoudiniEnv:

    def read(self):
        pathArr =[]

        pathHoudini = hou.homeHoudiniDirectory()
        for env in os.listdir(pathHoudini):
            if env == "houdini.env":
                envPath = pathHoudini  + "\\" + env
                f1= open(envPath,"r")
                a = list(f1.readlines())

                for i in a:
                    if i[0:len("SMILE_HOT_BOXPATH")] == "SMILE_HOT_BOXPATH":
                        pathArr.append(i)
                        f1.close()


        return pathArr

