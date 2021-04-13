def to_time(seconds):
    hours = seconds//3600
    minutes = (seconds - hours*60*60)//60
    return str(hours) + ' hour(s) and ' + str(minutes) +' minute(s)'