# Given a calendar schedule
# Business hour: 9am-5pm
# Find the maximum number of 30 minute slots

schedule = [
    [
        {"time": "09:30", "duration": 30},
        {"time": "11:15", "duration": 45},
        {"time": "12:30", "duration": 15},
        {"time": "14:30", "duration": 30},
        {"time": "15:30", "duration": 30},
    ],
    [
        {"time": "10:30", "duration": 30},
        {"time": "11:45", "duration": 15},
        {"time": "12:30", "duration": 15},
        {"time": "13:30", "duration": 15},
        {"time": "15:30", "duration": 15},
    ],
    [
        {"time": "09:00", "duration": 30},
        {"time": "12:00", "duration": 60},
        {"time": "14:30", "duration": 15},
        {"time": "15:30", "duration": 30},
        {"time": "16:30", "duration": 30},
    ],
    [
        {"time": "09:30", "duration": 30},
        {"time": "11:15", "duration": 45},
        {"time": "12:30", "duration": 15},
        {"time": "13:30", "duration": 15},
        {"time": "14:30", "duration": 30},
        {"time": "15:30", "duration": 30},
        {"time": "16:30", "duration": 15},
    ],
    [
        {"time": "09:30", "duration": 30},
        {"time": "12:15", "duration": 45},
        {"time": "15:30", "duration": 60},
    ],
]


ans = []


for day in schedule:
    current_time = 9 * 60
    end_time = 17 * 60
    slot_30 = 0
    for meeting in day:
        hour, min = meeting["time"].split(":")
        start_time = int(hour) * 60 + int(min)
        finish_time = int(hour) * 60 + int(min) + meeting["duration"]

        if start_time - current_time >= 30:

            slot_30 += (start_time - current_time) // 30

        current_time = finish_time

    if end_time - current_time >= 30:
        slot_30 += (end_time - current_time) // 30

    ans.append(slot_30)

print(ans)
