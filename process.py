#!/usr/bin/python

import subprocess
import sys

#ssh command define
def SSH(COMMAND):
    # Host
    HOST = "allenlin3024@cnmc.tw"
    # Process
    ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
                           shell=False,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
    result = ssh.stdout.readlines()
    #
    if result == []:
        error = ssh.stderr.readlines()
        print (sys.stderr, "ERROR: %s" % error)
    else:
        print(result)
#where am i
SSH("pwd")
