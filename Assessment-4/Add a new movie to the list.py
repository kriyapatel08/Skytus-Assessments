#Add a new movie to the list.
favorite_movies = []
for i in range(3):
    movie = input("Enter the name of one of your favorite movies: ")
    favorite_movies.append(movie)   
new_movie = input("Enter the name of a new movie to add to the list: ")
favorite_movies.append(new_movie)
print("Updated list of your favorite movies:", favorite_movies)
