##
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
  
