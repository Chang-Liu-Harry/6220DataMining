import os
import re
from collections import defaultdict, Counter


user_ratings_count = defaultdict(int)
users_with_exactly_200_ratings = set()
lowest_user_id_ratings = defaultdict(list)
movie_id_pattern = re.compile(r"(\d+):")
movie_id_to_name = {}
directory = './netflix'
movie_titles_file = './netflix/movie_titles.csv'

with open(movie_titles_file, 'r', encoding='ISO-8859-1') as file:
    for line in file:
        movie_id, year, title = line.strip().split(',', 2)
        movie_id_to_name[movie_id] = title

# Step 1: Iterate over each file in the directory and count movie ratings by user
for filename in os.listdir(directory):
    if filename.startswith("combined_data_") and filename.endswith(".txt"):
        with open(os.path.join(directory, filename), 'r') as file:
            current_movie_id = None
            for line in file:
                if movie_id_pattern.match(line):
                    current_movie_id = line.rstrip(':\n')
                else:
                    user_id, rating, _ = line.strip().split(",")
                    user_ratings_count[user_id] += 1
                    if int(rating) == 5:
                        lowest_user_id_ratings[user_id].append(current_movie_id)

# Step 2: Find users who have rated exactly 200 movies and the one with the lowest ID
for user_id, count in user_ratings_count.items():
    if count == 200:
        users_with_exactly_200_ratings.add(user_id)

lowest_user_id = min(users_with_exactly_200_ratings, key=int)

# Step 3: Print the names of the movies that the lowest user ID rated with 5 stars
lowest_user_movie_names = [movie_id_to_name[movie_id] for movie_id in lowest_user_id_ratings[lowest_user_id]]

number_of_users = len(users_with_exactly_200_ratings)
lowest_user_favorite_movies = Counter(lowest_user_movie_names)

print(f"Number of users who rated exactly 200 movies: {number_of_users}")
print(f"Movies rated 5 stars by user {lowest_user_id}:")
for movie, count in lowest_user_favorite_movies.items():
    print(f"{movie} (rated {count} times)")