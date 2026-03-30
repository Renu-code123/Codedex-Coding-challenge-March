# Ye Olde Emoticons

## Problem
Given a text string `message`, analyze the emoticons present and return an overall mood score.

## Rules
Each emoticon contributes:
- Happy emoticons → +1
- Sad emoticons → -1

### Happy Emoticons
:) , :p , XD , :3 , <3 , \m/

### Sad Emoticons
:( , :'( , t(-.-t)

## Approach
- Store happy and sad emoticons in separate lists
- Count occurrences of each emoticon in the message
- Add for happy, subtract for sad
- Return the final score

## Solution (Python)
```python
def emoticons_mood(message):
    happy = [":)", ":p", "XD", ":3", "<3", "\\m/"]
    sad = [":(", ":'(", "t(-.-t)"]
    
    score = 0
    
    for emo in happy:
        score += message.count(emo)
        
    for emo in sad:
        score -= message.count(emo)
        
    return score
