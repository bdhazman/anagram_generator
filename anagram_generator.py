import sys
"""
init_anagram_dictionary() must be run before calling get_anagrms()

storing the anagram dictionary as a static variable allows us to use the
dictionary multiple times in a program execution, without having to
reload the dictionary from the anagram_dictionary.txt file.
"""
anagram_dictionary = {}
def init_anagram_dictionary():
    """
    initializes the anagram_dictionary to hold sorted_word values as the keys
    and any word whose sorted_word matchest that key to be in an array as the
    value of the dictionary.
    """
    with open("data/anagram_dictionary.txt") as anagram_dictionary_file:
        for line in anagram_dictionary_file:
            line_split = line.split(":")
            anagrams = line_split[1].strip("\n").split("|")
            anagram_dictionary[line_split[0]] = anagrams[0:len(anagrams)-1]


def get_anagrams(word):
    """
    returns all words that have the same sorted_word as the given word,
    therefore, this function retuns all anagrams of the given word.

    Args:
        word (str): the word that we are going to find anagrams of

    Returns:
        List[str]: a list of anagrams of word

    """
    sorted_word = ''.join(sorted(word.lower()))
    if sorted_word in anagram_dictionary:
        return anagram_dictionary[sorted_word]
    else:
        return []

if __name__ == '__main__':
    init_anagram_dictionary()
    if len(sys.argv) > 1:
        print("Anagrams of "+ sys.argv[1] +":")
        for anagram in get_anagrams(sys.argv[1]):
            print(anagram)
    else:
        print("No word given.")
