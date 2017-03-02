# Find all words that have the same letters, or anagrams, in a dictionary.

# empty dictionary for anagrams
map_dictionary = {}

def solve():
    """ For all words in the list, create a tuple that acts as a key to the dictionary.
        If it is found, add the word to its own dictionary.
        Then, print all dictionaries contianing words, or anagrams!"""
    f = open('words.txt')
    for wordList in f:
        wordList = wordList.strip() 
        tupe = tuple(sorted(wordList))
        if tupe not in map_dictionary:
            map_dictionary[tupe] = [wordList]
        else:
            map_dictionary[tupe].append(wordList)

    for key in map_dictionary: 
        if len(map_dictionary[key]) > 1:
             print map_dictionary[key]
        
        
        
        
solve()
        

