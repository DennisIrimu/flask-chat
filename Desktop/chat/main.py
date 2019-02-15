from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'illenium'
socketio = SocketIO(app)

if __name__ == '__main__'
    socket.run(app, debug=True)
