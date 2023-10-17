from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')
def index():
    color = generate_color()
    return render_template('index.html', color=color)

def generate_color():
    colors = ['red', 'blue', 'green', 'yellow', 'purple']
    return random.choice(colors)

if __name__ == '__main__':
    app.run()
