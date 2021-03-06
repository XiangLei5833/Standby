#!/usr/bin/env python3

import sys
import os
from multiprocessing import Process, Queue

queue1 = Queue()
queue2 = Queue()

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
        else:
            raise
    except:
        raise
    data = userdata.items()
    queue1.put(data)


def tax_due(configfile):
    data = queue1.get()
    config = []
    try:
        if len(sys.argv)>0 and os.path.isfile(configfile):
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
   
    ID = []
    MS = []
    SI = []
    IIT = []
    AT = []
    TDI = []
    for info in data:
        ID.append(int(info[0]))
        MS.append(int(info[1]))
    for wage in MS:
        if wage < config[0]:
            si = 2193 * rate
        elif wage > config[1]:
            si = 16446.00 * rate
        else:
            si = wage * rate
        tdi = wage - si - 3500 
        SI.append('%.2f'%si)
        TDI.append(tdi)
    for tdi in TDI:
        if tdi <= 0:
            iit = 0
        elif tdi <= 1500:
            iit  = tdi*0.03-0
        elif tdi <= 4500:
            iit = tdi*0.1-105
        elif tdi <= 9000:
            iit = tdi*0.2-555
        elif tdi <= 35000:
            iit = tdi*0.25-1005
        elif tdi <= 55000:
            iit = tdi*0.3-2755
        elif tdi <= 80000:
            iit = tdi*0.35-5505
        else:
            iit = tdi*0.45-13505
        IIT.append('%.2f'%iit) 
    for i in range(len(ID)):
        at = MS[i] - SI[i] - IIT[i]
        AT.append('%.2f'%at)
    
    newdata = zip(ID, MS, SI, IIT, AT)
    queue2.put(newdata)


def write(gongzi):
    newdata = queue2.get()
    for sub_data in newdata:
         try:
             if len(sys.argv) >0:        
                 f = open(gongzi, 'a')
                 f.write(sub_data)
                 f.write('\n\n')
             else:
                 raise
         except:
             raise
    f.close()


def main():
    args = sys.argv[1:]
    index = args.index('-c')
    configfile = args[index+1]
    index = args.index('-d')
    userdatafile = args[index+1]
    index = args.index('-o')
    gongzi = args[index+1]

    p1 = Process(target=salary, args=(configfile,))
    p2 = Process(target=tax_due, args=(userdatafile,))
    p3 = Process(target=write, args=(gongzi,))
    p1.start()
    p2.start()
    p3.start()
        

if __name__ == '__main__':
    main()
             
                 
