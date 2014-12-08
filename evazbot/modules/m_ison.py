# -*- coding: utf-8 -*-
from base import *
import ast
from urllib.request import urlopen
import pprint

url="http://redflare.ofthings.net"

def msg(mp):
  if mp.cmd("ison"):
    search = mp.args()
    found = {}
    with urlopen(url+"/reports") as u:
      servers = ast.literal_eval(u.read().decode())
      for server in servers.keys():
        for name_p in servers[server]['playerNames']:
          name = name_p['plain']
          if name.lower().find(search.lower()) != -1:
            if server not in found:
              found[server]=list()
            found[server].append(name)
      for s in found:
        out = servers[s]['description']+": "
        for p in found[s]:
          out+=p+", "
        main.sendcmsg(out)
    return True
  return False
  
def showhelp():
  main.sendcmsg(".ison name of player: Search "+url+" for <name>.")