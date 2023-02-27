from collections import Counter
# Name : Anish Banswada

# Time Taken : 1 hour

# Problem Description :  Given a string and a second string representing required characters, 
# return the length of the shortest substring containing all the required characters.

# Anticipated Strategy : Growing/Shrinking window

# Assumptions -  s1 always contains s2, and size(s1) <= size(s2)

# Function 
def ShortestSubstring(s1, s2):
    target_letters = Counter(s2)
    window_start = 0
    length = len(s1) + 1
    cur_len = len(s1) + 1
    for index,letter in enumerate(s1):
        if letter in target_letters:
            target_letters[letter] -= 1
        while(sum(target_letters.values()) == 0):
            cur_len = index - window_start + 1
            if s1[window_start] in target_letters:
                target_letters[s1[window_start]] += 1
            window_start += 1
        length = min(length, cur_len)
    return length


# Main

if __name__ == "__main__":

    print("Expected 4 and got " + str(ShortestSubstring("abracadabra", "abc")))
   
 