import os
import sys

def search_files(directory, keyword):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as file_content:
                for line_number, line in enumerate(file_content, start=1):
                    if keyword in line:
                        print(f"Keyword '{keyword}' found in file '{file_path}', line {line_number}: {line.strip()}")

# Get the directory path and keyword from command-line arguments
directory = sys.argv[1]
keyword = sys.argv[2]

# Search for the keyword in files
search_files(directory, keyword)