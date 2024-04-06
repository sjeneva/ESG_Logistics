import os
import nltk
from nltk.corpus import stopwords
from gensim import corpora, models
from gensim.utils import simple_preprocess

# Function to read text from a file
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Download the stopwords from NLTK
nltk.download('stopwords')

# Path to the input and output directories
input_dir = r'Separated_Files_2.6'
output_dir = r'Separated_Files_3.3'

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Set up stopwords
stop_words = set(stopwords.words('english'))

# Process each file
for filename in os.listdir(input_dir):
    if filename.endswith('.txt'):
        # Read and preprocess the text
        file_path = os.path.join(input_dir, filename)
        text = read_text_file(file_path)
        processed_text = simple_preprocess(text)
        filtered_text = [word for word in processed_text if word not in stop_words]

        # Create a dictionary and corpus for LDA
        dictionary = corpora.Dictionary([filtered_text])
        corpus = [dictionary.doc2bow(filtered_text)]

        # Build the LDA model with specified parameters
        lda_model = models.LdaModel(
            corpus=corpus,
            id2word=dictionary,
            num_topics=1,
            random_state=100,
            update_every=100,
            chunksize=100,
            passes=100,
            alpha='auto',
            per_word_topics=True
        )

        # Save the topics to a new file
        output_filepath = os.path.join(output_dir, f'topics_{filename}')
        with open(output_filepath, 'w', encoding='utf-8') as f:
            for idx in range(lda_model.num_topics):
                # Get the words and their probabilities for the topic
                words_and_probs = lda_model.show_topic(idx, topn=5)
                # Format the topic as a string
                formatted_topic = ", ".join([f"{word} ({prob:.2f})" for word, prob in words_and_probs])
                f.write(f"Topic {idx}: {formatted_topic}\n")

# If needed, print the path to the output directory
print(f"Topics saved to the directory: {output_dir}")
