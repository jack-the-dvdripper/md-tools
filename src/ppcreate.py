#!/usr/bin/env python3

import os
import sys
import subprocess
import getopt 
import configparser
import getpass
import datetime
usage='''

Usage: pcreate.py [-p] path [-c] config 

-----
OPTIONS:
    --help   -h     display help dialog
    --path   -p     PATH to Markdown File
    --config -c     Config File for Markdown
-----
Simple python wrapper for Markdown Presentations

path
|
|
|---literature
|   |-paper1.pdf
|   |-paper2.pdf
|   |-bib.bibtex
|
|
|--graphics
|    |-pic001.png
|
|--MarkdownFile

'''
def create(path,configfile):
    try:
        with open(configfile,'r') as cfile:
            config=configparser.ConfigParser()
            config.read(cfile)
    
    except:
        print('''Falling back to standard config''')
        config=configparser.ConfigParser()
        config['YAML']={
                'title': input("Title: "),
                'author': str(getpass.getuser()),
                'date' : str(datetime.date.today()),
                'theme' : 'Dresden',
                'colortheme' : 'beaver',
                'aspectratio' : '169',
                'fontsize' : '10pt',
                'pagestyle' : 'plain',
                'bibliography' : 'literature/bib.bibtex',
                'reference-section-title' : 'Literature'}
    
    if not os.path.isdir(path):
        os.makedirs(path)
            
        if not os.path.isdir(os.path.join(path,"literature")):
            os.makedirs(os.path.join(path,"literature"))
            
        if not os.path.isdir(os.path.join(path,"graphics")):
            os.makedirs(os.path.join(path,"graphics"))


    with open(os.path.join(path,"presentation.md"),'w') as mdfile:
        mdfile.write('--- \n')
        for key in config['YAML']:
            mdfile.write(key + ":" + '\n') 
            mdfile.write('-' + ' ' + config['YAML'][key] + '\n')
        mdfile.write('--- \n')


argumentsList = sys.argv[1:]
gnuOpts = ["help","config=","path="]
path=""
configfile=""

try:
    arguments,values=getopt.getopt(argumentsList,"hc:p:",gnuOpts)

except getopt.GetoptError as e:
    print (e)
    print(usage)
    sys.exit(2)

for arg,val in arguments:
    if arg in ('-h','--help'):
        print(usage)
        sys.exit(0)
    elif arg in ('-c','--config'):
        configfile=os.path.realpath(val)
    elif arg in ('-p','--path'):
        path=os.path.realpath(val)
    else:
        print('unknown option \n', usage)
        sys.exit(1)

if path :
    create(path,configfile)
else:
    print("Failed to create Markdown presentation")
    sys.exit(1)
