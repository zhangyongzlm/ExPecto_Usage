#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 12/15/2018 4:40 PM
# @Author  : Yong
import pandas as pd
import numpy as np

genes = pd.read_csv('data/geneanno.csv')
print(genes.head())

effects = pd.read_csv('data/variants_0.0001_AltEffects.csv', usecols=['0', '1', '3', '4', 'gene', 'strand', 'ENCC'])
print(effects.head())
