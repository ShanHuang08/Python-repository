def answer1(seconds):
    if seconds <= 0 : seconds = abs(seconds)
    
    sec_rem = seconds % 60 // 1
    sec_str = 'second' if sec_rem == 1 else 'seconds'

    min_rem = seconds % 3600 // 60
    min_str = 'minute' if min_rem == 1 else 'minutes'

    hour_rem = seconds % 86400 // 3600
    hour_str = 'hour' if hour_rem == 1 else 'hours'

    day_rem = seconds % 31536000 // 86400
    day_str = 'day' if day_rem == 1 else 'days' 

    year = seconds // 31536000
    year_str = 'year' if year == 1 else 'years'

    
    if seconds == 0: return 'now'
    elif seconds < 60: return f'{sec_rem} {sec_str}'
    elif seconds < 60*60:
        # minute only
        if sec_rem == 0: return f'{min_rem} {min_str}'
        # minute and seconds
        else: return f'{min_rem} {min_str} and {sec_rem} {sec_str}'
    elif seconds < 60*60*24:
        # hour only
        if min_rem == 0: return f'{hour_rem} {hour_str}'
        # hour and minute
        elif sec_rem == 0: 
            return f'{hour_rem} {hour_str} and {min_rem} {min_str}'
        # hour and seconds
        elif min_rem == 0: return f'{hour_rem} {hour_str} and {sec_rem} {sec_str}'
        # hour, minute and second
        else: 
            return f'{hour_rem} {hour_str}, {min_rem} {min_str} and {sec_rem} {sec_str}'
    elif seconds < 60*60*24*365: 
        # day only
        if hour_rem == 0: return f'{day_rem} {day_str}'
        # day and hour
        elif min_rem == 0 and sec_rem == 0: return f'{day_rem} {day_str} and {hour_rem} {hour_str}'
        # day and minute
        elif hour_rem == 0 and sec_rem == 0: return f'{day_rem} {day_str} and {min_rem} {min_str}'
        # day and seconds
        elif hour_rem == 0 and min_rem == 0: return f'{day_rem} {day_str} and {sec_rem} {sec_str}' 
        # day, hour and minute
        elif sec_rem == 0: return f'{day_rem} {day_str}, {hour_rem} {hour_str} and {min_rem} {min_str}'
        # day, minute and seconds
        elif hour_rem == 0: return f'{day_rem} {day_str}, {min_rem} {min_str} and {sec_rem} {sec_str}'
        # day, hour and seconds
        elif min_rem == 0: return f'{day_rem} {day_str}, {hour_rem} {hour_str} and {sec_rem} {sec_str}'
        # day, hour, minute and seconds
        else: return f'{day_rem} {day_str}, {hour_rem} {hour_str}, {min_rem} {min_str} and {sec_rem} {sec_str}'
    else:
        # year only
        if day_rem == 0: return f'{year} {year_str}'
        # year and day
        elif hour_rem == 0 and min_rem == 0 and sec_rem == 0: return f'{year} {year_str} and {day_rem} {day_str}'
        # year and hour
        elif day_rem == 0 and min_rem == 0 and sec_rem == 0: return f'{year} {year_str} and {hour_rem} {hour_str}'
        # year and minute
        elif day_rem == 0 and hour_rem == 0 and sec_rem == 0: return f'{year} {year_str} and {min_rem} {min_str}'
        # year and seconds
        elif day_rem == 0 and hour_rem == 0 and min_rem == 0: return f'{year} {year_str} and {sec_rem} {sec_str}'
        # year, day and hour
        elif min_rem == 0 and sec_rem == 0: return f'{year} {year_str}, {day_rem} {day_str} and {hour_rem} {hour_str}'
        # year, day and minute
        elif hour_rem == 0 and sec_rem == 0: return f'{year} {year_str}, {day_rem} {day_str} and {min_rem} {min_str}'
        # year, day and seconds 
        elif hour_rem == 0 and min_rem == 0: return f'{year} {year_str}, {day_rem} {day_str} and {sec_rem} {sec_str}'
        # year, hour and minute
        elif day_rem == 0 and sec_rem == 0: return f'{year} {year_str}, {hour_rem} {hour_str} and {min_rem} {min_str}'
        # year, hour and seconds
        elif day_rem == 0 and min_rem == 0: return f'{year} {year_str}, {hour_rem} {hour_str} and {sec_rem} {sec_str}'
        # year, minute and seconds
        elif day_rem == 0 and hour_rem == 0: return f'{year} {year_str}, {min_rem} {min_str} and {sec_rem} {sec_str}'
        # year, day, hour and minute
        elif sec_rem == 0: return f'{year} {year_str}, {day_rem} {day_str}, {hour_rem} {hour_str} and {min_rem} {min_str}'
        # year, day, hour and seconds
        elif min_rem == 0: return f'{year} {year_str}, {day_rem} {day_str}, {hour_rem} {hour_str} and {sec_rem} {sec_str}'
        # year, day, hour, minute and seconds
        else: return f'{year} {year_str}, {day_rem} {day_str}, {hour_rem} {hour_str}, {min_rem} {min_str} and {sec_rem} {sec_str}'

