import csv


def merge_movie_data():
    movies = {}
    with open('movies.csv', 'r') as file1, open('movie_details.csv', 'r') as file2:
        reader1 = csv.DictReader(file1)
        reader2 = csv.DictReader(file2)
        
        for row in reader1:
            movie_id = int(row['id'])
            movies[movie_id] = {
                'id': movie_id,
                'title': row['title'],
                'release_date': row['release_date'],
                'popularity': float(row['popularity'])
            }
            
        for row in reader2:
            movie_id = int(row['movie_id'])
            if movie_id in movies:
                movies[movie_id]['budget'] = int(row['budget'])
                movies[movie_id]['revenue'] = int(row['revenue'])
                movies[movie_id]['runtime'] = int(row['runtime'])
                
        
    # Save the movies data to a file
    with open('processed/movies_processed.csv', 'w', newline='') as outfile:
        fieldnames = ['id', 'title', 'release_date', 'popularity', 'budget', 'revenue', 'runtime']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for movie in movies.values():
            writer.writerow(movie)
            

def reviews_to_csv():
    reviews = []
    with open('movie_reviews.csv', 'r') as file:
        reader = csv.DictReader(file)
        for idx, row in enumerate(reader):
            reviews.append({
                'id': idx + 1,
                'movie_id': int(row['movie_id']),
                'author': row['author'],
                'content': row['content'],
                'rating': float(row['rating'])
            })
    
    # Save the reviews data to a file
    with open('processed/reviews_processed.csv', 'w', newline='') as outfile:
        fieldnames = ['id', 'movie_id', 'author', 'content', 'rating']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for review in reviews:
            writer.writerow(review)
            
            
def cast_to_csv():
    casts = []
    with open('movie_cast.csv', 'r') as file:
        reader = csv.DictReader(file)
        for idx, row in enumerate(reader):
            casts.append({
                'id': idx + 1,
                'movie_id': int(row['movie_id']),
                'name': row['name'],
                'character': row['character'],
                'order': int(row['order'])
            })
    
    # Save the casts data to a file
    with open('processed/casts_processed.csv', 'w', newline='') as outfile:
        fieldnames = ['id', 'movie_id', 'name', 'character', 'order']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for cast in casts:
            writer.writerow(cast)
            
            
def genre_to_csv():
    with open('movie_details.csv', 'r') as file:
        reader = csv.DictReader(file)
        genre_data = set()
        movie_genres = []
        count_id = 1
        for row in reader:
            current_genre = row['genres'].split(',')
            for genre in current_genre:
                genre_data.add(genre)
                movie_genres.append({
                    'id': count_id,
                    'movie_id': int(row['movie_id']),
                    'genre_id': genre
                })
       
    genre_id_map = {genre: idx + 1 for idx, genre in enumerate(genre_data)} 
    with open('processed/genres_processed.csv', 'w', newline='') as outfile:
        fieldnames = ['id', 'name']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for genre, idx in genre_id_map.items():
            writer.writerow({'id': idx, 'name': genre})
            
            
    with open('processed/movie_genres_processed.csv', 'w', newline='') as outfile:
        fieldnames = ['id', 'movie_id', 'genre_id']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for idx, movie_genre in enumerate(movie_genres):
            writer.writerow({'id': idx+1, 'movie_id': movie_genre['movie_id'], 'genre_id': genre_id_map[movie_genre['genre_id']]})
            
        
        
if __name__ == "__main__":
    genre_to_csv()