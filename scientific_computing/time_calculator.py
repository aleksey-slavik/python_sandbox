DAYS_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
BEFORE_MIDDAY_PERIOD = 'AM'
AFTER_MIDDAY_PERIOD = 'PM'
HOUR_MINUTES = 60
HALF_DAY_HOURS = 12
DAY_HOURS = 24
WEEK_DAYS = 7


def calculate_time_minutes(time, period=None):
    time_hours = int(time.split(':')[0])
    time_minutes = int(time.split(':')[1])

    if period is not None:
        if period == BEFORE_MIDDAY_PERIOD:
            if time_hours == 12:
                time_hours = 0
        else:
            if time_hours != 12:
                time_hours += 12

    time_minutes += time_hours * HOUR_MINUTES
    return time_minutes


def get_day_index(day_to_search):
    for day_index in range(WEEK_DAYS):
        if DAYS_OF_WEEK[day_index].lower() == day_to_search.lower():
            return day_index
    return None


def add_time(start, duration, start_day=None):
    start_time_minutes = calculate_time_minutes(start.split()[0], start.split()[1])
    duration_minutes = calculate_time_minutes(duration)
    result_time_minutes = start_time_minutes + duration_minutes
    result_minutes = result_time_minutes % HOUR_MINUTES
    result_hours = (result_time_minutes // HOUR_MINUTES) % DAY_HOURS
    result_period = AFTER_MIDDAY_PERIOD if result_hours // HALF_DAY_HOURS == 1 else BEFORE_MIDDAY_PERIOD
    result_hours = HALF_DAY_HOURS if result_hours % HALF_DAY_HOURS == 0 else result_hours % HALF_DAY_HOURS
    result_days = (result_time_minutes // HOUR_MINUTES) // DAY_HOURS
    new_time = str(result_hours) + ':' + str(result_minutes).rjust(2, '0') + ' ' + result_period

    if start_day is not None:
        start_day_index = get_day_index(start_day)
        day_of_week = DAYS_OF_WEEK[(start_day_index + result_days) % WEEK_DAYS]
        new_time += ', ' + day_of_week

    if result_days == 1:
        new_time += ' (next day)'
    elif result_days > 1:
        new_time += ' (' + str(result_days) + ' days later)'

    return new_time


print(add_time('11:30 AM', '2:32', 'Monday'))
