# Convert BGI to Illumina pipeline

## A example sample Info

| Sample_ID | Name    | Index 7  | Lane  |
| --------- | ------- | -------- | ----- |
| Truseq06  | 1_31GEX | GCAACAAA | Lane3 |
| Truseq06  | 2_31GEX | TAGTTGTC | Lane3 |
| Truseq06  | 3_31GEX | CGCCATCG | Lane3 |
| Truseq06  | 4_31GEX | ATTGGCGT | Lane3 |



### FileNames are like:

| ID  | reads                                                             |
| --- | ----------------------------------------------------------------- |
| 1   | V300079632_L03_1_31GEX_1.fq.gz<br/>V300079632_L03_1_31GEX_2.fq.gz |
| 2   | V300079632_L03_2_31GEX_1.fq.gz<br/>V300079632_L03_2_31GEX_2.fq.gz |
| 3   | V300079632_L03_3_31GEX_1.fq.gz<br/>V300079632_L03_3_31GEX_2.fq.gz |
| 4   | V300079632_L03_4_31GEX_1.fq.gz<br/>V300079632_L03_4_31GEX_2.fq.gz |



### Folders

```shell
CRData
├── BC_Attached ## output of 01_batch_attachBarcodes.py
│   └── 31GEX
│       ├── 31GEX_ATTGGCGT_L003_R1.fastq.gz
│       ├── 31GEX_ATTGGCGT_L003_R2.fastq.gz
│       ├── 31GEX_CGCCATCG_L003_R1.fastq.gz
│       ├── 31GEX_CGCCATCG_L003_R2.fastq.gz
│       ├── 31GEX_GCAACAAA_L003_R1.fastq.gz
│       ├── 31GEX_GCAACAAA_L003_R2.fastq.gz
│       ├── 31GEX_TAGTTGTC_L003_R1.fastq.gz
│       └── 31GEX_TAGTTGTC_L003_R2.fastq.gz
├── BGI ## original BGI data
│   └── 31GEX
│       ├── V300079632_L03_1_31GEX_1.fq.gz
│       ├── V300079632_L03_1_31GEX_2.fq.gz
│       ├── V300079632_L03_2_31GEX_1.fq.gz
│       ├── V300079632_L03_2_31GEX_2.fq.gz
│       ├── V300079632_L03_3_31GEX_1.fq.gz
│       ├── V300079632_L03_3_31GEX_2.fq.gz
│       ├── V300079632_L03_4_31GEX_1.fq.gz
│       └── V300079632_L03_4_31GEX_2.fq.gz
├── Converted ## output of 02_run_convertHeaders.py
│   └── 31GEX ## can take this as input of cellranger
│       ├── 31GEX_S1_L003_R1_001.fastq.gz
│       ├── 31GEX_S1_L003_R2_001.fastq.gz
│       ├── 31GEX_S2_L003_R1_001.fastq.gz
│       ├── 31GEX_S2_L003_R2_001.fastq.gz
│       ├── 31GEX_S3_L003_R1_001.fastq.gz
│       ├── 31GEX_S3_L003_R2_001.fastq.gz
│       ├── 31GEX_S4_L003_R1_001.fastq.gz
│       └── 31GEX_S4_L003_R2_001.fastq.gz


```



### Pipeline step

1. `python3 01_batch_attachBarcodes.py` to attach barcode to fastq file

   > Please set `BGI_prefix`(V300079632 in our case) & `lst` before running the script

2. `python 3 02_run_convertHeaders.py` to convert to cellranger input format

   > Please set dict `d` before running the script

3. `bash 03_homosapien_cellranger.sh` to run cellranger



Reference:
https://github.com/powellgenomicslab/BGI_vs_Illumina_Benchmark
https://github.com/IMB-Computational-Genomics-Lab/BGIvsIllumina_scRNASeq

