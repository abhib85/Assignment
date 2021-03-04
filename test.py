import pandas as pd
from configparser import ConfigParser
import os
import glob
import logging
import os.path



os.chdir("C:/Users/abhi/PycharmProjects/pythonProject_11feb21/client/")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
print(all_filenames)
#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
#export to csv
combined_csv.to_csv(r"C:/Users/abhi/PycharmProjects/pythonProject_11feb21/network/combinedttt_csv.csv", index=False)
