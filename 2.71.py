import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

# Function to preprocess the content of a file
def preprocess_file(file_path):
    cleaned_lines = []
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        cleaned_lines.append(text)
    return cleaned_lines

# Function to process all text files in the source directory
def process_directory(source_directory):
    preprocessed_texts = []
    file_names = []

    for filename in os.listdir(source_directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(source_directory, filename)
            cleaned_lines = preprocess_file(file_path)
            preprocessed_texts.extend(cleaned_lines)
            file_names.append(filename)

    return preprocessed_texts, file_names

if __name__ == "__main__":
    source_directory = r'C:\Users\1234\OneDrive - 인하대학교\바탕 화면\ESG_Logistics\2.6_Korea_KLN_Filtered_POS_Texts'
    preprocessed_texts, file_names = process_directory(source_directory)

    # Initialize TfidfVectorizer with min_df parameter
    tfidf_vectorizer = TfidfVectorizer(min_df=2)  # Set min_df to 2 to exclude terms that appear in only one document

    # Compute TF-IDF scores for the preprocessed texts
    tfidf_matrix = tfidf_vectorizer.fit_transform(preprocessed_texts)

    # Convert TF-IDF matrix to dense array
    tfidf_dense = tfidf_matrix.toarray()

    # Output directory for TF-IDF results
    output_directory = r'C:\Users\1234\OneDrive - 인하대학교\바탕 화면\ESG_Logistics\2.71_Korea_KLN_TFIDF_Results'

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Write TF-IDF results to text files
    for i, filename in enumerate(file_names):
        result_file_path = os.path.join(output_directory, f"tfidf_{filename}")

        # Write TF-IDF scores for the current document to a text file
        with open(result_file_path, 'w', encoding='utf-8') as result_file:
            for j, word in enumerate(tfidf_vectorizer.get_feature_names_out()):
                result_file.write(f"{word}: {tfidf_dense[i][j]}\n")

        print(f"TF-IDF results for {filename} saved to {result_file_path}")
