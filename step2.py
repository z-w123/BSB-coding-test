#!/usr/bin/env python3

#Note:  bedtools is required for this step and should already be installed

import step1
import os
import subprocess
import time

path = "./output_dir" # output directory for filtered bed files
filtered_breakend_files = [f.path for f in os.scandir(path)]

asisi_sites = "./coding-test-advanced/data/chr21_AsiSI_sites.t2t.bed"
# sample_id = lambda string: (os.path.basename(string)).rsplit(".")[0] # extract only sample id from from full path + file name
#print(step1.breakend_files)


def timer(func):
    def wrapper(*args): # to account for the arg for the output_overlaps() func
        start = time.time()
        func(*args)
        end = time.time()
        e_time = end - start # elapsed time
        print(f"{func} took {e_time}s to run")
    return wrapper

@timer # calculating elapsed time for below func
def output_overlaps(filtered_file):
    try:
        subprocess.run(f"bedtools intersect -a {filtered_file} -b {asisi_sites} > ./output_dir/asisi_breaks_{step1.sample_id(filtered_file)}.txt", shell=True, check=True)
        #print("bedtools intersect run successfully")
    except Exception as e:
        print("Error running bedtools intersect command", e)

for fbf in filtered_breakend_files:
    output_overlaps(fbf)







# a = pybedtools.BedTool('filtered.bed')
# b = pybedtools.BedTool('chr21_AsiSI_sites.t2t.bed')
#
# a.intersect(b).saveas('test_pybedtools.bed')
#bedtools intersect to output overlaps + sum number of lines

#bedtools intersect -a filtered.bed -b ./coding-test-advanced/data/chr21_AsiSI_sites.t2t.bed