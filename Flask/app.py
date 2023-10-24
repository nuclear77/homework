from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///event_registration.db'
db = SQLAlchemy(app)

class Attendee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    event = db.Column(db.String(100))

    def __init__(self, name, email, event):
        self.name = name
        self.email = email
        self.event = event

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    event = request.form['event']

    attendee = Attendee(name, email, event)
    db.session.add(attendee)
    db.session.commit()

    return render_template('success.html', name=name, event=event)

@app.route('/visitors/<event>')
def attendees(event):
    attendees = Attendee.query.filter_by(event=event).all()
    return render_template('attendees.html', event=event, attendees=attendees)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)