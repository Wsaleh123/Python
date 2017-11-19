def minutes_to_hours(seconds, min=70):
    hours = min/60 + seconds / 3600
    return hours

print(type(minutes_to_hours(300, 200)))
