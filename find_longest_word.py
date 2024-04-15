def get_longest_word_idx(string_):
    words = string_.split()  # Dzieli ciąg znaków na słowa
    longest_word = ""
    longest_word_index = -1
    
    for idx, word in enumerate(words):
        if len(word) > len(longest_word):
            longest_word = word
            longest_word_index = idx
    
    return longest_word, longest_word_index

string_ = "Hello, my best day ever-ever!"
print(get_longest_word_idx(string_))