import csv
import os
from PIL import Image
from datetime import datetime

def combine_images(fabric_path, sofa_path, output_path):
    # Open the fabric and sofa images
    fabric = Image.open(fabric_path)
    sofa = Image.open(sofa_path)

    # Resize images to fit 250x500 dimensions (half the output image size)
    fabric = fabric.resize((500, 250))  # Fabric will be at the bottom, 250px tall
    sofa = sofa.resize((500, 250))     # Sofa will be at the top, 250px tall

    # Create a new blank image with size 500x500
    combined_image = Image.new('RGB', (500, 500))

    # Paste the sofa image (top)
    combined_image.paste(sofa, (0, 0))  # Place sofa on the top (0, 0)
    # Paste the fabric image (bottom)
    combined_image.paste(fabric, (0, 250))  # Place fabric on the bottom (0, 250)

    # Save the combined image
    combined_image.save(output_path)

def generate_timestamp_filename():
    # Generate a filename using the current timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_%f')  # e.g., 20250312_102800_123456
    return f"{timestamp}.png"

def process_csv(input_csv, output_folder, fabric_folder, sofa_folder):
    # Read the CSV file and create a list of rows
    rows = []
    with open(input_csv, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        
        # Debug: Print the headers of the CSV file
        print("CSV Headers:", reader.fieldnames)

        for row in reader:
            # Clean up headers by stripping any extra spaces
            row = {key.strip(): value for key, value in row.items()}
            
            # Debug: Print the row content
            print("Processing Row:", row)
            
            try:
                fabric_filename = row['file_1']
                sofa_filename = row['file_2']
                
                # Generate a timestamp-based filename for the result image
                result_filename = generate_timestamp_filename()
                
                # Construct the full paths for the images
                fabric_path = os.path.join(fabric_folder, fabric_filename)
                sofa_path = os.path.join(sofa_folder, sofa_filename)
                result_path = os.path.join(output_folder, result_filename)
                
                # Combine the images
                combine_images(fabric_path, sofa_path, result_path)
                
                # Add the result filename to the row and append to rows list
                row['result'] = result_filename
                rows.append(row)
                
                # Debug: Print the result filename
                print(f"Saved combined image as {result_filename}")
            except KeyError as e:
                print(f"KeyError: Missing column {e} in CSV")

    # Write the updated CSV with result filenames
    with open(input_csv, 'w', newline='', encoding='utf-8-sig') as csvfile:
        fieldnames = ['file_1', 'file_2', 'result']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')

        # Write header
        writer.writeheader()

        # Write updated rows
        writer.writerows(rows)

# Example usage:
input_csv = 'data.csv'  # The path to your CSV file
output_folder = 'output_images'  # Folder to save the combined images
fabric_folder = 'file_1'  # Folder where fabric images are stored
sofa_folder = 'file_2'  # Folder where sofa images are stored

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Process the CSV and combine images
process_csv(input_csv, output_folder, fabric_folder, sofa_folder)
