#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 12/3/2018 11:54 AM
# @Author  : Yong


import pandas as pd


variants_orig = pd.read_csv('data/variants_Alex_orig', sep='\t')
variants_orig = variants_orig[variants_orig.PVALUE < 0.001]
variants_orig['chr'] = 'chr'
variants_orig['CHROM'] = variants_orig.CHROM.astype(str)
# print(variants_orig.dtypes)
variants_orig['CHROM'] = variants_orig['chr'] + variants_orig['CHROM']
variants_orig['-'] = '-'
variants_orig.to_csv('data/variants_0.001.vcf', columns=['CHROM', 'POS', '-', 'REF', 'ALT'], header=False, index=False,
                     sep='\t')
