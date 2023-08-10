# Name : Anish Banswada

# Strategy : Trie as a parameter

# Time Taken : 30 minutes

# Assumptions : None

# Space Complexity : O(m*n)

# Time Complexity : O(m*n)

# Function 
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    def addWord(self,word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

def boggle(grid,words):
    if not (words or grid):
        return [""]
    root = TrieNode()
    for word in words:
        root.addWord(word)
    visit = set()
    directions = [[-1,0],[1,0],[0,1],[0,-1],[-1,1],[1,-1],[-1,-1],[1,1]]
    res = set()
    def dfs(r,c,word,node):
        if r >= len(grid) or r < 0 or c >= len(grid[0]) or c < 0 or (r,c) in visit or grid[r][c] not in node.children:
            return 
        node = node.children[grid[r][c]]
        word += grid[r][c]
        if node.end:
            res.add(word)
        visit.add((r,c))
        for direction in directions:
            i = r + direction[0]
            j = c + direction[1]
            dfs(i,j,word,node)
        visit.remove((r,c))
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            dfs(i,j,"",root)
    return list(res)

if __name__ == '__main__':
    board = [['A','D','E'],['R','C','P'],['L','A','Y']]
    words = ['ACE','DRA','ARP','LAY','ZAK','DEP','PDL','YAR']
    res = ['ACE','DRA','LAY','DEP','YAR']
    output = boggle(board,words)
    assert len(output) == len(res)
    for word in res:
        assert word in output
    print('Testing completed')


        
    