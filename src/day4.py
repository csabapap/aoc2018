import operator


def order_log(shift_log):
    entries = {}
    for log_entry in shift_log:
        datetime, log = log_entry.split("] ")
        entries[datetime[1:]] = log.rstrip()

    return sorted(entries.items(), key=operator.itemgetter(0))


def part1(shift_log):
    logs = order_log(shift_log)
    guard_id = 0
    asleep_at = 0
    guards_sleep_time = {}
    for datetime, entry in logs:
        if entry.startswith("Guard"):
            guard_id = entry.split('#')[1].split()[0]
            asleep_at = 0
        if entry.startswith("falls"):
            asleep_at = datetime.split(':')[1]
        if entry.startswith("wakes"):
            wakes_up = datetime.split(':')[1]
            if guard_id not in guards_sleep_time:
                guards_sleep_time[guard_id] = 0
            guards_sleep_time[guard_id] += int(wakes_up) - int(asleep_at)

    laziest_guard_id = max(guards_sleep_time.items(), key=operator.itemgetter(1))[0]
    print(laziest_guard_id)
    laziest_guard = False
    start = 0
    minutes = [0 for i in range(60)]
    for datetime, entry in logs:
        if entry.startswith("Guard"):
            if entry.split('#')[1].split()[0] != laziest_guard_id:
                laziest_guard = False
                continue
            laziest_guard = True
            continue
        if laziest_guard and entry.startswith("falls"):
            start = int(datetime.split(':')[1])
            continue
        if laziest_guard and entry.startswith("wakes"):
            end = int(datetime.split(':')[1])
            for i in range(start, end):
                minutes[i] += 1
        start = 0
    nmb = 0
    max_index = 0
    index = 0
    for nmb_of_minutes in minutes:
        if nmb_of_minutes > nmb:
            nmb = nmb_of_minutes
            max_index = index
        index += 1
    print(max_index)


if __name__ == '__main__':
    file = open("../assets/day4-input.txt", 'r')
    part1(file)