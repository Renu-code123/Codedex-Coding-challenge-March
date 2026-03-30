##
def emoticons_mood(message):
    happy = [":)", ":p", "XD", ":3", "<3", "\\m/"]
    sad = [":(", ":'(", "t(-.-t)"]
    score = 0
    for emo in happy:
        score += message.count(emo)
    for emo in sad:
        score -= message.count(emo)
    return score
