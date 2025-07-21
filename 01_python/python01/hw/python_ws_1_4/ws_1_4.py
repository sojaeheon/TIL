movies = ["inception", "interstellar","Dunkirk","Tenet"]

def get_movie_recommendation(rating):
    if rating > 9:
        print(f'Recommended movie: {movies[0]}')
    elif 8<=rating<9:
        print(f'Recommended movie: {movies[1]}')
    elif 7<=rating<8:
        print(f'Recommended movie: {movies[2]}')
    else:
        print(f'Recommended movie: {movies[3]}')

rating_input = int(input("Enter your movie rating (0~10): "))
get_movie_recommendation(rating_input)