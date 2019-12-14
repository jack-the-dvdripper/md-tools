#!/usr/bin/env python3

import os
import sys
import pypandoc
import subprocess

usage='''
Usage: genpdf.py [inputfile] 
'''

if len(sys.argv)<2:
    print(usage)
    quit()

basename=os.path.splitext(os.path.basename(sys.argv[1]))[0]
texfile="".join([basename,'.tex'])
pdffile="".join([basename,'.pdf'])

print(basename)

'''
output = pypandoc.convert_file(sys.argv[1],'beamer', '--toc',outputfile=texlive)
'''

filters = ['pandoc-citeproc']
pdoc_args=['-s', '--toc','--number-sections', '-V lang=de']
output = pypandoc.convert_file(sys.argv[1],
                               to='beamer',
                               format='md',
                               extra_args=pdoc_args,
                               filters=filters)
with open(texfile,'w') as f:
    f.write(output)
print("generated " + texfile)

subprocess.call(['xelatex',texfile])

print("generated " + pdffile)
