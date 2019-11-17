# Def function:

# Returns the length of the longest  
# palindromic subsequence in seq  

def lps(seq, i, j): 
      
    # Base Case #1 - only one char
    if (i == j): 
        return 1
  
    # Base Case #2 - only 2 character and both are same
    if (seq[i] == seq[j] and i + 1 == j):
        return 2
      
    # Found match first and last character
    if (seq[i] == seq[j]): 
        return lps(seq, i + 1, j - 1) + 2
  
    # Not found match
    return max(lps(seq, i, j - 1),  
               lps(seq, i + 1, j))

# Running the code

seq = "DATAMININGSAPIENZA"
n = len(seq) 
print("The length of the LPS is",lps(seq, 0, n - 1))
