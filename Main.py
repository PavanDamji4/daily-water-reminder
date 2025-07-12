import time
from datetime import datetime
from plyer import notification

# Setting Custom Time
reminder_times = [
    "07:00",
    "10:00",
    "14:00",
    "17:00",
    "20:00",
    "22:00"
]

notified_today = set()

def send_notification():
    notification.notify(
        title=" Time to Drink Water!",
        message="Stay healthy, drink a glass of water now!",
        timeout=10
    )

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")

    # Reset time
    if current_time == "00:00":
        notified_today.clear()

    if current_time in reminder_times and current_time not in notified_today:
        send_notification()
        notified_today.add(current_time)

    time.sleep(60)  # check every 1 min
