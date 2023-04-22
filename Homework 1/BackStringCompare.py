# Name : Anish Banswada
# Time Taken : 15 minutes

# Problem Description : Given two strings representing series of keystrokes, determine whether the resulting text is the same. 
# Backspaces are represented by the '#' character so "x#" results in the empty string ("").


# Anticipated Strategy : Two arrays/strings two-pointer

# Assumptions -  If number of backspaces > number of letters, string should be empty. 

# Space Complexity - O(n)

# Time Complexity - O(n)

# Function 
def BackStringCompare(s1, s2):
    res1 = []
    for letter in s1:
        if (letter == '#'):
            if (len(res1) > 0):
                res1.pop()
        else: 
            res1.append(letter)
    res2 = []
    for letter in s2:
        if (letter == '#'):
            if (len(res2) > 0):
                res2.pop()
        else: 
            res2.append(letter)
    return res1 == res2
# Main

    
if __name__ == "__main__":
    s1, s2 = "abcde", "abcde"
    if BackStringCompare(s1,s2):
        print("true")
    s1, s2 = "a#bb", "ba"
    if BackStringCompare(s1,s2):
        print("true")
    else:
        print("False")
    s1, s2 = "aaaa###", "a"
    if BackStringCompare(s1,s2):
        print("true")
    else:
        print("False")
   
 