import re     # A library called RegEx
from nltk.corpus import stopwords   # NLTK Library extracts all the stopwords for every language to be removed
from nltk.tokenize import word_tokenize   # Tokenize our sentence so it is separated to simple words
from nltk.stem import PorterStemmer   # Stems the word to it's root word/verb

def preprocessing_step(text):
  ### Lower Text
  text = text.lower()   # str is important as it won't convert to lower if it wasn't a series
  ### Remove any special Character
  text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
  ### Tokenization ['I love you'] --> ['I','love','you']
  tokens = word_tokenize(text)
  ### Stopwords
  stop_words = set(stopwords.words('english'))
  filtered_tokens = [word for word in tokens if word not in stop_words] ## List comprehension is used as it is faster than for loop
  ### Stemming porter stemmer / Lemetization    ## Stemming is fast, not as accurate  ## Lemetization is slow, More accurate
  stemmer = PorterStemmer()
  stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]
  stemmed_tokens = ' '.join(stemmed_tokens)
  return stemmed_tokens