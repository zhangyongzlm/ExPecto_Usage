#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 9/11/2018 4:06 PM
# @Author  : Yong ZHANG

gencode19 = "data/gencode.v19.annotation.gtf_withproteinids"
gencode19_cut = "data/gencode.v19.annotation.gtf_withproteinids.bed"

with open(gencode19, 'rt') as fin, open(gencode19_cut, 'wt', newline='') as fout:
    for line in fin:
        if line.startswith("#"):
            continue
        else:
            fields = line.strip().split('\t')
            if fields[2] != 'gene':
                continue
            chrom = 'chr' + fields[0]
            if fields[6] == '+':
                start_pos = str(int(fields[3]) - 1)
                end_pos = fields[3]
            else:
                start_pos = str(int(fields[4]) - 1)
                end_pos = fields[4]
            strand = fields[6]
            gene_id = fields[-1].split(';')[0].split('"')[1].split('.')[0]
            line_out = '\t'.join([chrom, start_pos, end_pos, strand, gene_id])
            print(line_out)
            print(line_out, file=fout, end='\n')


