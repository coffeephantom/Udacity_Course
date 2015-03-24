import media

toy_story = media.Movie("Toy Story","A story about a boy and his toy that come into life",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar","A marine on an alian planet","http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")

big_hero_6 = media.Movie ("Big Hero 6","The adventure of junior robotic genius, health care robot, and other friends","https://en.wikipedia.org/wiki/Big_Hero_6_(film)#/media/File:Big_Hero_6_(film)_poster.jpg","https://www.youtube.com/watch?v=z3biFxZIJOQ")

#print toy_story.storyline
#avatar.show_trailer()

print big_hero_6.title
print big_hero_6.storyline
big_hero_6.show_trailer()