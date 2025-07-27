import sys, os
from .. import config

def process_directory(full_path):
    csvfiles = [file for file in os.listdir(full_path) if file.endswith(config.SEARCHED_FILES)]
    print(csvfiles)
    files_processed = 0
    for csvfile in csvfiles:
        with open(os.path.join(full_path, csvfile), "r") as f:
            for line in f:
                print("LINE:", line)
        files_processed += 1