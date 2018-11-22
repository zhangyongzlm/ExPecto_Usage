#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 11/5/2018 2:05 PM
# @Author  : Yong


import pandas as pd
import numpy as np

input_data = 'data/ExpressionData/IMR90.ENCC.count.TPM.FPKM.txt'
geneanno = "data/ExpressionData/geneanno.csv"

exp = pd.read_table(input_data)
exp['id'] = exp.gene_id.str.split('_', expand=True)[0]
exp['symbol'] = exp.gene_id.str.split('_', expand=True)[1]
gene_exp = pd.DataFrame(exp[['id', 'FPKM']])
gene_exp['logFPKM'] = np.log2(gene_exp['FPKM'])
# gene_exp[gene_exp['logFPKM'] == float('-inf')] = None

# print(gene_exp.head())
gencode19_df = pd.read_csv(geneanno)

# result = pd.merge(gene_exp.sort_values('id'), gencode19_df.sort_values('id'), how='right', on='id')
result = pd.merge(gene_exp, gencode19_df, how='right', on='id').sort_values('id')

result.to_csv('data/ExpressionData/gene_exp_merge.csv', header=True, index=False, line_terminator='\n')

# geneanno_ENCC = result[['id', 'symbol', 'seqnames', 'strand', 'TSS', 'CAGE_representative_TSS', 'type']]
# geneanno_ENCC.to_csv('data/ExpressionData/geneanno_ENCC.csv', header=True, index=False, line_terminator='\n')

geneanno_exp_ENCC = pd.DataFrame(result['logFPKM'])
geneanno_exp_ENCC.name = 'ENCC'
geneanno_exp_ENCC.to_csv('data/ExpressionData/geneanno.exp_ENCC.csv', header=True, index=True)


