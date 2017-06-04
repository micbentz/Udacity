import webbrowser


class Movie():
    """This class represents a movie

    Attributes:
        title: The movie's title
        story_line: A short description of the movie's plot
        poster_url: The URL of the movie poster
        trailer_url: The URL of the movie trailer
    """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, storyline, poster_url, trailer_url):
        """Inits Movie with the title, storyline, poster URL and trailer URL"""
        self.title = title
        self.storyline = storyline
        self.poster_url = poster_url
        self.trailer_url = trailer_url

    def show_trailer(self):
        """Opens default browswer with the movie trailer"""
        webbrowser.open(self.trailer_url)
