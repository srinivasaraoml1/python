# This is an exercise on "Even More Practice"

def breaks_stuff(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def prints_first_word(words):
    """Prints the first word after popping it off."""
    return words.pop(0)

def print_last_word(words):
    """Prints the last word after popping it off."""
    return words.pop(-1)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    x = breaks_stuff(sentence)
    return sort_words(x)

def first_last_sentence(sentence):
    """Prints the first and last words of the sentence."""
    words = breaks_stuff(sentence)
    print_first_word(words)
    print_last_word(words)

def first_last_sorted_sentence(sentence):
    """Sorts the words then prints the first and last one."""
    x = breaks_stuff(sentence)
    print_first_word(x)
    print_last_word(x)
