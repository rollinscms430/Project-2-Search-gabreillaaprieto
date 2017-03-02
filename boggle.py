# My intention was check each letter in the grid 
# and its immediate neighbors in the grid for matches using the prefix dictionary!
from copy import deepcopy
board = [['u', 'n', 't', 'h'],['g','a','e','s'],['s','r','t','r'],['h','m','i','a']]
queue = []
words = {}
prefixes = {}

class State(object): 
    def __init__(self, letters, positions):
        self.letters = letters
        self.positions = positions
    def new_letters(self, position):
        new_letters = deepcopy(self.letters)
        new_letters += board[position[0]][position[1]]
        new_positions = deepcopy(self.positions)
        new_positions.append(position)
        return State(new_letters, new_positions)
        
    
def get_neighbors(state):
    position = state.positions(len(state.positions) - 1)
    row = position[0]
    col = position[1]
    positions = []
    if position = (0,0):
        positions.append((0,1))
        positions.append((1,0))
        positions.append((1,1))
    if position = 
    
        
    
    # return a list of tuples(positions)
    return positions
    
    
def is_word(state):
    if state.letters in words:
        return True
    return False
    
def is_prefix(state):
    if state.letters in prefixes:
        return True
    return False
        
    
    
def solve(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            visited = [(i,j)]
            letters = board[i][j]
            new_state = State(letters, visited)
            queue.append(new_state)
            
    while len(queue) > 0:
        current_state = queue.pop(0)
        if is_word(current_state):
            print current_state.letters
        if is_prefix(current_state):
            list_of_neighbors = get_neighbors(current_state)
            for position in list_of_neighbors:
                new_state = current_state.new_letters(position)
                queue.append(new_state)
            
            
        
        
    
if __name__ == '__main__':
    f = open('words.txt'):
    for wordList in f:
        wordList = wordList.strip() 
        words[wordList] = 1
        pref = ''
        for i in range(len(wordList) - 2 ):
            pref += wordList[i]
            if pref not in prefixes:
                prefixes[pref] = 1
            
    solve(board)
    
    