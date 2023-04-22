# Name : Anish Banswada
# Time Taken : 30 minutes

# Problem Description : Given a string, reverse the order of the vowels in the string.

# Anticipated Strategy : Forward/backward two-pointer

# Assumptions -  1) case is preserved 2) input isn't empty 

# Space Complexity - O(1)

# Time Complexity - O(n)

# Function 
def reverseVowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    s = list(s)
    left = 0 
    right = len(s) - 1
    while (left <= right):
        while(s[left] not in vowels and left < right):
            left += 1
        while(s[right] not in vowels and right > left):
            right -= 1
        temp = s[left]
        s[left] = s[right]
        s[right] = temp
        left += 1
        right-= 1
    return ''.join(s) 

# Main

if __name__ == "__main__":
    s = "Uber Career Prep"
    print(reverseVowels(s))
    s = "xyz"
    print(reverseVowels(s))
    s = "flamingo"
    print(reverseVowels(s))
    s = "abexu"
    print(reverseVowels(s))

   
 