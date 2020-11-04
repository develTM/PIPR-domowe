def time_description(hour, minutes):
    dic = {0:'twelve', 1:'one', 2:'two', 3:'three',4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine',
           10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen',
           17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 21:'twenty-one', 22:'twenty-two',
           23:'twenty-three', 24:'twenty-four', 25:'twenty-five', 26:'twenty-six', 27:'twenty-seven',
           28:'twenty-eight', 29:'twenty-nine', 30:'half'}

    if hour > 12:
        hour %= 12
    if minutes == 0:
        if hour == 0:
            return 'midnight'
        return dic[hour] +" o'clock"
    elif minutes <= 30:
        return dic[minutes] + ' past ' + dic[hour]
    else:
        return dic[60-minutes] + ' to ' + dic[hour]

for hour in range(12):
    for minutes in range(0, 60, 13):
        print(time_description(hour, minutes))