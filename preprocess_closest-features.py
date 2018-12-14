#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 12/3/2018 3:12 PM
# @Author  : Yong
import pandas as pd
import argparse


parser = argparse.ArgumentParser(description='Convert the 1-based variant file to the 0-based variant file')
parser.add_argument('inFile', type=str, action='store',
                    help='Path of the input file in 1-based position')
parser.add_argument('outFile', type=str, action='store',
                    help='Path of the output file in 0-based position')
args = parser.parse_args()

vcf = pd.read_table(args.inFile, header=None, names=['CHROM', 'POS', '-', 'REF', 'ALT'])
vcf.insert(1, 'POS_0', vcf['POS']-1)
vcf.sort_values(by=['CHROM', 'POS'], inplace=True)
vcf.to_csv(args.outFile, columns=['CHROM', 'POS_0', 'POS'], sep='\t', header=False, index=False)
