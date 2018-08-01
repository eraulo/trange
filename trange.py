#!/usr/bin/env python

__author__ = "Mariano de Deus"
__email__ = "dedeus_mariano@yahoo.com"

def Range(first=0, number=0, step=0 ):
    if (first or number or step) and number:
        if number:
            tlist = [first]
            while True:
                if len(tlist) ==  1:
                    if tlist[0] == 0:
                        tlist += [len(tlist)]
                    else:
                        tlist += [abs(~len(tlist))]
                elif tlist[-1] < number:
                    tlist += [abs(~tlist[-1])]
                elif tlist[-1] == number:
                    break
            if first != 0 and step != 0:
                for n in tlist[(first-1):(number-1):step]:
                    yield n
            elif first == 0 and step != 0:
                for n in tlist[first:number:step]:
                    yield n
            elif first != 0 and step == 0:
                for n in tlist[(first-1):(number-1)]:
                    yield n
            elif first != 0:
                for n in tlist[(first-1):(number-1)]:
                    yield n
            else:
                for n in tlist[first:number]:
                    yield n
    elif first != 0:
        number = first
        tlist = [0]
        while True:
            if len(tlist) ==  1:
                tlist += [len(tlist)]
            elif tlist[-1] < number:
                tlist += [abs(~tlist[-1])]
            elif tlist[-1] == number:
                    break
        for n in tlist[0:number]:
            yield n
    else:
        return

if __name__ == '__main__':
    Range()
