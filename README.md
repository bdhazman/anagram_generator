# Python Anagram Generator
An anagram generator written in python that can be executed from the command line or used in projects as needed.
## How it Works
To find an anagram of a given word, we first sort the letters of the given word.

```Python
word = "peek"
sorted_word = ''.join(sorted(word))
sorted_word #sorted_word = "eekp"
```

Using a txt [dictionary file](https://github.com/dwyl/english-words), setup.py creates a python dictionary that uses a ```sorted_word``` as a key, with its values being an array of all words that have that same ```sorted_word```.
```python
anagram_dictionary = {}
#some code (see setup.py)
anagram_dictionary[sorted_word] #["keep","peek","peke"]
```

This allows us to find all anagrams of a given word by simply accessing ```anagram_dictionary[sorted_word]``` for any word.

## How to use
#### From the Command Line
```
$ python anagram_generator.py <word>
```

## License
See [License](LICENSE.md) for the license rights and limitations (MIT).
