# Name : Anish Banswada
# Time Taken : 35 mins

# Problem Description : Two strings are considered to be “k-anagrams” if they can be made into anagrams by changing 
# at most k characters in one of the strings. Given two strings and an integer k, determine if they are k-anagrams.

# Anticipated Strategy : One-directional running computation/total

# Assumptions -  1) Spaced are valid characters, 2) Case sensitive, 

# Space Complexity - Unsure

# Time Complexity - O(n)

from collections import Counter
# Function 
def KAnagrams(s1, s2, k):
    if len(s1) != len(s2):
        return False
    c1 =  Counter(s1)
    c2 =  Counter(s2)
    diff = 0
    for letter in set(s1):
        diff += abs(c1[letter] - c2.get(letter,0))
        if diff > k:
            return False
    diff = 0
    for letter in set(s2):
        diff += abs(c2[letter] - c1.get(letter,0))
        if diff > k:
            return False
    return True

# Main

if __name__ == "__main__": 
    if(KAnagrams("apple","peach", 1)):
        print("YES")
    else:
        print("NO")     # Correct Output

    if(KAnagrams("apple","peach", 2)):
        print("YES")     # Correct Output
    else:
        print("NO")

    if(KAnagrams("cat","dog", 3)):
        print("YES")       # Correct Output
    else:
        print("NO")
    
    if(KAnagrams("debit curd","bad credit", 1)):
        print("YES")       # Correct Output
    else:
        print("NO")

    if(KAnagrams("baseball","basketball", 2)):
        print("YES")       # Correct Output
    else:
        print("NO")