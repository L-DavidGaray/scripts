# Author: David Garay #
# Script for making new csv with only relevant columns##
## how to use:	python3 clean_grading.py -f <filename.csv> 
import csv
import argparse
import pandas as pd
#import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", type=str)
args = parser.parse_args()
file = args.file

df = pd.read_csv(args.file, usecols=[2,7,12,21,22,28])
df.to_csv('/Users/d.garay/Documents/GradingTickets/VERIFIED_'+file, index=1)

print("\tclean file created")
