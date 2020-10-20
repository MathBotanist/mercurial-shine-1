from flask import Flask
import socketio

static_files = {
    '/': 'index.html',
    '/script.js': 'script.js'
}

sio = socketio.Server(async_mode='threading')
app = Flask(__name__)
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app, static_files=static_files)

@sio.event
def connect(sid, environ):
    print('sending hey')
    sio.emit('hey', {'data': 'heyy!!'})

if __name__ == '__main__':
    app.run(threaded=True)