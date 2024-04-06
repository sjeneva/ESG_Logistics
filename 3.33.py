from wordcloud import WordCloud
import matplotlib.pyplot as plt

# File path to your text file
file_path = r'C:\Users\1234\OneDrive - 인하대학교\바탕 화면\ESG_Logistics\3.32_cleaned_topics.txt'
# Function to parse the file and extract words and weights
def parse_file(file_path):
    keywords = {}
    with open(file_path, 'r') as file:
        for line in file:
            if '(' in line and ')' in line:
                # Extract word and weight
                word, weight = line.split('(')
                weight = weight.replace(')', '').strip()
                keywords[word.strip()] = float(weight)
    return keywords

# Parse the file to get keywords and their weights
keywords = parse_file(file_path)

# Generate word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(keywords)

# Plot the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Hide axis
plt.title('Word Cloud of Keywords')
plt.show()
