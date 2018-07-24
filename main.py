#!/usr/bin/env python
# -*- coding:Utf-8 -*-
import os
import glob
import re
import subprocess
import shutil
import datetime

now = datetime.datetime.now()
newDirName = now.strftime("%Y_%m_%d-%Hh%Mmn%Ss")
print newDirName

from optparse import OptionParser
import sys
import os

if ( len(sys.argv) < 2 ):
    print("you must execute \'python main.py -h\' to see for correct execution")
    sys.exit(1)
else:
    print("option : %s" % sys.argv[1])

    parser = OptionParser()
    parser.add_option("-d", "--dir", dest="rep", help ="mettre un dossier contenant les fichiers python")
    parser.add_option("-f", "--file", dest="rep", help ="mettre un fichier python")
    parser.add_option("--files", dest="rep", help ="mettre des fichiers python entre double quotes")
    (options, args) = parser.parse_args()
    rep = options.rep

    print("work on %s" % rep)

def getFilesList():
    for arg in sys.argv:
        print("getFilesList : %s" % arg)

if __name__ == '__main__':
    getFilesList()

    cnt_empty_lines = 0
    cnt_lines = 0
    cnt_total_lines = 0

    f = open(rep, 'r')
    for line in f:
        if ( len(line) == 1 ): # len == 0, empty line
#            print("empty line")
            cnt_empty_lines += 1
        else: # len <> 0
#            print line
            cnt_lines +=1
    f.close()
    cnt_total_lines = cnt_empty_lines + cnt_lines
    print("there is %d lines" % cnt_total_lines)
    print("there is %d full lines" % cnt_lines)
    print("there is %d full lines" % cnt_empty_lines)
    print("fin")
