import webbrowser

'''
Class that incorporates characteristics of a movie like title, storyline,
poster image and youtube url
'''


class Movie():

    # Constructor method
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Method to play the trailer of the movie when its poster image is clicked
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
