#!/bin/bash
import os
import pprint
import datetime
import multiprocessing


## Please specify the sequencing info in the first place
##   Index:    [reads, Name, Lane]
d = {"GCAACAAA":[1, "31GEX",3],
     "TAGTTGTC":[2, "31GEX",3],
     "CGCCATCG":[3, "31GEX",3],
     "ATTGGCGT":[4, "31GEX",3]}



def worker(inputfile, outputfile):
    cmd = f"python convertHeaders.py -i {inputfile} -o {outputfile}"
    os.system(cmd)

jobs = []
for k, v in d.items():
    S = v[0]
    ID = v[1]
    L = v[2]
    print(datetime.datetime.now(), "processing: ", k, v)
    if not os.path.exists(f"CRData/Converted/{ID}"):
        os.mkdir(f"CRData/Converted/{ID}")

    for strand in [1,2]:
        inputfile = f"CRData/BC_Attached/{ID}/{ID}_{k}_L00{L}_R{strand}.fastq.gz"
        outputfile = f"CRData/Converted/{ID}/{ID}_S{S}_L00{L}_R{strand}_001.fastq.gz"
        if not (os.path.exists(inputfile)):
            print("no file named:", inputfile)
            continue

        p = multiprocessing.Process(target=worker, args=(inputfile, outputfile))
        jobs.append(p)
        p.start()

for proc in jobs:
    proc.join()
