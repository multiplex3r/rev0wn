#!/usr/bin/env python
from netaddr import *
import socket
import sys

"""
rev0wn.py
author: multiplex3r
description: reverse DNS record searching tool to assist with asset identification
thanks: peleus
required python libs: netaddr (pip install netaddr)
"""

if len(sys.argv) < 2:
    print "Usage: {} <domain name> <netblock cidr>".format(sys.argv[0])
    print "Example: ./rev0wn.py blahblah.com 192.168.0.0/24"
    print "Description: rev0wn will look for the occurance of blahblah.comin the PTR records for hosts in netblock"
    sys.exit()

class notify:
    start = '\033[94m[*]\033[0m'
    alert = '\033[92m[!]\033[0m'
    fail = '\033[91m[+]\033[0m'
    warn = '\033[93m[+]\033[0m'
    stop = '\033[94m[*]\033[0m'

t = sys.argv[2]
l = sys.argv[1]
c = 0

print notify.start + " Starting rev0wn scanner.."

for i in IPSet([t]):
    c += 1
    try:
        r = socket.gethostbyaddr(str(i))
        if str(l) in str.lower(r[0]):
            print "\r{} {} {} asset found: {}".format(notify.alert, i, l, r[0])
        else:
            print "\r{} {} {} not a {} PTR record..".format(notify.fail, i, r[0], sys.argv[1])
    except:
        print "\r{} {}/{} IPs scanned - {}..".format(notify.warn, c, len(IPSet([t])), i),
        sys.stdout.flush()
        pass

print "\r{} Scan of {} addresses completed..".format(notify.stop, l)
