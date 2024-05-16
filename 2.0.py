import os


def extract_specific_part_from_text(text, start_marker, end_marker):
    """
    Extracts a specific part of the text between two markers.

    Args:
    text: The full text from which to extract the specific part.
    start_marker: The start marker of the specific part.
    end_marker: The end marker of the specific part.

    Returns:
    The extracted part of the text, or None if the markers are not found.
    """
    start_index = text.find(start_marker)
    if start_index != -1:
        end_index = text.find(end_marker, start_index)
        if end_index != -1:
            return text[start_index:end_index + len(end_marker)]
    return None


def process_files(source_directory_path, result_directory_path):
    """
    Processes all text files in the source directory to extract specific parts of the text,
    and saves those parts into new files in the result directory.
    """
    if not os.path.exists(result_directory_path):
        os.makedirs(result_directory_path)

    for filename in os.listdir(source_directory_path):
        if filename.endswith('.txt'):
            source_file_path = os.path.join(source_directory_path, filename)
            with open(source_file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                extracted_text = extract_specific_part_from_text(text, "_닫기_", "__**")
                if extracted_text:
                    result_file_path = os.path.join(result_directory_path, f"extracted_{filename}")
                    with open(result_file_path, 'w', encoding='utf-8') as result_file:
                        result_file.write(extracted_text)
                    print(f"Extracted text from {filename} saved to {result_file_path}")
                else:
                    print(f"No specific part found in {filename}.")


if __name__ == "__main__":
    source_directory_path = r'Korea_KLN_사회_extracted_articles'
    result_directory_path = r'2.0_Korea_KLN_사회_extracted_articles'
    process_files(source_directory_path, result_directory_path)
