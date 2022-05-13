
def print_upper_words(word_list, must_start_with):
    """Prints each word on a separate line, but in all uppercase"""
    
    for word in word_list:
        # if word.startswith('e') or word.startswith('E'):
        for letter in must_start_with:
            if word.startswith(letter):
        
                print(word.upper())


# print_upper_words(['hi', 'butt', 'eeeeee', 'lol', 'angee', 'english', 'apple', 'enlighten'])


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})