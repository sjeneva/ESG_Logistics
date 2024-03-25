# It appears there was an error due to not defining 'pd'. Let's correct this by importing pandas and executing the operation again.
import pandas as pd

# Repeating the process with the corrected code
# Reading the file content
file_path = r'C:\Users\1234\OneDrive - 인하대학교\바탕 화면\ESG_Logistics\title.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.readlines()

# Extracting relevant lines
extracted_lines = [line.strip()[4:] for line in content if line.startswith('###')]

# Creating a DataFrame
df = pd.DataFrame(extracted_lines, columns=['Extracted Text'])

# Saving the DataFrame to an Excel file
excel_file_path = r'C:\Users\1234\OneDrive - 인하대학교\바탕 화면\ESG_Logistics\extracted_text.xlsx'
df.to_excel(excel_file_path, index=False)

excel_file_path
