# find a ladder connecting 'snakes' and 'brains'

from copy import deepcopy
words = {}
queue = []
visited = {}
class State(object): 
    """Represents a state in the solution of the puzzle
    
        Attributes:
            words: a sequence of words added to it"""
    def __init__(self, words):
        self.words = words
    def new_word(self, word):
        new_words = deepcopy(self.words)
        new_words.append(word)
        return State(new_words)
        
def solve(word):
    """Recursively solves the problem by checking all words in the 
    dictionary of same length for a letter difference of 1, and if
    it has not been visited create a new state with the new word added,
    and add this new state to the queue of pontential successful word lists.
    Run time is not great, remove # at line 32 to see that it is actually working.
    """
    state = State([word])
    queue.append(state)
    while len(queue) > 0:
        current_state = queue.pop(0)
        current_word = current_state.words[len(current_state.words) - 1]
        visited[word] = 1
#        print current_state.words
        if current_word == 'brains':
            print current_state.words
        for word in words:
            if len(word) == len(current_word):
                count = 0
                for i in range(len(word) - 1):
                    if word[i] != current_word[i]:
                        count += 1
                if count == 1:
                    if word not in visited:
                        new_state = current_state.new_word(word)
                        queue.append(new_state)
                
    
    
 
                
if __name__ == '__main__':
    f = open('words.txt')
    for wordList in f:
            wordList = wordList.strip() 
            words[wordList] = 1
    solve('snakes')
