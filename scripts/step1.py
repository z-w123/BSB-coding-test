#!/usr/bin/env python3

import pandas as pd
import os

path = "./coding-test-advanced/data/breaks/"
breakend_files = [f.path for f in os.scandir(path)] # full path + file name
#print(breakend_files)

sample_id = lambda string: (os.path.basename(string)).rsplit(".")[0] # extract only sample id from from full path + file name


#create output directory for filtered bed files
if not os.path.exists("./output_dir"):
    try:
        os.makedirs("./output_dir")
        print(f"Successfully created output directory")
    except Exception as error:
        print(error)
        print(
            f"\n ERROR could not create output directory.")


def filter_files(file, threshold):
    with open(file, 'r', newline='') as f:
        df = pd.read_csv(f, delimiter='\t')

    df.columns = ['chrom', 'start', 'end', 'col3', 'mapQ', 'orientation']

    filtered_df = df.loc[df['mapQ'] >= 30]

    # filtered_df.to_csv('filtered.bed', sep='\t', header=False, index=False) #write to file without header and index #full bed file
    filtered_df.to_csv(f"./output_dir/{sample_id(file)}_filtered_trunc.bed", sep='\t', columns=['chrom', 'start', 'end'], header=False, index=False) # keeping same cols as in chr21_AsiSI_sites.t2t.bed for step 2

for bf in breakend_files:
    filter_files(bf, 30)
