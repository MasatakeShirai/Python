import os
import sys
import getopt

argv = sys.argv[1:]

options, arguments = getopt.getopt(argv, "u:p:h", ('username=', 'passward=', 'help'))

for name,value in options:
    if name in ('-u', '--username'):
        print('username=%s'% value)
    elif name in ('-p', '--passward'):
        print('passward=%s'% value)
    elif name in ('-h', '--help'):
        print('Useage:...')
