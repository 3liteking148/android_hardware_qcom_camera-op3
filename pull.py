#!/bin/python
#pull from vendor repo
#assumes that script is located in los15/hardware/qcom/camera-op3/

from shutil import copy2
import os
VENDOR_DIR = "../../../vendor/oneplus-cm-14.1"

systemdir = os.getcwd() + "/system/"
def pull(line):
    copy2(VENDOR_DIR + "/oneplus3/proprietary/" + line,  systemdir + line)

def main():
    print "Opening proprietary-files.txt"
    f = open("proprietary-files.txt", "r")
    for line in f:
        line = line[0:len(line)-1]
        
        #remove hash
        if line.find("|") != -1:
            line = line[0:len(line)-41]
        if line.find("#") == -1 and line != "":
            print line
            if not os.path.isdir(systemdir + os.path.dirname(line)):
                os.makedirs(systemdir + os.path.dirname(line))
            pull(line)
            
main()
