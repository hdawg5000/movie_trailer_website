#Imports the movie and fresh_tomatoes files
import movie
import fresh_tomatoes

#Create instances of the Movie class, passing in movie title, box art URL and movie trailer URL
the_kite_runner = movie.Movie("The Kite Runner", "http://www.bdsfbd.com/wp-content/uploads/2016/05/the-kite-runner-movie.jpg", "https://www.youtube.com/watch?v=muW9Ob7V7ME")
split = movie.Movie("Split", "https://images-na.ssl-images-amazon.com/images/M/MV5BZTJiNGM2NjItNDRiYy00ZjY0LTgwNTItZDBmZGRlODQ4YThkL2ltYWdlXkEyXkFqcGdeQXVyMjY5ODI4NDk@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://www.youtube.com/watch?v=84TouqfIsiI")
the_dark_knight = movie.Movie("The Dark Knight", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg", "https://www.youtube.com/watch?v=EXeTwQWrcwY")
fury = movie.Movie("Fury", "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA4MDU0NTUyN15BMl5BanBnXkFtZTgwMzQxMzY4MjE@._V1_UY1200_CR90,0,630,1200_AL_.jpg", "https://www.youtube.com/watch?v=-OGvZoIrXpg")
lion = movie.Movie("Lion", "https://upload.wikimedia.org/wikipedia/en/f/f0/Lion_%282016_film%29.png", "https://www.youtube.com/watch?v=-RNI9o06vqo")

#Store instances of Movie in a movies array, used by the fresh_tomatoes.py file to generate an HTML file
movies = [the_kite_runner, split, the_dark_knight, fury, lion]

#Call the open_movies method in the fresh_tomatoes file to generate the HTML page that displays the movies
fresh_tomatoes.open_movies_page(movies)
