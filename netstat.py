#!/usr/bin/env python

import subprocess

# nestat command with "-tulpn" options
def netstat_func():
    command = "netstat"
    command_arg = "-tulpn"
    print ("Gathering server port information with %s command:\n" % command)
    subprocess.call(command_arg, command)

def main():
    netstat_func()

main()
