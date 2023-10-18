from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def about():
    return render_template('about.html')

@app.route('/contac')
def сcontac():
    return render_template('contac.html')

@app.route('/about')
def index():
    return render_template('index.html')


@app.route('/negp')
def negp():
    return render_template('negp.html')


app.run(port=2023)
