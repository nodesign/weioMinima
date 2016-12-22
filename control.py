#!/usr/bin/python -u
#
# WEIO Web Of Things Platform
# Copyright (C) 2013 Nodesign.net, Uros PETREVSKI, Drasko DRASKOVIC
# All rights reserved
#
#               ##      ## ######## ####  #######
#               ##  ##  ## ##        ##  ##     ##
#               ##  ##  ## ##        ##  ##     ##
#               ##  ##  ## ######    ##  ##     ##
#               ##  ##  ## ##        ##  ##     ##
#               ##  ##  ## ##        ##  ##     ##
#                ###  ###  ######## ####  #######
#
#                    Web Of Things Platform
#
# This file is part of WEIO and is published under BSD license.
# All rights not explicitly granted in the BSD license are reserved.
# See the included LICENSE file for more details.
#
###

from weioLib import weioRunnerGlobals, weioParser, weioUserApi, weioIO, weioGpio

import signal

# User main
import main

import subprocess

class WeioControl(object):
    ###
    # Connect to UPER
    ###
    def __init__(self):
        # User main PID
        self.proc = None

    ###
    # Connect to UPER
    ###
    def init(self):
        # Install signal handlers
        signal.signal(signal.SIGTERM, self.stop)
        signal.signal(signal.SIGINT, self.stop)

        # Init GPIO object for uper communication
        if (weioRunnerGlobals.WEIO_SERIAL_LINKED == False):
            try:
                weioIO.gpio = weioGpio.WeioGpio()
            except:
                print "LPC coprocessor is not present"
                weioIO.gpio = None

    ###
    # Load user module and start threads
    ###
    def start(self):

        # Add user callback handlers for events
        for key in weioUserApi.attach.events:
            weioParser.addUserEvent(weioUserApi.attach.events[key].event,
                    weioUserApi.attach.events[key].handler)

        # Launching subprocess
        self.proc = subprocess.Popen(["python", "main.py"])
        weioRunnerGlobals.WEIO_SERIAL_LINKED = True

    ###
    # execute()
    ###
    def execute(self, req):
        if req['request'] in weioParser.weioSpells or req['request'] in weioParser.weioUserSpells:
            if req['request'] in weioParser.weioSpells:
                res = weioParser.weioSpells[req['request']](req['data'])
            elif req['request'] in weioParser.weioUserSpells:
                res = weioParser.weioUserSpells[req['request']](req['data'])
        else:
            res = None

        return res

    ###
    # stop()
    ###
    def stop(self):
        print("closing process")
        if (self.proc.poll() == None):
            self.proc.terminate()
        if (weioIO.gpio != None):
            if (weioRunnerGlobals.WEIO_SERIAL_LINKED == True):
                weioIO.gpio.stopReader()
                weioIO.gpio.reset()
