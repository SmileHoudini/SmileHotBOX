# SmileHotBOX
Overview
This is an open source framework for load Houdini tools,you can quickly customize the tools and install them on the Interface.It is very meaningful to help you simplify the complex operation of common use,They have used more than a year, good improvement of their own operation, so the source code for everyone to share.

install
Written in a cross platform use python,Here is the way to install windows7+, the same method of Linux and OS

1,Copy  INSTALLPATH/HoudiniHotBox17.0/houdini.env file to  C:\Users\Administrator\Documents\houdini16.0  and open the houdini.env ,Modifying the environment variable corresponding to your path   SMILEHOTBOX = C:/hotboxtest/HoudiniHotBox17.0  

2,Copy  HoudiniHotBox17.0\toolbar\SmileHotBox17.shelf file to C:\Users\Administrator\Documents\houdini16.0\toolbar

3,open Hoduini,Find smilehotbox in shelftool 
[图片]

4 ,Recommend set hotkey "S",Getting used to this shortcut key will make you feel comfortable and comfortable
[图片]

Instructions
You can press S at different windows, and there will be different tool interfaces, which can well satisfy your operation under all interfaces. Now it supports operation under senseviwe and networkview, you can expand with more in hotBox_17_manUi.py
1 ,Press S to release S immediately
2,Press the left mouse button on the interface to slide on the interface
3,Slide to the outer ring function to release the left mouse button

Custom tools
It's very easy to extend the written Python file to HoudiniHotBox17.0\lib ,The python file name will set the button name of the interface. For the sake of beauty, the best initials are capitalized, such as SetRendPath.py,The class name in the code is guaranteed to be the same as the file name, such as  class SetRendPath:  ,The main function def run (): ,
for example Cd_Object.py:
  1. import hou
  2. class Cd_Object:
  3.     def __init__(self):
  4.         self.pane=hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
  5.     def run(self):
  6.         f1 = open('material.txt', 'r')
  7.         a=   f1.readlines()[0]
  8.         a=hou.node(a).parent().path()
  9.         f1.close()
  10.       self.pane.cd(a)
Next, set the function to the interface
1,
[图片]









2
[图片]











3
[图片]

Set over and enjoy it

Support
You can tell me your needs by mail, including your problems,Telephone +8618810865732
Because my personal thoughts are limited, I hope you can give me a better idea of your mail. I will update it to GitHub for the first time. I am looking forward to receiving your mail, any suggestion, email:change52092@yahoo.com.
This is a good preview of the function
HoudiniHotBox17.0\doc\SmileHotBoxShowReel.mp4

Known Issues
Ninety percent of the functionality you can use across the platform,Some functions only support windows, but TD developers are easy to correct. Some functions are too large dependence , Rigid tools rely on 40 more complex assets. They belong to the content of tuition tutorial,He spent a great deal of blood,I'm sorry it's need pay.Please see details SmileFX  https://weidian.com/s/1225774756?ifr=shopdetail&wfr=c

Release Notes
2018/3/27 smileHotBox 17.0   Initial relea
