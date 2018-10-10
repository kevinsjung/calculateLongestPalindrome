def computeLongestPalindromeLength(text):
    """
    Delete letters from the input text to find the longest palindrome achievable.
    A palindrome is a string that is the same read forwards and backwards (ex: 'abba').
    For example: the longest palindrome in 'abigail' is 'aba', 'aia', or 'aga'.
    This algorithm will return the length, so for the above example, it will return 3.
    This algorithm runs in O(len(text)^2) time.
    """

    """
    Basic idea of algorithm is to create a table of size len(text) x len(text).
    Traverse "diagonally" down the table comparing text[i] to text[j]
    A palindrome is found text[i] == text[j] and the length can be calculated by adding the adjacent (left or bottom) value.
    """

    if text == text[::-1]: # input is a palindrome
        return len(text)
    else:

        palindrome_length = [[0 for i in range(len(text))] for j in range(len(text))]

        for i in range(len(text)):
            palindrome_length[i][i] = 1
            i += 1

        for sl in xrange(2, len(text) + 1): #substring length, want to test strings from length 2 to the whole word
            for i in xrange(0, len(text) + 1 - sl): # starting index to fit length of substring
                j = i + sl - 1  # last character in substring
                if text[i] == text[j]:
                    palindrome_length[i][j] = palindrome_length[i+1][j-1] + 2
                else:
                    palindrome_length[i][j] = max(palindrome_length[i][j-1], palindrome_length[i+1][j])

        return palindrome_length[0][len(text)-1]

# Sample test
print computeLongestPalindromeLength('What is the longest palindrome length?')