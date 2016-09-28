import tornado.ioloop
import tornado.web
import os.path
import tornado.httpserver

from controller.IndexHandler import IndexHandler

from config import Env

class Application(tornado.web.Application):
    """
        This is the entry point for the app.
    """
    def __init__(self):
        routes = [
            (r"/", IndexHandler),                   #GET retrieve all posts
            # (r"/(.*)", NotFoundHandler),            #404 links and everything else
        ];
        
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "View"),
            xsrf_cookies=True,
            cookie_secret=Env.COOKIE_SEC,
            debug=True,
        )
        
        # Initialize the app, passing in the handlers and settings.
        super(Application, self).__init__(routes, **settings)


if __name__ == "__main__":
    app = tornado.httpserver.HTTPServer(Application());
    app.listen(8888);
    try:
        tornado.ioloop.IOLoop.instance().start();
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.instance().stop();