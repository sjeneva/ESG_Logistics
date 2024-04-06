import os

def merge_text_files(input_dir, output_file):
    with open(output_file, 'w') as outfile:
        for file_name in os.listdir(input_dir):
            if file_name.endswith('.txt'):
                with open(os.path.join(input_dir, file_name), 'r') as infile:
                    outfile.write(infile.read() + '\n')

# Input directory containing text files
input_dir = r'C:\Users\1234\OneDrive - 인하대학교\바탕 화면\ESG_Logistics\Separated_Files_3.3'

# Output file name
output_file = r'C:\Users\1234\OneDrive - 인하대학교\바탕 화면\ESG_Logistics\3.31_merged.txt'

# Merge the files
merge_text_files(input_dir, output_file)

