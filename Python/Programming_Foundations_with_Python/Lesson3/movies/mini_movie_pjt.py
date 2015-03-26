
import media
import fresh_tomatoes

big_hero_6 = media.Movie ("Big Hero 6","The adventure of junior robotic genius, health care robot, and other friends","http://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29_poster.jpg","https://www.youtube.com/watch?v=z3biFxZIJOQ")

monsters_university = media.Movie("Monster University","Monster learn how to scary people","http://upload.wikimedia.org/wikipedia/en/2/2a/Monsters_University_poster_3.jpg","https://www.youtube.com/watch?v=QxrQ6BaijAY")


harry_potter = media.Movie("Harry Potter","The growth of a boy wizard","http://upload.wikimedia.org/wikipedia/en/d/df/Harry_Potter_and_the_Deathly_Hallows_%E2%80%93_Part_2.jpg","https://www.youtube.com/watch?v=_EC2tmFVNNE")

pirates_of_caribbean = media.Movie("Pirates of the Caribbean","A Legendary story of the Captain","http://upload.wikimedia.org/wikipedia/en/5/5a/Pirates_AWE_Poster.jpg","https://www.youtube.com/watch?v=naQr0uTrH_s")

favorite_movies=[big_hero_6, monsters_university,harry_potter,pirates_of_caribbean]

fresh_tomatoes.open_movies_page(favorite_movies)




