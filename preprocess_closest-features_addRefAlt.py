#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 12/3/2018 4:38 PM
# @Author  : Yong
import pandas as pd


vcf = pd.read_table('data/variants_0.001.vcf', header=None, names=['CHROM', 'POS', '-', 'REF', 'ALT'])
closestgene = pd.read_table('data/variants_0.001_for_closest-features.vcf.bed.sorted.bed.closestgene', header=None,
                            names=['CHROM', 'POS_0', 'POS', 'chr', 'TSS_0', 'TSS', 'Strand', 'Gene_ID', 'Dist'])

merged = pd.merge(closestgene, vcf, on=['CHROM', 'POS'], how='outer')
merged = merged.reindex(columns=['CHROM', 'POS_0', 'POS', 'REF', 'ALT', 'chr', 'TSS_0', 'TSS', 'Strand', 'Gene_ID', 'Dist'])

# print(vcf.head())
# print(closestgene.head())
# print(merged.head())

order_custom = ['chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8', 'chr9', 'chr10', 'chr11', 'chr12',
                'chr13', 'chr14', 'chr15', 'chr16', 'chr17', 'chr18', 'chr19', 'chr20', 'chr21', 'chr22', 'chrX', 'chrY']
merged['CHROM'] = merged['CHROM'].astype('category').cat.set_categories(order_custom)
merged.sort_values(by=['CHROM', 'POS'], ascending=True, inplace=True)

merged.to_csv('data/variants_0.001_for_closest-features.vcf.bed.sorted.bed.closestgene_RefAlt', sep='\t',
              index=False, header=False)
