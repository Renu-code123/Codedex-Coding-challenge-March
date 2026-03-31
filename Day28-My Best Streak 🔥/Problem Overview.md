# My Best Streak

## Problem
Given a list representing a user's daily progress:

- '✅' = completed the challenge  
- '❌' = missed the challenge  

Find the length of the longest consecutive streak of '✅'.

## Example

Input:
['✅', '✅', '❌', '✅', '✅', '✅']

Output:
3

## Approach
- Traverse the list once.
- Maintain two variables:
  - current_streak: counts consecutive '✅'
  - max_streak: stores the maximum streak found
- Reset current_streak to 0 when '❌' appears.

## Code

```python
def longest_streak(progress):
    max_streak = 0
    current_streak = 0
    
    for day in progress:
        if day == '✅':
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 0
    
    return max_streak
