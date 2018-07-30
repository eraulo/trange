#!/usr/bin/env python

__author__="Mariano de Deus dedeus_mariano@yahoo.com"

def trange(first=0, number=0, step=0 ):
    if (first or number or step) and number:
        if number:
            rlist = [first]
            while True:
                if len(rlist) ==  1:
                    if rlist[0] == 0:
                        rlist += [len(rlist)]
                    else:
                        rlist += [abs(~len(rlist))]
                elif rlist[-1] < number:
                    rlist += [abs(~rlist[-1])]
                elif rlist[-1] == number:
                    break
            if first != 0 and step != 0:
                for n in rlist[(first-1):(number-1):step]:
                    yield n
            elif first == 0 and step != 0:
                for n in rlist[first:number:step]:
                    yield n
            elif first != 0 and step == 0:
                for n in rlist[(first-1):(number-1)]:
                    yield n
            elif first != 0:
                for n in rlist[(first-1):(number-1)]:
                    yield n
            else:
                for n in rlist[first:number]:
                    yield n
    elif first != 0:
        number = first
        rlist = [0]
        while True:
            if len(rlist) ==  1:
                rlist += [len(rlist)]
            elif rlist[-1] < number:
                rlist += [abs(~rlist[-1])]
            elif rlist[-1] == number:
                    break
        for n in rlist[0:number]:
            yield n
    else:
        return

if __name__ == '__main__':
    trange()
