import os
import hou
#import binascii
#
### uncoad
#
#def uncoad (s_16):
#    s_16List = []
#    new_16 =""
#    for index in s_16:
#        s_16List.append(index)
#    s_16List.reverse()
#
#    for a in s_16List:
#        new_16+=a
#    s = binascii.a2b_hex(new_16)
#    return s
#
#def report():
#    for a in range(10):
#
#        print "Please contact the purchase of genuine QQ 854067387"
#
#
#
### run
#def run():
#    pathnew = os.environ
#    pathnew = pathnew['USERPROFILE']+r"\Documents"
#
#
#    tPath = os.getenv('SMILEHOTBOX')
#
#    #coad path
#    boosId = pathnew+r"\WINDOWS1.txt"
#    SmileRbdToolCpuAllInfo = tPath +"\\HoudiniHotBoxCpuAllInfo.txt"
#
#
#    #openCpufile
#    try:
#        fl1=open(SmileRbdToolCpuAllInfo, 'r')
#
#    #allcoad
#        allCoad = fl1.readlines()
#
#        fl1.close()
#
#        fl2=open(boosId, 'r')
#        bossIdCoad= fl2.readlines()
#        fl2.close()
#    except:
#        report()
#
#    spk = []
#    for coad in allCoad:
#        coad= coad.split("\n")[0]
#        try :
#            if uncoad(coad):
#                coad=uncoad(coad)
#
#                spk.append(coad)
#
#
#
#        except :
#            pass
#    spk2 = []
#    temp =0
#    for b in spk:
#
#        try:
#            b= b.split("854067387")[0].split("HoudiniHotBox")[1]
#            a =uncoad( bossIdCoad[0])
#            a= a.split("HoudiniHotBox854067387")[0]
#
#            if b == a:
#                temp+=1
#
#
#        except:
#           pass
#    if temp ==0:
#        report()
#        hou.Error(hou.NodeError)
#