from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/index/<name>')
def index(name):
    return render_template('first_html.html', title=name)


@app.route('/training/<prof>')
def training(prof):
    if 'инженер' in prof.lower() or 'строитель' in prof.lower():
        return render_template('training.html', title='Инженерные тренажеры',
                               inmage=url_for('static', filename='plane-ENG.gif'))

    else:
        return render_template('training.html', title='Научные симуляторы',
                               inmage=url_for('static', filename='plane-Lab.gif'))

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')