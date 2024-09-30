import streamlit as st
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
import string

# Download the stopwords from nltk
nltk.download('stopwords')

def main():
    st.title("Word Counter")

    uploaded_file = st.file_uploader("Choose a text file", type="txt")

    if uploaded_file is not None:
        text = uploaded_file.read().decode("utf-8")
        text = text.lower()
        word_count = len(text.split())
        
        st.subheader("Word Count:")
        st.write(f"Word Count: {word_count}")

        st.subheader("Additional Statistics:")
        char_count = len(text)
        st.write(f"Character Count: {char_count}")
        line_count = text.count('\n') + 1
        st.write(f"Line Count: {line_count}")

        stop_words = set(stopwords.words('english'))

        # Remove punctuation from the text
        text = text.translate(str.maketrans('', '', string.punctuation))

        # Filter out stop words from the text
        words = [word for word in text.split() if word.lower() not in stop_words]

        word_freq = Counter(words)

        # Create a DataFrame for the word frequencies
        word_freq_df = pd.DataFrame(word_freq.items(), columns=['Word', 'Frequency'])

        word_freq_df = word_freq_df.sort_values(by='Frequency', ascending=False).head(10)

        fig, ax = plt.subplots()
        bars = word_freq_df.plot(kind='bar', x='Word', y='Frequency', ax=ax, legend=False)
        plt.xticks(rotation=45)
        plt.title('Top 10 Most Frequent Words')
        plt.xlabel('Words')
        plt.ylabel('Frequency')

        for bar in bars.patches:
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), int(bar.get_height()), 
                    ha='center', va='bottom')

        st.pyplot(fig)

if __name__ == "__main__":
    main()