#import webbrowser module
import webbrowser

#Movie class where we
class Movie():
    #Initalize method that is called each time class is instantiated
    def __init__(self, title, poster_image_url, trailer_youtube_url):
    	self.title = title
    	self.poster_image_url = poster_image_url
    	self.trailer_youtube_url = trailer_youtube_url

    #Class method that opens the web browser with the class instance's YouTube URL
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    #Class method that opens the web browser and opens the instance's box art URL
    def show_poster(self):
        webbrowser.open(self.box_art_url)
