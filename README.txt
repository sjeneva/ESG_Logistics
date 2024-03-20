
1.News Crawling: The initial step involves automated gathering of news articles from predefined sources, a process commonly referred to as 'crawling'. This phase populates the dataset for subsequent analysis.
(1) News Publishers - (2) News publisher's website - (3) Extract articles - (4) Translate
File Names in Python: 1.1.NC - 1.2.NC - 1.3.NC - 1.4.NC

① Crawling Google News for articles based on a list of keywords helps identify news publishers covering a specific topic.
   Result will be in EXCEL File 1.1.NC_Korea, 1.1.NC_USA
②
③
④

2.Text Preprocessing: This critical phase prepares the raw text data for analysis through several sub-steps:
(1) Word Segmentation - (2) Removing Redundant Data - (3) Removing the Null - (4) Removing Irrelevant Content - (5) Removing Stop Words - (6) Term Frequency-Inverse Document Frequency (TF-IDF)
File Names in Python: 2.1.TP - 2.2.TP - 2.3.TP - 2.4.TP - 2.5.TP - 2.6.TP

① The text is divided into discrete units or tokens, typically words or phrases.
   [Use tokenization functions from libraries like NLTK or spaCy.]

② Any duplicated content within the dataset is identified and eliminated to improve processing efficiency and accuracy.
   [Implement Python scripts to detect and remove duplicates or irrelevant data entries.]

③ Entries that are empty or have missing values are discarded as they do not contribute meaningful information for analysis.
   [Use pandas DataFrame methods like .dropna() to remove or .fillna() to impute null values.]

④ Text elements that do not contribute to the understanding of the content, such as numbers or punctuation, are removed.
   [Manually define criteria for relevance and use scripts to filter out non-compliant data]
   [Use supervised learning to classify and remove irrelevant content automatically.]

⑤ Commonly occurring words (e.g., "the", "is", "at") which are deemed irrelevant for topic modeling are filtered out.
   [Utilize stop words lists provided by NLTK, spaCy, or other NLP libraries to filter them out of the text.]

⑥ Statistical measure is computed for each word to reflect its importance in the corpus. Term Frequency denotes the frequency of a word in a document, while Inverse Document Frequency diminishes the weight of terms that occur very frequently across the document set and increases the weight of terms that occur rarely.
   [Use the TfidfVectorizer from scikit-learn to compute TF-IDF scores for words in your documents.]

3.Latent Dirichlet Allocation (LDA) is a generative statistical model that allows sets of observations to be explained by unobserved groups that explain why some parts of the data are similar. In this context, it helps in discovering topics that are present in a corpus.
  [Apply LDA using libraries like Gensim, specifying the number of topics and other hyperparameters. Analyze the topics and their distributions across the documents.]

4.Main Topics: The outcome of the LDA is a set of topics that are prevalent across the news articles. Each topic is characterized by a cluster of words with a certain probability distribution, representing different themes extracted from the text data.

