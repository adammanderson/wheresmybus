from math import floor

def seconds_to_minutes(seconds):
    return floor(seconds % 3600 / 60)
