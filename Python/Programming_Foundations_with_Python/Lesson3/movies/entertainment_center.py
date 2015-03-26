import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story","A story about a boy and his toy that come into life",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar","A marine on an alian planet","http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")

big_hero_6 = media.Movie ("Big Hero 6","The adventure of junior robotic genius, health care robot, and other friends","http://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29_poster.jpg","https://www.youtube.com/watch?v=z3biFxZIJOQ")

#print toy_story.storyline
#avatar.show_trailer()

#print big_hero_6.title
#print big_hero_6.storyline
#big_hero_6.show_trailer()
movies=[toy_story,avatar,big_hero_6]

fresh_tomatoes.open_movies_page(movies)
print media.Movie.valid_ratings
print media.Movie.__doc__