Methodology

1.News Crawling: The initial step involves automated gathering of news articles from predefined sources, a process commonly referred to as 'crawling'. This phase populates the dataset for subsequent analysis.
(1) News Publishers - (2) News publisher's website - (3) Extract articles
① Crawling Google News for articles based on a list of keywords helps identify news publishers covering a specific topic.
②
③

2.Text Preprocessing: This critical phase prepares the raw text data for analysis through several sub-steps:
 (1) Word Segmentation - (2) Removing Redundant Data - (3) Removing the Null - (4) Removing Irrelevant Content - (5) Removing Stop Words - (6) Term Frequency-Inverse Document Frequency (TF-IDF)
  ①The text is divided into discrete units or tokens, typically words or phrases.
  ②Any duplicated content within the dataset is identified and eliminated to improve processing efficiency and accuracy.
  ③Entries that are empty or have missing values are discarded as they do not contribute meaningful information for analysis.
  ④Text elements that do not contribute to the understanding of the content, such as numbers or punctuation, are removed.
  ⑤Commonly occurring words (e.g., "the", "is", "at") which are deemed irrelevant for topic modeling are filtered out.
  ⑥Statistical measure is computed for each word to reflect its importance in the corpus. Term Frequency denotes the frequency of a word in a document, while Inverse Document Frequency diminishes the weight of terms that occur very frequently across the document set and increases the weight of terms that occur rarely.

3.Latent Dirichlet Allocation (LDA) is a generative statistical model that allows sets of observations to be explained by unobserved groups that explain why some parts of the data are similar. In this context, it helps in discovering topics that are present in a corpus.

4.Main Topics: The outcome of the LDA is a set of topics that are prevalent across the news articles. Each topic is characterized by a cluster of words with a certain probability distribution, representing different themes extracted from the text data.

File Names_Python
1.News Crawling: 1.1.NC - 1.2.NC - 1.3.NC
2.Text Preprocessing: 2.1.TP - 2.2.TP - 2.3.TP - 2.4.TP - 2.5.TP - 2.6.TP
