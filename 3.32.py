from collections import defaultdict

def cleanse_topics(text):
    # Initialize a defaultdict to store unique words for each topic
    unique_words_per_topic = defaultdict(set)

    # Split the text into lines
    lines = text.split('\n')

    # Iterate over each line
    for line in lines:
        # Split the line into words and extract the topic number and words
        parts = line.split(':')
        if len(parts) >= 2:  # Check if there are enough parts
            topic_number = parts[0].strip()
            words = parts[1].strip().split(', ')

            # Remove duplicates from the list of words
            unique_words = set(words)

            # Update the defaultdict with unique words for the corresponding topic
            unique_words_per_topic[topic_number].update(unique_words)

    # Prepare the cleaned text
    cleaned_text = ''
    for topic_number, words in unique_words_per_topic.items():
        cleaned_text += "Topic " + topic_number + ":\n"
        for word in words:
            cleaned_text += word + "\n"
        cleaned_text += "\n"

    return cleaned_text

with open(r"C:\Users\1234\OneDrive - 인하대학교\바탕 화면\ESG_Logistics\3.31_merged.txt", "r") as file:
    topics_text = file.read()

# Get the cleaned text
cleaned_text = cleanse_topics(topics_text)

# Write the cleaned text to a file
with open("3.32_cleaned_topics.txt", "w") as file:
    file.write(cleaned_text)

print("Cleaned topics have been written to cleaned_topics.txt")


