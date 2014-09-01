import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        html = open("index.html", 'r').read()
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(html)

class MusicPage(webapp2.RequestHandler):
    def get(self):
        html = open("music.html", 'r').read()
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/music', MusicPage)
], debug=True)
