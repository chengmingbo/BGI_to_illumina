#!/bin/bash

### Job name
#SBATCH -J 31GEX
#SBATCH -e logs/31GEX.txt
#SBATCH -o logs/31GEX.txt

### Time your job needs to execute, e. g. 15 min 30 sec
#SBATCH -t 400:00:00

### Memory your job needs per node, e. g. 1 GB
#SBATCH --mem=450G



################################################################
# PATH
#if [ -r /usr/local_host/etc/bashrc ]; then
#   . /usr/local_host/etc/bashrc
#fi
#
#export PATH=/usr/bin:$PATH
#export PATH=/usr/local_host/bin:$PATH
#source /home/sz753404/for-se/anaconda3/bin/activate
#conda activate r_env4s3
#source /home/sz753404/r4.0.Source
#module add scRNA/1.0.3
################################################################
# LIBRARYPATH



ID="31GEX"
echo "ID is " $ID

refer=/home/sz753404/data/project/BGI_to_illumia/CRData/reference/GRCh38_premRNA

cellranger count --id=$ID --fastqs=CRData/Converted/${ID}/ --sample=$ID --transcriptome=$refer
