#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 12/3/2018 3:12 PM
# @Author  : Yong
import pandas as pd


vcf = pd.read_table('data/variants_0.001.vcf', header=None, names=['CHROM', 'POS', '-', 'REF', 'ALT'])
vcf.insert(1, 'POS_0', vcf['POS']-1)
vcf.sort_values(by=['CHROM', 'POS'], inplace=True)
vcf.to_csv('data/variants_0.001_for_closest-features.vcf', columns=['CHROM', 'POS_0', 'POS'], sep='\t', header=False, index=False)
