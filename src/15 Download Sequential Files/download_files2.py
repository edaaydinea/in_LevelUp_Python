import os
import re
import urllib.parse
import urllib.request


def download_files(base_url, output_dir):
  """Downloads a sequence of files from a base URL with sequential numbering.

  Args:
    base_url: The base URL for the first file in the sequence (e.g., http://...).
    output_dir: The directory path where downloaded files will be saved.
  """
  os.makedirs(output_dir, exist_ok=True)  # Create output directory if not exists

  # Extract filename pattern from base URL (assuming numbering at the end)
  filename_pattern = re.search(r".*/([^/]+)$", base_url).group(1)
  number_match = re.search(r"(\d+)", filename_pattern)

  # Check if numbering pattern is found
  if not number_match:
    raise ValueError("Could not extract numbering pattern from base URL")

  # Loop through the sequence (modify range as needed)
  for i in range(1, 51):  # Assuming 50 files
    # Format filename with padding
    formatted_number = str(i).zfill(len(number_match.group(1)))
    filename = filename_pattern.replace(number_match.group(1), formatted_number)

    # Construct the full URL
    full_url = urllib.parse.urljoin(base_url.rsplit('/', 1)[0], filename)

    # Construct the full path for the downloaded file
    filepath = os.path.join(output_dir, filename)

    try:
      # Download the file
      urllib.request.urlretrieve(full_url, filepath)
      print(f"Downloaded {filepath}")
    except urllib.error.URLError as e:
      print(f"Error downloading {full_url}: {e}")

if __name__ == '__main__':
  download_files('http://699340.youcanlearnit.net/image001.jpg', './images')