import os
from flask import Flask, render_template, send_from_directory
from flask_assets import Environment, Bundle

app = Flask(__name__)
assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('main.scss', filters='pyscss', output='all.css')
assets.register('scss_all', scss)


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
