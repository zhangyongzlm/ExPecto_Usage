# ExPecto_Usage
Specification of how to use ExPecto to predict variant's effect on gene expression when applying to our own data
## Computes the chromatin effects of the variants, using trained convolutional neural network model
```
python chromatin.py ./example/example.vcf
```
The input file *example.vcf* is the standard vcf format. The seperator is the table sign. The screenshot is as following.
![](Pictures/example_vcf.png)



## Computes predicted tissue-specific expression effects which takes predicted chromatin effects as input
```
python predict.py --coorFile ./example/example.vcf --geneFile ./example/example.vcf.bed.sorted.bed.closestgene --snpEffectFilePattern ./example/example.vcf.shift_SHIFT.diff.h5 --modelList ./resources/modellist --output output.csv
```
`--closestGeneFile ./example/example.vcf.bed.sorted.bed.closestgene`  The screenshot is as following.

![](Pictures/example.vcf.bed.sorted.bed.closestgene.png)