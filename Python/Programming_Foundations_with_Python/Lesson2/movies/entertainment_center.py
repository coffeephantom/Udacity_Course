import media

toy_story = media.Movie("Toy Story","A story about a boy and his toy that come into life",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar","A marine on an alian planet","http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")

print toy_story.storyline
avatar.show_trailer()