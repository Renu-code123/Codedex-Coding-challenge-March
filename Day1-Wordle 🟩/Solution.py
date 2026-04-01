``python:

def wordle_guess(secret, guess):
    count=0
    for i in range(len(secret)):
        if secret[i]==guess[i]:
            count+=1
    return count
