import nltk # Natural Language Toolkit

# Required to split text into word and sentence tokens
nltk.download("punkt") 
# Additional data package required by newer NLTK versions
nltk.download("punkt_tab") 

text = "Hello World! How are you! Hello, hi ..."

# Word Tokenization: word_tokenize splits the text into words
# Punctuation marks are also extracted as separate tokens
word_tokens = nltk.word_tokenize(text)
print("Word Tokens:", word_tokens)

# Sentence Tokenization: sent_tokenize splits the text into sentences
# Each sentence becomes a single token
sentence_tokens = nltk.sent_tokenize(text)
print("\nSentence Tokens:", sentence_tokens)