from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')
def index():
    color = generate_color()
    return render_template('index.html', color=color)

@app.route('/page1')
def page1():
    color = generate_color()
    return render_template('page1.html', color=color)

@app.route('/page2')
def page2():
    color = generate_color()
    return render_template('page2.html', color=color)

@app.route('/page3')
def page3():
    color = generate_color()
    return render_template('page3.html', color=color)


def generate_color():
    colors = ['red', 'blue', 'green', 'yellow', 'purple']
    return random.choice(colors)

if __name__ == '__main__':
    app.run()
