import fresh_tomatoes
import media

'''
Creating instances for each Movie object that we want to create with their
respective values for Movie title, storyline, poster image and youtube trailer
'''

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")


invictus = media.Movie("Invictus",
                       """Nelson Mandela brings South Africa together
                          using Rugby as medium""",
                       "https://upload.wikimedia.org/wikipedia/en/0/05/Invictus-poster.png",  # NOQA
                       "https://www.youtube.com/watch?v=RZY8c_a_dlQ")

pride_and_prejudice = media.Movie("Pride and Prejudice",
                                  """Five sisters from an English family deal with issues of
                                     marriage, morality and misconceptions""",
                                  "https://upload.wikimedia.org/wikipedia/en/0/03/Prideandprejudiceposter.jpg",  # NOQA
                                  "https://www.youtube.com/watch?v=7Afx8MGg00g")  # NOQA

sound_of_music = media.Movie("Sound of Music",
                             """A woman leaves an Austrian convent to become a governess
                                to the children of a Naval officer widower""",
                             "https://images-na.ssl-images-amazon.com/images/I/61FezQ4Ch%2BL._SL500_AC_SS350_.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=lEcKXr3mJ_o")

xmen = media.Movie("X-Men : First Class",
                   "Story of Mutants",
                   "https://vignette2.wikia.nocookie.net/xmenmovies/images/3/3c/X-Men_First_Class_poster_2.jpg/revision/latest?cb=20110814025614",  # NOQA
                   "https://www.youtube.com/watch?v=UrbHykKUfTM")

jerry_mg = media.Movie("Jerry Maguire",
                       """A sports agent has a moral epiphany
                          and decides to work as independent agent""",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMTgxMTAxNjI2OV5BMl5BanBnXkFtZTYwNzg5ODc4._V1_.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=rCCaTPY-z4Q")


# Grouping all movie objects created in a list
movies = [toy_story, invictus, pride_and_prejudice,
          sound_of_music, xmen, jerry_mg]


'''
Calling the method to build the HTML file
for displaying the movie website with the given movie list
'''
fresh_tomatoes.open_movies_page(movies)
