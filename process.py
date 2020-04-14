import subprocess
import sys


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


# where am i
SSH("pwd")
