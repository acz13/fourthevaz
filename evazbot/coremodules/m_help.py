# -*- coding: utf-8 -*-
from base import *


def msg(mp):
    if mp.cmd(c_net.helpcommand):
        args = mp.args()
        splitargs = args.split()
        if mp.iswlist():
            if len(splitargs) == 0:
                main.sendcmsg("Use .help <module> for a specific module.")
                cmd.outlist(c_modules.helpmodulenames())
            elif len(splitargs) == 1:
                c_modules.showhelp(splitargs[0])
            else:
                main.sendcmsg("Invalid Arguments")
        else:
            main.sendcmsg("No access, contact an admin.")
        return True
    return False


def showhelp():
    main.sendcmsg(".help <[module]>: View help for <module>." +
    "If <module> is omitted, view general help.")