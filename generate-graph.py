import os
from random import randint
from datetime import datetime, timedelta

# Set your desired start and end dates in yyyy-mm-dd format and the maximum number of commits per day
start_date_str = "2020-05-01"
end_date_str = "2020-05-25"
max_commits_per_day = 5

# Convert start and end date strings to datetime objects
start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

# Loop through the date range
current_date = start_date
while current_date < end_date:
    # Generate a random number of commits for the current day, up to the specified maximum
    for _ in range(0, randint(0, max_commits_per_day)):
        current_day_str = current_date.strftime("%Y-%m-%d")
        with open('file.txt', 'a') as file:
            file.write(current_day_str + '\n')  # Add a newline character for better readability
        os.system('git add .')
        os.system('git commit --date="{}" -m "commit"'.format(current_day_str))

    current_date += timedelta(days=1)

os.system('git push -u origin master ')
