"""
This script, using a dictionary provided by https://github.com/dwyl/english-words,
sorts the letters of each word in the dictionary,
and stores this sorted version of the word in a file followed by
any words that also has this string
An anagram of any word will have the same string of sorted letters as the given word.
We
"""
def create_anagram_dictionary():
    """
    Creates a dictionary of words based on the words in file "data/words_alpha.txt"
    Returns:
        dictionary: a dictionary that uses a string of characters (in alphabetical order) as the key and
        has a list of words that contain those characters (and only those characters).
    """
    anagram_dictionary = {}
    with open("data/words_alpha.txt","r") as words_file:
        for line in words_file:
            word = line.strip()
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagram_dictionary:
                anagram_dictionary.get(sorted_word).append(word)
            else:
                anagram_dictionary[sorted_word] = []
                anagram_dictionary[sorted_word].append(word)
    return anagram_dictionary

def cache_anagram_dictionary():
    """
    creates a text file that stores the dictionary created by create_anagram_dictionary()
    in the format:
    <string of sorted letters>: <anagram of those letters>, <anagram of those letters2>,...
    """
    anagram_dictionary_file = open("data/anagram_dictionary.txt","w")
    for sorted_word, words in create_anagram_dictionary().items():
        anagram_dictionary_file.write(sorted_word + ": ")
        for word in words:
            anagram_dictionary_file.write(word + ",")
        anagram_dictionary_file.write("\n")

if __name__ == '__main__':
    cache_anagram_dictionary()
