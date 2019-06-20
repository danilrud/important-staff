import media
import fresh_tomatoes
toy_story=media.Movie('Toy Story',
                      'A story of a boy and his toys that come to life',
                      'https://vignette.wikia.nocookie.net/disney/images/a/a3/Toy_Story_3_-_Poster_3.jpg/revision/latest?cb=20160408191136',
                      'https://www.youtube.com/watch?v=rNk1Wi8SvNc',1995,81)
#print(toy_story.storyline)
avatar=media.Movie('Avatar',
                   'A marine on an alien planet',
                   'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
                   'https://www.youtube.com/watch?v=5PSNL1qE6VY',2009,161)
#print(avatar.storyline)

interstellar=media.Movie('Interstellar',
                         'film about a group of astronauts who travel through a wormhole near Saturn in search of a new home for humanity',
                         'https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg',
                         'https://www.youtube.com/watch?v=zSWdZVtXT7E',2014,169)
#print(interstellar.storyline)
#interstellar.show_trailer()
school_of_rock=media.Movie('School of Rock','Using rock music to learn',
                           'https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg',
                           'https://www.youtube.com/watch?v=XCwy6lW5Ixc',2003,109)
harry_potter=media.Movie('Harry Potter','A story about magic world',
                         'https://st.kp.yandex.net/images/film_big/689.jpg',
                         'https://www.youtube.com/watch?v=VyHV0BRtdxo',2001,152)
hunger_games=media.Movie('Hunger Games','A really real reality show',
                         'https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg',
                         'https://www.youtube.com/watch?v=mfmrPu43DF8',2012,142)
movies=[toy_story, avatar, school_of_rock, interstellar, harry_potter, hunger_games,]
fresh_tomatoes.open_movies_page(movies)
#avatar.rating=8.7
#avatar.description()
#harry_potter.description()
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
big_bang_theory=media.TV_Show(12,22,'Big Bang Theory','https://upload.wikimedia.org/wikipedia/en/7/7b/The_Big_Bang_Theory_%28Official_Title_Card%29.png',
                              'A story about four phisisists and a blond girl ','https://www.youtube.com/watch?v=hakAG8PlBKQ')
movies=[toy_story, avatar, school_of_rock, interstellar, harry_potter, hunger_games,big_bang_theory]
fresh_tomatoes.open_movies_page(movies)

