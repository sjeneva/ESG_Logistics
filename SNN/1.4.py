import glob
import os
import re

# Define paths
directory_path = r'C:\Users\1234\OneDrive - 인하대학교\바탕 화면\ESG_Logistics\SNN\Korea_SNN_환경_extracted_articles'
output_dir = r'C:\Users\1234\OneDrive - 인하대학교\바탕 화면\ESG_Logistics\SNN\1.4_Korea_SNN_환경_extracted_articles'
os.makedirs(output_dir, exist_ok=True)

# Define the markers for extraction
markers = [
    {"start": "_닫기_", "ends": ["__**쉬핑뉴스넷**", "__*"]}
]


# Function to extract content between markers
def extract_content(content, start_marker, ends):
    start_index = content.find(start_marker)
    end_indexes = [content.find(end, start_index) for end in ends if content.find(end, start_index) != -1]
    if start_index != -1 and end_indexes:
        end_index = min(end_indexes)
        return content[start_index + len(start_marker):end_index].strip()
    return None


# Function to clean and debug the text
def clean_text(text):
    url_pattern = re.compile(r'https?://\S+')
    text = url_pattern.sub('', text)
    related_articles_pattern = re.compile(
        r'####\s+관련기사\s*\n(\s*[-*•\s]?\s*\[.*?\]\((?:/|\.\./|\.\./\.\./)news/articleView\.html\?idxno=\d+\)\s*[\r\n]+)+',
        re.MULTILINE | re.DOTALL
    )
    text = related_articles_pattern.sub('', text)
    return text


def debug_text(text):
    pattern = re.compile(r'####\s+관련기사[\s\S]{0,500}')
    matches = pattern.findall(text)
    for match in matches:
        print("Match found:", repr(match))


# Process each .txt file
for file_path in glob.glob(os.path.join(directory_path, '*.txt')):
    filename = os.path.basename(file_path)
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Debugging the content to see what's being read
    debug_text(content)  # Make sure this line is inside the loop

    extracted_texts = []
    for marker in markers:
        extracted_text = extract_content(content, marker["start"], marker["ends"])
        if extracted_text:
            cleaned_text = clean_text(extracted_text)
            extracted_texts.append(cleaned_text)

    # Save each cleaned text to a separate txt file in the output directory
    for i, text in enumerate(extracted_texts, 1):
        output_file_path = os.path.join(output_dir, f"{filename}_extract_{i}.txt")
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(text)

print(f"Extracted texts have been saved in {output_dir}.")
