import os
import tornado.ioloop
import tornado.web
import tornado.autoreload
import os.path

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        items = ["Item 1","Item 2","Item 3"]
    	self.render("template_test.html", title="My Title",items=items)

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    
    tornado.autoreload.start()
    #tornado.autoreload.add_reload_hook("server started/restarted")
    
    template_path = '/home/mstiller/tornado_dev'
    for filename in os.listdir(template_path):
    	tornado.autoreload.watch(os.path.abspath(os.path.join(template_path, filename)))
    
    tornado.ioloop.IOLoop.current().start()