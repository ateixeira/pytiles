import tornado.web
import concurrent.futures

class BaseHandler(tornado.web.RequestHandler):
    thread_pool = concurrent.futures.ThreadPoolExecutor(4);