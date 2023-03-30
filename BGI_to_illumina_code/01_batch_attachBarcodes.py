#!/bin/python
import os
import multiprocessing
import pandas as pd

## Please specify the sequencing info in the first place
BGI_prefix="V300079632"
##     [Lane, Name, Index]
lst = [[3, "31GEX", "GCAACAAA"],
       [3, "31GEX", "TAGTTGTC"],
       [3, "31GEX", "CGCCATCG"],
       [3, "31GEX", "ATTGGCGT"]]
attachBarcodes_shell="attachBarcodes.sh"







df = pd.DataFrame(lst, columns =['Lane', 'Sample', 'Barcode'], dtype = str)
def worker(inpfile, outfile, barcode):
    cmd = f"bash {attachBarcodes_shell} {infile} {outfile} {barcode}"
    os.system(cmd)


jobs = []

for row in df.index:
    a_row = df.iloc[row]
    lane = a_row["Lane"]
    bc = a_row["Barcode"]
    sample = a_row["Sample"]

    if not os.path.exists(f"CRData/BC_Attached/{sample}"):
        os.mkdir(f"CRData/BC_Attached/{sample}")

    for strand in [1,2]:
        infile = f"CRData/BGI/{sample}/{BGI_prefix}_L0{lane}_1_{sample}_{strand}.fq.gz"
        outfile = f"CRData/BC_Attached/{sample}/{sample}_{bc}_L00{lane}_R{strand}.fastq.gz"
        p = multiprocessing.Process(target=worker, args=(infile, outfile, bc))
        jobs.append(p)
        p.start()

for proc in jobs:
    proc.join()

