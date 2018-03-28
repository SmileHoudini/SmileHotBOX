import sys
sys.path.append(r"C:\PythonLibs\HoudiniHotBox17.0\lib")

class SubmitDeadline:
    def run(self):
        import SubmitDeadlineMain
        reload(SubmitDeadlineMain)