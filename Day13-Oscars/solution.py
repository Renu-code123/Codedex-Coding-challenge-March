def oscar_pool(predictions):
    winners = [
        "One Battle After Another",
        "Michael B. Jordan",
        "Jessie Buckley",
        "Paul Thomas Anderson"
    ]
    
    max_score = 0
    winner_name = ""
    tie = False
    
    for p in predictions:
        name = p[0]
        score = 0
        
        for i in range(4):
            if p[i+1] == winners[i]:
                score += 1
        
        if score > max_score:
            max_score = score
            winner_name = name
            tie = False
        elif score == max_score:
            tie = True
    
    if tie:
        return "Tie"
    
    return winner_name
