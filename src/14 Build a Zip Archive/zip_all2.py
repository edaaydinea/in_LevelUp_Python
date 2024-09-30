import os
import zipfile

def zip_all(directory, extensions, output_filename):
  """Creates a ZIP archive containing files with specified extensions in a directory.

  Args:
    directory: The path to the top-level directory to include in the archive.
    extensions: A list of file extensions (including the dot) to include.
    output_filename: The path to the resulting ZIP archive.
  """
  with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zip_file:
    for root, _, files in os.walk(directory):
      for file in files:
        if any(file.endswith(ext) for ext in extensions):
          filepath = os.path.join(root, file)
          zip_file.write(filepath, os.path.relpath(filepath, os.path.join(directory, '..')))

if __name__ == '__main__':
  zip_all('my_stuff', ['.jpg', '.txt'], 'my_stuff.zip')