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
                self.set_secure_cookie("priority", str(res))
                self.set_secure_cookie("agency_id", res[2][0])
                self.set_secure_cookie("agency_name", res[2][1])
                self.set_secure_cookie("branch_id", res[1][1])
                self.set_secure_cookie("branch_name", res[1][-1])
                self.redirect("/")
            else:
                self.write("login failed!")
        else:
            self.write("login failed!")

class WelcomeHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        user = self.get_secure_cookie("username")
        priority = self.get_secure_cookie("priority")
        self.render('index.html', user=user, priority=int(priority))

class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("username")
        self.redirect("/")

class CreateHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("create.html", user = self.get_secure_cookie("username"))

class AccountHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("account.html", user = self.get_secure_cookie("username"))

class CollectHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("collect.html", user = self.get_secure_cookie("username"))

class LocalHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("local.html", user = self.get_secure_cookie("username"))

class TestHandler(BaseHandler):
    @tornado.web.authenticated
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
                                            (r'/create', CreateHandler),
                                            (r'/account',AccountHandler),
                                            (r'/collect',CollectHandler),
                                            (r'/local',  LocalHandler),
                                            (r'/test', TestHandler),
                                            ], **settings)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
