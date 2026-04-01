# Wordle

## Problem
Given two strings `secret` and `guess` of equal length (5 letters), determine how many characters are correct and in the exact same position.

## Approach
- Compare both strings character by character.
- Count how many positions have the same character in both strings.
- Return the total count.

## Solution
```python
def wordle_guess(secret, guess):
    count=0
    for i in range(len(secret)):
        if secret[i]==guess[i]:
            count+=1
    return count
