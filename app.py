try:
    import importlib

    flask = importlib.import_module("flask")
    flask_socketio = importlib.import_module("flask_socketio")
    genai = importlib.import_module("google.generativeai")

    Flask = flask.Flask
    render_template = flask.render_template
    SocketIO = flask_socketio.SocketIO
    emit = flask_socketio.emit
except ImportError as e:
    raise ImportError(
        "Missing required package. Install dependencies with: pip install flask flask-socketio google-generativeai"
    ) from e

# API KEY
genai.configure(
    api_key="AIzaSyB55gwIdxjJQrNJ5DqDo0TT7qnd_SlIwXQ"
)

# MODEL
model = genai.GenerativeModel(
    "models/gemini-2.5-flash"
)

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'

socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('index.html')

@socketio.on('send_message')
def handle_message(data):

    username = data['username']
    user_message = data['message']

    # User message
    emit('message', {
        'username': username,
        'message': user_message
    }, broadcast=True)

    try:

        response = model.generate_content(
            user_message
        )

        bot_reply = response.text

    except Exception as e:

        bot_reply = str(e)

    # AI reply
    emit('message', {
        'username': 'AI Bot',
        'message': bot_reply
    }, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)