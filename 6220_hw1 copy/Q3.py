import os
import re


file_pattern = re.compile(r'combined_data_\d+\.txt$')
total_ratings = 0
unique_users = set()
years = set()
directory = './netflix'


for filename in os.listdir(directory):
    if file_pattern.match(filename):
        with open(os.path.join(directory, filename), 'r') as file:
            for line in file:
                if ',' in line:
                    #Q_3.1
                    total_ratings += 1
                    user_id, rating, date = line.split(',')
                    #Q 3.2
                    unique_users.add(user_id.strip())
                    year = date.split('-')[0].strip()
                    years.add(year)
#Q_3.3
if years:
    min_year = min(years)
    max_year = max(years)
else:
    min_year = max_year = None

print(f"Total number of ratings: {total_ratings}")
print(f"Total number of unique users: {len(unique_users)}")
print(f"Range of years: {min_year} to {max_year}")