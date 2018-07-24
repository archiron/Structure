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
# VERSION 0.0.0.2

from optparse import OptionParser
import sys
import os, fnmatch

if ( len(sys.argv) < 2 ):
    print("you must execute \'python main.py -h\' to see for correct execution")
    sys.exit(1)
else:
    print("option : %s" % sys.argv[1])

    parser = OptionParser()
    parser.add_option("-d", "--dir", dest="rep", help ="mettre un dossier contenant les fichiers python")
    parser.add_option("-f", "--file", dest="fichier", help ="mettre un fichier python")
    parser.add_option("--files", dest="multfichiers", help ="mettre des fichiers python entre double quotes")
    (options, args) = parser.parse_args()
    rep = options.rep
    fichier = options.fichier
    multfichiers = options.multfichiers

def getFilesList():
    '''
    WARNING : -f (--file) or --files option does not verify if files are .py files
    '''
    tempList = []
    if ( sys.argv[1] == '-d' or (sys.argv[1] == '--dir') ):
        print("work on %s " % rep)
        print("-d")
        listOfFiles = os.listdir('.')  
        pattern = "*.py"  
        for entry in listOfFiles:  
            if fnmatch.fnmatch(entry, pattern):
                print("dir : %s" % entry)
                tempList.append(entry)
    elif( (sys.argv[1] == '-f') or (sys.argv[1] == '--file') ):
        print("work on %s " % fichier)
        print("-f")
        tempList.append(fichier)
    elif( sys.argv[1] == '--files' ):
        print("multfichiers : %s" % multfichiers)
        listOfFiles = multfichiers.split(" ")
        for entry in listOfFiles:
            tempList.append(entry)
        print("work on %s " % multfichiers)
        print("--files")
    else:
        print("bad option")
        print("you must execute \'python main.py -h\' to see for correct execution")
        sys.exit(1)
    return tempList

if __name__ == '__main__':
    filesList = getFilesList()

    cnt_empty_lines = 0
    cnt_lines = 0
    cnt_total_lines = 0

    for file in filesList:
        print("main : %s" % file)
        f = open(file, 'r')
        for line in f:
            if ( len(line) == 1 ): # len == 0, empty line
#                print("empty line")
                cnt_empty_lines += 1
            else: # len <> 0
#                print line
                cnt_lines +=1
        f.close()
    cnt_total_lines = cnt_empty_lines + cnt_lines
    print("there is %d lines" % cnt_total_lines)
    print("there is %d full lines" % cnt_lines)
    print("there is %d empty lines" % cnt_empty_lines)
    print("fin")

