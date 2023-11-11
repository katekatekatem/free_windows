BUSY = [
    {'start': '10:30', 'stop': '10:50'},
    {'start': '18:40', 'stop': '18:50'},
    {'start': '14:40', 'stop': '15:50'},
    {'start': '16:40', 'stop': '17:20'},
    {'start': '20:05', 'stop': '20:20'}
]

START_TIME = '09:00'
END_TIME = '21:00'
INTERVAL = 30


def time_to_minutes(time):
    hours, minutes = map(int, time.split(':'))
    return hours * 60 + minutes


def minutes_to_time(minutes):
    hours = minutes // 60
    minutes = minutes % 60
    return '{0:02d}:{1:02d}'.format(hours, minutes)


def create_windows():
    start = time_to_minutes(START_TIME)
    end = time_to_minutes(END_TIME)
    intervals = []
    interval_start = start

    while interval_start < end:
        is_busy = False

        for busy_interval in BUSY:
            busy_start = time_to_minutes(busy_interval['start'])
            busy_end = time_to_minutes(busy_interval['stop'])
            interval_end = interval_start + INTERVAL
            if (interval_start <= busy_end and interval_end > busy_start):
                is_busy = True
                break

        if not is_busy:
            intervals.append([interval_start, interval_end])

        interval_start += INTERVAL           

    return intervals


def format_free_windows():
    free_windows = create_windows()
    formatted_free_windows = []

    for window in free_windows:
        formatted_window = 'Свободное окно: {} - {}'.format(
            minutes_to_time(window[0]),
            minutes_to_time(window[1])
        )
        formatted_free_windows.append(formatted_window)

    return formatted_free_windows


if __name__ == '__main__':
    print(*format_free_windows(), sep='\n')
