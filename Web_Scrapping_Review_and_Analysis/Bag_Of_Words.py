import pandas as pd
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
from collections import Counter

# Load your dataset
# Replace 'your_dataset.csv' with the actual file name
df = pd.read_csv('output.csv')

# Download NLTK resources (if not already downloaded)
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')
# Function to clean and tokenize text
def process_text(text):
    tokens = word_tokenize(text.lower())  # Convert to lowercase and tokenize
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.isalnum() and word not in stop_words]  # Remove punctuation and stop words
    return tokens

# Function to plot bag of words
def plot_bag_of_words(tokens, title):
    word_freq = Counter(tokens)
    plt.figure(figsize=(10, 6))
    plt.bar(word_freq.keys(), word_freq.values())
    plt.title(title)
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.show()

# Analyze sentiment using NLTK's SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
df['compound'] = df['reviews'].apply(lambda x: sia.polarity_scores(x)['compound'])

# Extract keywords and plot bag of words in batches
batch_size = 500
num_batches = len(df) // batch_size + 1

all_tokens = []

for i in range(num_batches):
    start_idx = i * batch_size
    end_idx = min((i + 1) * batch_size, len(df))
    batch_reviews = df.loc[start_idx:end_idx, 'reviews'].str.cat(sep=' ')

    batch_tokens = process_text(batch_reviews)
    all_tokens.extend(batch_tokens)

    # Plot bag of words for each batch
    plot_title = f'Bag of Words - Batch {i + 1}'
    plot_bag_of_words(batch_tokens, plot_title)

# Plot bag of words for all reviews
plot_bag_of_words(all_tokens, 'Bag of Words - All Reviews')

# Plot histogram for the top 25 words
top_words = Counter(all_tokens).most_common(25)
top_word_freq = dict(top_words)
plt.figure(figsize=(12, 8))
plt.bar(top_word_freq.keys(), top_word_freq.values(), color='skyblue')
plt.title('Top 25 Words - Histogram')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()
