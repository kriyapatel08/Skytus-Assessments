#Remove the first movie from the list.
favorite_movies = []
for i in range(3):       
    movie = input("Enter the name of one of your favorite movies: ")
    favorite_movies.append(movie)
print("Your favorite movies are:", favorite_movies)
removed_movie = favorite_movies.pop(0)
print("Removed the first movie: ", removed_movie)
print("Updated list of your favorite movies: ", favorite_movies)
