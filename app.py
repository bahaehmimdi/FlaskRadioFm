from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/start_call')
def start_call():
    return render_template('start_call.html')

@app.route('/receive_call')
def receive_call():
    return render_template('receive_call.html')

@socketio.on('start_call')
def handle_start_call(message):
    socketio.emit('start_call', message)

@socketio.on('receive_call')
def handle_receive_call(message):
    socketio.emit('receive_call', message)

if __name__ == '__main__':
    socketio.run(app, debug=True)

