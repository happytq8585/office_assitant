import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
import hashlib
import os.path
from tornado.options import define, options

from db.tables import query_user

define("port", default=8000, help="run on the given port", type=int)

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("username")
    def get_current_passwd(self):
        return self.get_secure_cookie("password")

class LoginHandler(BaseHandler):
    def get(self):
        self.render('login.html')
    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        if username and password:
            res = query_user(username + '\3' + password)
            if res:
                self.set_secure_cookie("username", username)
                self.redirect("/")
        self.write("login failed!")

class WelcomeHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('index.html', user=self.current_user)

class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("username")
        self.redirect("/")

class TestHandler(BaseHandler):
    def get(self):
        self.render('test.html')

if __name__ == "__main__":
    tornado.options.parse_command_line()
    settings = {
        "template_path": os.path.join(os.path.dirname(__file__), "templates"),
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
        "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
        "xsrf_cookies": True,
        "login_url": "/login" }
    application = tornado.web.Application([ (r'/', WelcomeHandler),
                                            (r'/login', LoginHandler),
                                            (r'/logout', LogoutHandler),
                                            (r'/test', TestHandler)
                                            ], **settings)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
