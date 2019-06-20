import webbrowser
class Video():
    def __init__(self,title,storyline,poster_image,trailer_youtube):
        self.title=title
        self.storyline=storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube
        def show_trailer(self):
            webbrowser.open(self.trailer_youtube_url)
    
class Movie(Video):
    """some documentation here"""
    rating=None
    VALID_RATINGS=['G','PG','PG-13','R',]
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube,year,movie_duration):
        Video.__init__(self,movie_title,movie_storyline,poster_image,trailer_youtube)
        self.year=year
        self.duration=movie_duration
        
    def description(self):
        print(self.title,'-',self.storyline+'.','Was released in',self.year)
        if not self.rating==None:
            print('Rated as',self.rating)
            
        
class TV_Show(Video):
    def __init__(self,number_of_seasons,number_of_episodes,show_title,poster_image,show_storyline,
                 trailer_youtube):
        Video.__init__(self,show_title,show_storyline,poster_image,trailer_youtube)
        self.seasons=number_of_seasons
        self.episods=number_of_episodes

