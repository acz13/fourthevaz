# -*- coding: utf-8 -*-
#This will import all essential Fourth Evaz components
from base import *


#The message-received event
def msg(mp):
    #if .example is received as a command
    if mp.cmd("example"):
        #Send a message echoing the arguments to the current channel/query.
        main.sendcmsg("Example's Default Arguments: " +
        '"' + mp.argsdef() + '"')
        #Send a message echoing -test
        if mp.argbool("test"):
            main.sendcmsg('"' + mp.argstr("test") + '"')
        #Command was received
        return True
    #No command received
    return False


#The ".help example" event
def showhelp():
    #Send a basic help message
    main.sendcmsg(".example <arguments>: Return the arguments.")