# Blood Moon

## Problem
Given a time in `"HH:MM"` (24-hour format), calculate the next three times a Blood Moon occurs. Each Blood Moon happens every **2 hours 48 minutes**.

## Approach
- Convert the given time into total minutes.
- Add **168 minutes** (2 hours 48 minutes) for each occurrence.
- Use modulo **1440** to handle wrap-around within a 24-hour day.
- Convert the result back to `"HH:MM"` format with leading zeros.

## Solution
```python
def blood_moon(time):
    hours,minutes=map(int,time.split(":"))
    total=hours*60+minutes
    result=[]
    for _ in range(3):
        total=(total+168)%1440
        h=total//60
        m=total%60
        result.append(f"{h:02d}:{m:02d}")
    return result
