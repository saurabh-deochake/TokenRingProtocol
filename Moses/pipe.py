#!/bin/python
import os
import subprocess
import shlex


dim = []
log = "log.txt"
command = 'java -cp libs/*:Moses.jar InteractiveAgent new-host.home 9001 tokenring.law server'

"""
proc = subprocess.Popen(, shell=True, stdout=subprocess.PIPE)

for line in iter(proc.stdout.readline, ''):
   dim.append(line.rstrip('\n'))
   f.write(line)
##print dim
##f.close()"""

print "Now accepting connections...\n\n Serving agents with tokens\n\n"

process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)

if os.path.isfile(log):
    os.remove(log)
else:
    f = open('log.txt','a')

while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            agent = output.strip().split()
            if agent[0] == "Received:":
                print agent[1][1:]#"\033[1;33;40m" +agent[1][1:]
        rc = process.poll()