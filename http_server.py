#!/usr/bin/env python3

from flask import Flask
import socketio
import db_connect

static_files = {
    '/': r'html\index.html',
    '/script.js': r'client-side-scripts\script.js',
    '/style.css': r'css\style.css',
    '/login': r'html\login.html',
    'login_style.css': r'css\login_style.css',
    'login_script.js': r'client-side-scripts\login_script.js'
}

sio = socketio.Server(async_mode='threading')
app = Flask(__name__)
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app, static_files=static_files)

@sio.event
def connect(sid, environ):
    print('sending hey')
    sio.emit('hey', {'text': 'heyy!!', 'x': 25, 'y': 50})

@sio.on('hello')
def hello(sid, *data):
    print(f'hello {data[0]}')

@sio.on('command')
def command_handler(sid, *data):
    print(data)

if __name__ == '__main__':
    app.run(threaded=True)