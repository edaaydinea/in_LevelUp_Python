import csv

def merge_csv(input_files, output_file):
  """Merges multiple CSV files into a single CSV file.

  Args:
    input_files: A list of file paths to CSV files to merge.
    output_file: The file path to save the resulting CSV file.
  """

  with open(output_file, 'w', newline='') as output_csv:
    writer = csv.writer(output_csv)

    for input_file in input_files:
      with open(input_file, 'r') as input_csv:
        reader = csv.reader(input_csv)
        header = next(reader)  # Read the header row
        writer.writerow(header)  # Write the header to the output file
        for row in reader:
          writer.writerow(row)

if __name__ == '__main__':
  merge_csv(['class1.csv', 'class2.csv'], 'all_students.csv')