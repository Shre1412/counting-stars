#! python3
# remove-csv-header.py - Removes the header from all CSV files in the current working directory

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

# Loop through every file in the current working directory.
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue # skip non-csv files

    print('Removing header from ' + csvFilename + '...')

    # Read the CSV file in (skipping first row).
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue # skip first row
        csvRows.append(row)
    csvFileObj.close()

    # Write out the CSV file.
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()

# Find all the CSV files in the current working directory
# Loop over a list of files from os.listdir(), skipping the non-CSV files
# Read the full contents of each file
# Create a CSV Reader object and read in the contents of the file, using the line_num attribute to figure out which line to skip
# Write out the contents, skipping the first line, to a new CSV file
# Create a CSV Writer object and write out the read-in data to the new file