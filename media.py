import webbrowser

 # Base Classe Video
class Video():

        def __init__(self, title, duration, producer):
           self.title = title
           self.duration = duration
           self.producer = producer

        def show__trailer(self):
                webbrowser.open(self.trailer_youtube_url)

# Classe that implements heritage and define a movie 
class Movie(Video):
        def __init__(self, title, duration, producer, storyline, poster_image,trailer_youtube):
                Video.__init__(self, title, duration, producer)
                self.storyline = storyline
                self.poster_image_url = poster_image
                self.trailer_youtube_url = trailer_youtube

# Classe that implements heritage and define a serie
class Serie(Video):
        def __init__(self, title, duration, producer, storyline, poster_image,trailer_youtube, episodes):
                Video.__init__(self, title, duration, producer)
                self.storyline = storyline
                self.poster_image_url = poster_image
                self.trailer_youtube_url = trailer_youtube
                self.episodes = episodes
