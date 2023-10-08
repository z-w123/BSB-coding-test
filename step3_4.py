#!/usr/bin/env python3
import pandas as pd
import os
import glob
import step1

path = "./output_dir/*.txt" # output directory for asisi break sites for each sample
asisi_break_samples = glob.glob(path)

asc_order = lambda f: int(''.join(filter(str.isdigit, f)))

dict = {}

def count_normalise_breaks(asisi_bfile, total_bfile):
    with open(f'{asisi_bfile}') as af:
        asisi_sum = len([ln for ln in (line.strip() for line in af) if ln]) #removes leading + trailing whitespaces from each line # line  count
    print(f"sum of asisi breaks in {asisi_bfile} is", asisi_sum)

    with open(f'{total_bfile}') as tf:
        total_breaks = len([ln for ln in (line.strip() for line in tf) if ln])
    print(f"total no. of breaks in {total_bfile} is", total_breaks)


    count_normalise_breaks.norm_val = asisi_sum / (total_breaks / 1000)
    print("normalised break value is", count_normalise_breaks.norm_val)

    return count_normalise_breaks.norm_val

asisi_break_samples.sort(key=asc_order), step1.breakend_files.sort(key=asc_order) #sorting list to keep samples together when zipping
zipped = zip(asisi_break_samples, step1.breakend_files)
#print(list(zipped))

for a_bf, t_bf in zipped:
    count_normalise_breaks(a_bf, t_bf)
    dict.update({step1.sample_id(t_bf): count_normalise_breaks.norm_val})

#print(dict)
normalise_df = pd.DataFrame(dict, index=['i',])
print(normalise_df)

normalise_df.to_csv(f"./output_dir/normalised_ASISI_sites.tsv", sep='\t', index=False) #combining normalised values for each sample in a single file


