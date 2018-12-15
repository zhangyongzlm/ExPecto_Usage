#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 12/14/2018 3:30 PM
# @Author  : Yong

import argparse
import pandas as pd
import numpy as np

parser = argparse.ArgumentParser(description='Statistics for variant effects on gene expression')
parser.add_argument('geneName', type=str, action='store', help='Path of the csv file with gene names')
parser.add_argument('origEffects', type=str, action='store', help='Path of the original variant effects')
args = parser.parse_args()

gene_name = pd.read_csv(args.geneName, usecols=['id', 'symbol'])
gene_name.rename(columns={'id': 'gene_id', 'symbol': 'gene_name'}, inplace=True)
# print(gene_name.head())

effects = pd.read_csv(args.origEffects, usecols=['0', '1', '3', '4', 'gene', 'strand', 'ENCC'])
effects.columns = ['chr', 'pos', 'Ref', 'Alt', 'gene_id', 'strand', 'ENCC']
effects['ENCC'] = effects['ENCC'].astype('float64')
# print(effects.head())

effects_gene_name = pd.merge(effects, gene_name, on=['gene_id'], how='left')
effects_gene_name = effects_gene_name.reindex(columns=['chr', 'pos', 'Ref', 'Alt', 'gene_id', 'gene_name', 'strand', 'ENCC'])
effects_gene_name.to_csv(args.origEffects[:-4] + '_withGeneName_sortByPos.csv', index=None)
# print(effects_gene_name.head())

effects_gene_name_sorted = effects_gene_name.sort_values(by='gene_name')
effects_gene_name_sorted.to_csv(args.origEffects[:-4] + '_withGeneName_sortByGene.csv', index=None)

grouped = effects_gene_name.groupby('gene_name')
grouped_stat = grouped['ENCC'].agg([np.std, np.mean])
grouped_stat.to_csv(args.origEffects[:-4] + '_withGeneName_stat.csv')

print('Finished!')
