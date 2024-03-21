
1.News Crawling: The initial step involves automated gathering of news articles from predefined sources, a process commonly referred to as 'crawling'. This phase populates the dataset for subsequent analysis.
(1) News Publishers - (2) News publisher's website - (3) Extract articles - (4) Translate
File Names in Python: 1.1.NC - 1.2.NC - 1.3.NC - 1.4.NC

① Crawling Google News for articles based on a list of keywords helps identify news publishers covering a specific topic.
   Result will be in EXCEL File 1.1.NC_Korea, 1.1.NC_USA
②
③
④

2.Text Preprocessing: This critical phase prepares the raw text data for analysis through several sub-steps:
(1) Word Segmentation [Tokenization] - (2) Removing Redundant Data - (3) Removing the Null - (4) Removing Irrelevant Content - (5) Removing Stop Words - (6) Term Frequency-Inverse Document Frequency (TF-IDF)
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

Appendix. 1 : Difference between LDA and Keywords
Latent Dirichlet Allocation (LDA) and keyword research serve different, although somewhat related, purposes in the realm of text analysis and search engine optimization (SEO). Here’s how they compare:

### LDA (Latent Dirichlet Allocation)
- **Topic Modeling**: LDA is a type of unsupervised machine learning used for topic modeling. It helps in discovering abstract topics within a collection of documents. LDA assumes that each document is a mixture of topics, and each topic is a mixture of words. By analyzing the word frequencies across documents, LDA can group words into topics and documents into mixtures of topics.
- **Discovery of Themes**: The main goal is to uncover latent themes or topics across a large corpus of text without prior labeling or classification. It’s about understanding the underlying thematic structure of the data.
- **Use Cases**: LDA is widely used in content categorization, organizing large sets of documents, and understanding content themes for academic research, content strategy, and more.

### Keyword Research
- **SEO and Content Strategy**: Keyword research is a practice used in SEO to find and research search terms that users enter into search engines. The aim is to use this information to optimize content, marketing strategy, and understand user behavior.
- **Identification of Specific Terms**: Unlike LDA, which identifies themes or topics, keyword research focuses on finding specific words or phrases that are important for SEO or content creation. It involves analyzing the popularity, search volume, and competitiveness of these keywords.
- **Purpose**: The goal is to identify keywords that can drive targeted traffic to a website from search engines. It’s a fundamental task in SEO and content marketing.

### Comparison
- **Scope**: LDA is broader, aiming to identify themes in a corpus of text, whereas keyword research is more focused, looking for specific terms that can be used to improve search engine visibility and content relevance.
- **Approach**: LDA is an automated, algorithm-driven process that requires no prior knowledge of the documents’ content. Keyword research, on the other hand, is often a manual process, guided by tools designed to analyze search engine data and trends.
- **Outcome**: LDA provides a set of topics, each represented by a cluster of words, to help understand the structure of a large text corpus. Keyword research provides a list of targeted keywords intended to be used for optimizing content and improving SEO.

While both LDA and keyword research can help in content strategy and understanding textual data, LDA is more about discovering the underlying themes in a body of text, and keyword research is about identifying specific terms for optimization and targeting purposes.