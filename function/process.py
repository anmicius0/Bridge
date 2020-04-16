import subprocess
import sys
import linecache

file = "test.py"


def SSH(COMMAND):
    """Example function with PEP 484 type annotations.

    Args:
        COMMAND (string): The first parameter.

    Returns:
        The return value. True for success, False otherwise.

    """

    # Host
    HOST = "allenlin3024@cnmc.tw"

    # Process
    ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
                           shell=False,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)

    result = ssh.stdout.readlines()

    # if error
    if result == []:
        error = ssh.stderr.readlines()
        print(sys.stderr, "ERROR: %s" % error)
    # if success
    else:
        print(result)


# reset
strings = "echo > temp.py"
Arg = False
# if there are Args then delete it
for times in range(len(open(file, 'r').readlines())):
    count = linecache.getline(file, times + 1)
    if count.find("\"\"\"") == -1:
        if not Arg:
            strings += "echo \"" + count.replace("\n", "") + "\">>temp.py;"
    else:
        if Arg:
            Arg = False
        elif not Arg:
            Arg = True
# throw the SSH python
strings += "python3 temp.py;rm temp.py"
print(strings)
SSH(strings)
