import csv
from collections import defaultdict

# Function to solve question 4a and 4b
def analyze_movie_titles(file_path):
    with open(file_path, mode='r', encoding='utf-8', errors='ignore') as file:
        csv_reader = csv.reader(file)
        movie_name_year_pairs = [(row[2], row[1]) for row in csv_reader if row]  # Extract movie name-year pairs

    # Count distinct movie names for 4a
    unique_movie_names_count = len(set(name for name, year in movie_name_year_pairs))

    # Count how many movie names occur in four or more different years for 4b
    movie_name_to_years = defaultdict(set)
    for name, year in movie_name_year_pairs:
        movie_name_to_years[name].add(year)
    movies_with_four_or_more_years = sum(1 for years in movie_name_to_years.values() if len(years) >= 4)

    return unique_movie_names_count, movies_with_four_or_more_years


file_path = './netflix/movie_titles.csv'


unique_movie_names_count, movies_with_four_or_more_years = analyze_movie_titles(file_path)
print(f"Number of movies with unique names: {unique_movie_names_count}")
print(f"Number of movie names that refer to four or more different movies (in different years): {movies_with_four_or_more_years}")
