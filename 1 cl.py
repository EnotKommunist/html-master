from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/index/<name>')
def index(name):
    return render_template('first_html.html', title=name)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')