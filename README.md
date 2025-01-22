# Simple N-Gram Model

This project implements a simplified N-gram model (a purely simplified language model) in Python.

## Structure du projet

The project includes the following files:  
- `main.py`: Source file.  
- `text.txt`: Text file used as a dataset (currently the TinyShakespeare dataset).

### Main Functions

- `clean_word(word)`: Cleans a word by removing punctuation characters and converting it to lowercase.
- `disct_count(text)`: Counts the occurrences of each word in a text.
- `by_gram_dic_count(text)`: Counts the occurrences of each bigram (sequence of two words) in a text.
- `by_gram(text)`: Generates a bigram model from a text.
- `three_gram(text)`: Generates a trigram model from a text.
- `four_gram(text)`: Generates a quadrigram model from a text.
