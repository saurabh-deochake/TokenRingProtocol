#!/bin/python
"""
A python program to visualize the agents with tokens accesing the server 
Author: Saurabh Deochake
"""

import os
import subprocess
import shlex


command = 'java -cp libs/*:Moses.jar InteractiveAgent new-host.home 9001 tokenring.law server'

print "Now accepting connections...\n\n Serving agents with tokens\n\n"

process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)

###pipe the output from stdout to the script
while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            agent = output.strip().split()
            if agent[0] == "Received:":
                print agent[1][1:]
        rc = process.poll()