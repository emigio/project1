import webbrowser
class Movie():

  """ this is class for movie for movie site """
  VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']
  def __init__ (self, movie_title, movie_storyline, movie_image, movie_youtube): 
    """Movie class takes 4 arguments, title of movie, short description, image url, and youtube url"""
    self.title = movie_title
    self.storyline = movie_storyline
    self.poster_image_url = movie_image
    self.trailer_youtube_url =movie_youtube

  
  def show_trailer(self):
    webbrowser.open(self.trailer_youtube_url)
    
