import streamlit as st
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
from textblob import Word
from nltk.corpus import stopwords
import nltk
import string

# Download the stopwords from nltk
nltk.download('stopwords')

class WordCounter:
    def __init__(self, language='english'):
        self.language = language
        self.stop_words = set(stopwords.words(language))

    def process_text(self, text):
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        words = [word for word in text.split() if word.lower() not in self.stop_words]
        return words

    def get_statistics(self, text):
        word_count = len(text.split())
        char_count = len(text)
        line_count = text.count('\n') + 1
        return word_count, char_count, line_count

    def get_word_frequencies(self, words):
        word_freq = Counter(words)
        word_freq_df = pd.DataFrame(word_freq.items(), columns=['Word', 'Frequency'])
        word_freq_df = word_freq_df.sort_values(by='Frequency', ascending=False)
        return word_freq_df

    def plot_word_frequencies(self, word_freq_df, top_n):
        word_freq_df = word_freq_df.head(top_n)
        fig, ax = plt.subplots()
        sns.barplot(x='Frequency', y='Word', data=word_freq_df, ax=ax)
        plt.title(f'Top {top_n} Most Frequent Words')
        plt.xlabel('Frequency')
        plt.ylabel('Words')
        return fig

def main():
    st.title("Word Counter")

    uploaded_file = st.file_uploader("Choose a text file", type="txt")
    language = st.selectbox("Choose language", ["english", "spanish", "french", "german"])
    top_n = st.slider("Select number of top words to display", min_value=1, max_value=40, value=10)

    if uploaded_file is not None:
        text = uploaded_file.read().decode("utf-8")
        
        wc = WordCounter(language)
        
        word_count, char_count, line_count = wc.get_statistics(text)
        
        st.subheader("Word Count:")
        st.write(f"Word Count: {word_count}")
        st.subheader("Additional Statistics:")
        st.write(f"Character Count: {char_count}")
        st.write(f"Line Count: {line_count}")

        words = wc.process_text(text)
        word_freq_df = wc.get_word_frequencies(words)
        fig = wc.plot_word_frequencies(word_freq_df, top_n)

        st.pyplot(fig)

if __name__ == "__main__":
    main()
