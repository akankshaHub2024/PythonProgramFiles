def count_word_occurrences(sentence):
    # Convert the sentence to lowercase and split into words
    words = sentence.lower().split()
    
    # Create a dictionary to store word counts
    word_count = {}
    
    for word in words:
        # Increment count for each word
        word_count[word] = word_count.get(word, 0) + 1
    
    return word_count

# Example usage
sentence = "This is a test. This test is only a test."
# Removing punctuation for more accurate counting
import string
sentence_clean = sentence.translate(str.maketrans('', '', string.punctuation))

result = count_word_occurrences(sentence_clean)
print(result)
