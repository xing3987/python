# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 10:27:34 2018

@author: Administrator
"""

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello,world")
        
def make_app():
   return tornado.web.Application([(r"/",MainHandler),])

if __name__=="__main__":
    app=make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
