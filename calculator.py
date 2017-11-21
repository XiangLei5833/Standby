#!/usr/bin/env python3

import sys
import os
import multiprocess import Process, Queue

args = sys.argv[1:]
index = args.index('-c')
configfile = args[index+1]
index = args.index('-d')
userdatafile = args[index+1]

queue1, queue2 = Queue()

def salary(userdatafile):
    userdata = {}
    try:
        if len(sys.argv)>0 and os.path.isfile(userdatafile):
            f = open(userdatafile)
            for user in f:
                user = user.strip('\n')
                user = user.split(',')
                key = user[0].strip()
                value = user[1].strip()
                userdata[key] = value
        data = userdata.items()
        queue1.put(data)
        else:
            raise
    except:
        raise

def tax_due(configfile)
    data = queue1.get()
    config = []
    try:
        if len(sys.argv)>0 and os.path.isfile(configfile)
            f = open(configfile)
            for c in f:
                c = c.strip('\n')
                c = c.split('=')
                value = c[1].strip()
                config.append(value)
        else:
            raise
    except:
        raise
    rate = sum(config[2:])
        
