# BSB-coding-test

Python code for steps 1 -4 of the data processing pipeline can be found in the scripts/ folder.    

Please note that 'bedtools' should be installed prior to running. This can be installed here: https://bedtools.readthedocs.io/en/latest/content/installation.html

## Answers to questions
1. The control samples are: Samples 1-2 and Samples 4-8 (inclusive) as the breakends have no overlaps with ASISI sites. Treated samples are Sample 3 and Samples 9-16 as the breakend files show >0 overlaps with ASISI sites.    
2. Sample 3 could be uncertain as it has the next lowest number of overlaps with ASISI sites (1) and the second lowest normalised ASISI break number
3. unsure/as above
4. There are 71 ASISI sites in total in the chr21_AsiSI_sites.t2t.bed file. The maximum number of overlaps with ASISI sites in any sample is 18, from Sample 16. 18/71 * 100 = 25.35% maximum percentage observed in a single sample.
