#importing modules

import pandas as pd
from configparser import ConfigParser
import os
import glob
import logging
import pandas as pd
import os.path

logging.basicConfig(filename='C:/Users/abhi/PycharmProjects/pythonProject_11feb21/logs/logt',level=logging.DEBUG,filemode='a',format='%(asctime)s:%(levelname)s:%(message)s')
# Folders:
# client   : incoming excel sheets
# network  : merged excel files updated from the client folder
# config   : storing all paths
# log      : logging
# scripts  : main  script

# object creation of ConfigParser() class
config = ConfigParser()
configFilePath=r"C:/Users/abhi/PycharmProjects/pythonProject_11feb21/config/config.cfg"
print(config.read(configFilePath))

# Reading sections of config file
# print(config.sections())
# print(config["path"]["client"])
# print(config["path"]["logs"])
# print(config["path"]["scripts"])
#print(config["path"]["network"])

path_network=config["path"]["network"]
path_client=config["path"]["client"]
path_scripts=config["path"]["scripts"]
path_logs=config["path"]["logs"]


print(path_network)
print(path_client)
print(path_scripts)
print(path_logs)





class Student:
    # current = r"C:/Users/abhi/PycharmProjects/pythonProject_11feb21/client/"
    # b = os.listdir(current)
    # print(b)

    def students_data(self):
        print("program start")
        current = path_client
        print(current)
        b = os.listdir(current)
        print(b)

        try:
            if len(b) > 1:
                logging.info("Files are greater than 1")
                # i = 0
                # while i<=len(b):

                for file in b:
                    os.chdir("path_client")
                    extension = 'csv'
                    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
                    print(all_filenames)
                    # combine all files in the list
                    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
                    # export to csv
                    combined_csv.to_csv(path_network+"combinedf_csv.csv", index=False)

            elif len(b) == 0:
                logging.info("No file exist")
            else:
                logging.info("There is single file")

        except:
            logging.info("There was some error")

        finally:
            logging.info("Operation Completed")



s=Student()
s.students_data()






















#
# print("Importing Modules")
# print("File Exists")
# print("File doesnt exist")
# print("Merging the files")
# print("File merge completed")
# print("End of Program")
# print("Start of Program")