# test = answer1(31536000*0 + 86400*0 + 3600*0 + 60*2 + 4) # 1day, 1hr + 1 min + 2 secs
# 31536000*0 + 86400*2 + 3600*2 + 60*2 + 2
# print(test)



def format_duration1(seconds):
    times = [("year", 365 * 24 * 60 * 60), 
         ("day", 24 * 60 * 60),
         ("hour", 60 * 60),
         ("minute", 60),
         ("second", 1)]

    if not seconds:
        return "now"

    chunks = []
    for name, secs in times:
        qty = seconds // secs
        if qty:
            if qty > 1:
                name += "s"
            chunks.append(str(qty) + " " + name)

        seconds = seconds % secs

    return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]


def f(n, unit):
    return [', ', '{} {}{}'.format(n, unit, 's' if n > 1 else '')]

def format_duration2(seconds):
    if not seconds: return 'now'

    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    years, days = divmod(days, 365)

    fs = []
    if years: fs.extend(f(years, 'year'))
    if days: fs.extend(f(days, 'day'))
    if hours: fs.extend(f(hours, 'hour'))
    if minutes: fs.extend(f(minutes, 'minute'))
    if seconds: fs.extend(f(seconds, 'second'))

    fs[-2] = ' and '
    fs.pop(0)
    return ''.join(fs)



def format_duration3(sec):
    from datetime import timedelta
    timy = timedelta(seconds = sec)
    times = [timy.days//365, timy.days%365, timy.seconds//3600, timy.seconds//60 - (timy.seconds//3600)*60, timy.seconds%60]
    name = ["year", "day", "hour", "minute", "second"]
    res = []
    for x in range(0, 5):
        if times[x]:
            res.append(str(times[x]) + " " + name[x])
            if times[x] > 1:
                res[-1] += "s"
    return {
        0 : "now",
        1 : "{}",
        2 : "{} and {}",
        3 : "{}, {} and {}",
        4 : "{}, {}, {} and {}",
        5 : "{}, {}, {}, {} and {}"
      }[len(res)].format(*res)




def format_duration4(seconds):
    from collections import OrderedDict
    if(seconds == 0): return 'now'
    
    time = OrderedDict()
    
    time['years'] = seconds // 31536000
    time['days'] = seconds // 86400 % 365
    time['hours'] = seconds // 3600 % 24
    time['minutes'] = seconds // 60 % 60
    time['seconds'] = seconds % 60
    
    output = []
    
    for key in time:
        if(time[key] > 1):
            output.append(str(time[key]) + ' ' + key)
        elif (time[key] == 1):
            output.append(str(time[key]) + ' ' + key[:-1])
            
    print(output)
            
    return ", ".join(output[:-2] + [" and ".join(output[-2:])])


def format_duration5(seconds):
    td = {
        "year": seconds // 31536000,
        "day": seconds % 31536000 // 86400,
        "hour": seconds % 86400 // 3600,
        "minute": seconds % 3600 // 60,
        "second": seconds % 60,
    }

    r = [str(v) + " " + add_s(v, k) for k, v in td.items() if v > 0]

    return ' and '.join(', '.join(r).rsplit(', ', 1)) or 'now'
    
def add_s(c, s):
    if c > 1:
        return s + 's'
    return s


import requests
def get_request(url):
    print(f'Execute requests.get({url})')
    # current_func = inspect.stack()[0].function
    try:
        requests.get(url, auth=('admin','123456'), verify=False)
        print("requests.get(url, auth=('admin','123456'), verify=False)")
    except requests.exceptions.ConnectTimeout as e:
        print(f'ConnectTimeout: {e}')
        retry(get_request, url)

def patch_request(url, body):
    print(f'Execute requests.get({url})')
    # current_func = inspect.stack()[0].function
    try:
        requests.patch(url, auth=('admin','123456'), json=body, verify=False)
        print("requests.patch(url, auth=('admin','123456'), json=body, verify=False)")
    except requests.exceptions.ConnectTimeout as e:
        print(f'ConnectTimeout: {e}')
        retry(patch_request, url)

def retry(method, url):
    print(f'retrying {method.__name__}...')
    if method == 'get_request':
        print(f'retry requests.get({url})')
    else:
        get_url = 'https://127.0.0.2/api'
        print(f'requests.get({get_url})')

patch_request('https://127.0.0.1/patch/api', {'test' : 123})