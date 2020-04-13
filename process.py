#!/usr/bin/python

import subprocess
import sys
#Host
HOST="cnmc@140.131.149.24"
# Process
COMMAND="ls"
#
ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
result = ssh.stdout.readlines()
#
if result == []:
    error = ssh.stderr.readlines()
    print >>sys.stderr, "ERROR: %s" % error
else:
    print(result)
