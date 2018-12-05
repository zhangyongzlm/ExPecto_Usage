#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 12/3/2018 11:54 AM
# @Author  : Yong


import pandas as pd
import argparse


parser = argparse.ArgumentParser(description='Standardize vcf form and filter variants based on P-value')
parser.add_argument('inFile', type=str, action='store', help='Path of the input file')
parser.add_argument('outFile', type=str, action='store', help='Path of the output file')
parser.add_argument('--threshold', '-T', dest='threshold', type=float, action='store', default=0.001,
                    help='P-value Threshold')
args = parser.parse_args()
# args = parser.parse_args('data/variants_Alex_orig data/variants_0.001.vcf'.split())

variants_orig = pd.read_csv(args.inFile, sep='\t')
variants_orig = variants_orig[variants_orig.PVALUE < args.threshold]
variants_orig['chr'] = 'chr'
variants_orig['CHROM'] = variants_orig.CHROM.astype(str)
variants_orig['CHROM'] = variants_orig['chr'] + variants_orig['CHROM']
variants_orig['-'] = '-'
variants_orig.to_csv(args.outFile, columns=['CHROM', 'POS', '-', 'REF', 'ALT'], header=False, index=False, sep='\t')
