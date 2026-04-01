##
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
