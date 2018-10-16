# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 22:08:57 2018

@author: Administrator
"""

from flask import Flask,g
from proxypool01 import RedisClient

#api_host='127.0.0.1'
#api_port=8080

__all__=['app']
app=Flask(__name__)

def get_conn():
    if not hasattr(g,'redis'):
        g.redis=RedisClient()
    return g.redis

@app.route('/')
def index():
    return '<h2>Welcome to Proxy Pool System<h2>'

@app.route('/random')
def get_proxy():
    conn=get_conn()
    return conn.random()

@app.route('/count')
def get_counts():
    conn=get_conn()
    return str(conn.count())

if __name__=='__main__':
    app.run()  #默认分配127.0.0.1:5000,也可以给端口run(api_host,api_port)














