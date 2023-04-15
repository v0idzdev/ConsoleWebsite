import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route('/')
def home():
    """Serves index.html when it is requested"""
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    """Serves the favicon when it is requested"""
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    app.run(debug=True)  # TODO: Run w/out debug during deployment
