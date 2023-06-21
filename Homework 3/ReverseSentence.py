# Name : Anish Banswada

# Time Taken : 15 minutes

# Assumptions : None

# Space Complexity : O(1)

# Time Complexity : O(n)

# Function 
def reverse(sentence):
    return " ".join(sentence.split()[::-1])

# Main

if __name__ == "__main__":
    assert reverse("Hello world") == "world Hello"
    assert reverse("Uber Career Prep") == "Prep Career Uber"
    assert reverse("Emma lives in Brooklyn, New York.") == "York. New Brooklyn, in lives Emma"
    print("Testing completed")

   
 