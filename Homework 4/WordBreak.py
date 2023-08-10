# Name : Anish Banswada

# Strategy : Trie as a param

# Time Taken : 30 minutes

# Assumptions : None

# Space Complexity : O(n*m) where n is num of words and m is avg word length

# Time Complexity : O(m*n)

# Function 

# Main
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
def wordBreak(target,words):
    root = TrieNode()
    for word in words:
        root.addWord(word)
    cur = root
    def dfs(cur,i):
        if i >= len(target):
            return True
        if target[i] not in cur.children:
            return False
        cur = cur.children[target[i]]
        if cur.end:
            new_cur = root
            return dfs(new_cur,i+1) or (cur,i+1)
        return dfs(cur,i+1)
    return True

if __name__ == "__main__":
    
    words = ['elf','go','golf','man','manatee','not','note','pig','quip','tee','teen']
    target = 'mangolf'
    assert wordBreak(target,words) == True
    target = 'manateenotelf'
    assert wordBreak(target,words) == True
    target = 'quipig'
    assert wordBreak(target,words) == False
 