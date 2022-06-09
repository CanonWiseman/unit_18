def print_upper_words(words, must_start_with):
    """prints uppercase words from a list of words starting with user defined letters"""
    for word in words:
        for char in must_start_with:
            if not(word[0].find(char) == -1):
                print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})